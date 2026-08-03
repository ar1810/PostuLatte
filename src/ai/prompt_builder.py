# src/ai/prompt_builder.py
import json

class PromptBuilder:
    """Encargado de estructurar las instrucciones del sistema garantizando 
    la extracción de datos al formato del CandidateProfile.
    """

    def __init__(self) -> None:
        self._template = {
            "personal": {
                "full_name": "Nombre completo",
                "email": "correo@ejemplo.com",
                "phone": "+123456789",
                "location": "Ciudad, País",
                "linkedin": "URL de LinkedIn",
                "website": "URL de portfolio/GitHub"
            },
            "professional": {
                "target_roles": ["Rol o puesto principal"],
                "years_of_experience": 0.0
            },
            "experience": [
                {
                    "company": "Empresa",
                    "role": "Cargo",
                    "period_from": "Fecha inicio",
                    "period_to": "Fecha fin o Actualidad",
                    "description": "Logros y tareas principales"
                }
            ],
            "skills": {
                "hard_skills": ["Habilidad técnica 1"],
                "soft_skills": ["Habilidad blanda 1"]
            },
            "languages": [
                {
                    "language": "Español",
                    "level": "Nativo"
                }
            ]
        }

    def build_system_instructions(self) -> str:
        instructions = (
            "Eres un sistema ATS (Applicant Tracking System) de ultra-precisión.\n"
            "Tu única tarea es extraer información estructurada a partir del texto bruto de un Currículum Vitae "
            "completando la estructura JSON provista.\n\n"
            "⚠️ REGLAS CRÍTICAS DE EXTRACCIÓN:\n"
            "1. Extrae todos los datos reales explícitamente presentes en el CV.\n"
            "2. Para campos simples (texto o número) que NO estén presentes, asigna null.\n"
            "3. Para listas/colecciones (`experience`, `languages`, `hard_skills`, etc.), si NO hay datos o información aplicable, DEBES devolver una lista vacía `[]`. NO incluyas objetos con campos null dentro de las listas.\n"
            "4. En la lista `languages`, cada objeto DEBE incluir obligatoriamente el nombre del idioma en la clave 'language' (string válido).\n"
            "5. Formato de Salida Estricto: Tu respuesta debe ser ÚNICAMENTE el objeto JSON válido.\n"
            "6. NO incluyas explicaciones, introducciones, saludos ni bloques de código markdown (```json).\n\n"
            f"Estructura JSON requerida:\n{json.dumps(self._template, ensure_ascii=False, indent=2)}"
        )
        return instructions

    def build_user_message(self, raw_text: str) -> str:
        """Formatea el texto bruto del CV para el mensaje del usuario."""
        return f"Texto bruto del CV a procesar:\n\n{raw_text}"