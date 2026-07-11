# src/ai/ollama_client.py
import json
from typing import List

# Intentamos importar ollama de forma segura. Si no está instalado, guardamos None.
try:
    import ollama
except ImportError:
    ollama = None

from src.domain.interfaces import AIService
from src.domain.entities import CandidateProfile, JobOffer, MatchResult
from src.core.config import config

class OllamaAIService(AIService):
    """Implementación concreta de la IA utilizando Ollama corriendo en local."""

    def __init__(self):
        # Si el usuario intenta inicializar este servicio pero no instaló la librería:
        if ollama is None:
            raise RuntimeError(
                "❌ Error: La librería 'ollama' no está instalada.\n"
                "Por favor, ejecutá el instalador interactivo: python install.py "
                "y seleccioná la opción [1] Local."
            )
            
        self.model_name = config.active_ai.model       
        self.temperature = config.active_ai.temperature 
        self.client = ollama.Client(host=config.active_ai.base_url)

    def analyze_compatibility(self, profile: CandidateProfile, job: JobOffer) -> MatchResult:
        prompt = f"""
        Sos un reclutador experto en tecnología (Tech Recruiter) y un especialista en sistemas ATS.
        Tu tarea es evaluar la compatibilidad entre el Perfil del Candidato y la Oferta de Trabajo provista.

        [PERFIL DEL CANDIDATO]
        - Roles objetivo: {', '.join(profile.target_roles)}
        - Experiencia: {profile.experience_years} años.
        - Habilidades principales: {', '.join(profile.skills)}
        - Resumen profesional: {profile.experience_summary}

        [OFERTA DE TRABAJO]
        - Puesto: {job.title}
        - Empresa: {job.company}
        - Descripción completa: {job.description}

        INSTRUCCIONES DE SALIDA:
        Debes responder ESTRICTAMENTE con un objeto JSON válido. No agregues texto introductorio ni explicaciones fuera del JSON.
        El formato del JSON debe ser exactamente el siguiente:
        {{
            "score": <un número entero de 0 a 100>,
            "matching_skills": ["habilidad1", "habilidad2"],
            "missing_skills": ["habilidad_faltante"],
            "justification": "<explicación en español de 2 o 3 oraciones>"
        }}
        """
        try:
            response = self.client.generate(
                model=self.model_name,
                prompt=prompt,
                options={"temperature": self.temperature},
                format="json"
            )
            result_data = json.loads(response['response'])
            score = result_data.get("score", 0)
            is_approved = score >= config.search.min_match_score

            return MatchResult(
                job_id=job.id,
                score=score,
                matching_skills=result_data.get("matching_skills", []),
                missing_skills=result_data.get("missing_skills", []),
                justification=result_data.get("justification", "Sin justificación."),
                is_approved=is_approved
            )
        except Exception as e:
            return MatchResult(
                job_id=job.id, score=0, matching_skills=[], missing_skills=[],
                justification=f"Error crítico al procesar con Ollama: {str(e)}", is_approved=False
            )

    def extract_keywords(self, text: str) -> List[str]:
        return []