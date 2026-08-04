# src/ai/ollma_client.py
import json
import logging
import requests
from src.domain.interfaces import AIService
from src.domain.entities import CandidateProfile
from src.ai.prompt_builder import PromptBuilder

class OllamaAIService(AIService):
    """Implementación del servicio de IA utilizando Ollama local (ADR 0006)."""
    
    def __init__(self, config: dict = None) -> None:
        self.logger = logging.getLogger(__name__)
        self.config = config or {}
        self.base_url = self.config.get("base_url", "http://localhost:11434")
        self.model_name = self.config.get("model", "llama3")
        self._prompt_builder = PromptBuilder()

    def extract_profile(self, raw_text: str, prompt_instructions: str = None) -> dict:
        """Envía el texto bruto del CV a Ollama forzando el formato JSON 
        y aplicando las directivas rígidas de extracción pura.
        """
        system_prompt = prompt_instructions or self._prompt_builder.build_system_instructions()
        user_message = self._prompt_builder.build_user_message(raw_text)
        
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            "stream": False,
            "options": {
                "temperature": 0.0
            },
            "format": "json"
        }

        try:
            self.logger.info(f"Iniciando extracción de perfil con el modelo local: {self.model_name}")
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status()

            result_json = response.json()
            response_content = result_json.get("message", {}).get("content", "{}")
            
            profile_data = json.loads(response_content)

            # --- SANEAMIENTO DEFENSIVO ---
            # Descartar idiomas nulos o vacíos
            if isinstance(profile_data.get("languages"), list):
                profile_data["languages"] = [
                    lang for lang in profile_data["languages"]
                    if isinstance(lang, dict) and lang.get("language")
                ]

            # Descartar experiencias sin empresa ni rol
            if isinstance(profile_data.get("experience"), list):
                profile_data["experience"] = [
                    exp for exp in profile_data["experience"]
                    if isinstance(exp, dict) and (exp.get("company") or exp.get("role"))
                ]

            return profile_data

        except requests.RequestException as e:
            self.logger.error(f"Error de comunicación con el servicio local de Ollama: {str(e)}")
            raise RuntimeError(f"Servicio de IA local inaccesible: {str(e)}")
        except json.JSONDecodeError as e:
            self.logger.error(f"El LLM devolvió un formato JSON corrupto o inválido: {str(e)}")
            raise ValueError(f"Respuesta de la IA no estructurable: {str(e)}")