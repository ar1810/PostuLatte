# src/ai/prompt_builder.py
import json
from src.domain.entities import CandidateProfile

class PromptBuilder:
    """Encargado de estructurar las instrucciones del sistema embebiendo
    el esquema JSON que exige Pydantic para el perfil del candidato,
    garantizando el cumplimiento de la Política de Extracción Pura.
    """
    
    def __init__(self) -> None:
        # Extraemos el esquema JSON nativo de Pydantic V2 de forma dinámica
        self._schema = CandidateProfile.model_json_schema()

    def build_system_instructions(self) -> str:
        """Genera el System Prompt rígido con el esquema inyectado y la directiva
        estricta de inicialización de datos ausentes mediante contenedores vacíos.
        """
        rules = (
            "Eres un sistema ATS (Applicant Tracking System) de ultra-precisión.\n"
            "Tu única tarea es extraer información estructurada a partir del texto bruto de un Currículum Vitae.\n\n"
            "⚠️ REGLAS CRÍTICAS DE EXTRACCIÓN PURA:\n"
            "1. Cero Tolerancia a la Alucinación: Si un dato NO está explícitamente mencionado en el texto del CV, "
            "debes inicializar el campo estrictamente vacío ([] para colecciones o listas, y \"\" para campos de texto/strings). "
            "Bajo ninguna circunstancia debes asumir, deducir, extrapolar o inventar información.\n"
            "2. Formato de Salida Estricto: Tu respuesta debe ser ÚNICAMENTE el objeto JSON válido que coincida exactamente "
            "con el esquema provisto abajo.\n"
            "3. No incluyas explicaciones, introducciones, saludos ni bloques de código de markdown (como ```json o ```). "
            "Devuelve el texto JSON crudo y limpio listo para ser parseado.\n\n"
            "Esquema JSON requerido:\n"
        )
        return f"{rules}{json.dumps(self._schema, ensure_ascii=False, indent=2)}"

    def build_user_message(self, raw_text: str) -> str:
        """Formatea el texto bruto del CV para el mensaje del usuario de manera aislada."""
        return f"Texto bruto del CV a procesar:\n\n{raw_text}"