# src/ai/ollama_client.py
import json
import logging
# ... (otras importaciones que tengas de HTTP o clientes de ollama)

from src.domain.interfaces import AIService
from src.domain.entities import CandidateProfile  # Traemos solo el perfil consolidado

class OllamaAIService(AIService):
    """Implementación del servicio de IA utilizando Ollama local."""
    
    def __init__(self, config=None):
        self.logger = logging.getLogger(__name__)
        # Tu inicialización del cliente...

    def extract_profile(self, raw_text: str, prompt_instructions: str) -> dict:
        """Implementación de la extracción usando Ollama."""
        # Tu lógica actual...
        pass

    # Recordatorio: El método match_job se comentará/eliminará temporalmente 
    # hasta el sprint correspondiente para que no pida JobOffer.