# tests/integration/test_ollama_extraction.py
import json
import pytest
from unittest.mock import patch, MagicMock
from src.ai.ollama_client import OllamaAIService
from src.domain.entities import CandidateProfile

@patch('src.ai.ollama_client.requests.post')
def test_ollama_extract_profile_success(mock_post):
    """Valida el flujo completo: el cliente envía el formato correcto
    y parsea la respuesta JSON simulada de Ollama de forma exitosa.
    """
    # 1. Configurar el falso contenido respetando la jerarquía exacta del Dominio
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "message": {
            "content": json.dumps({
                "personal": {
                    "full_name": "Juan Pérez",
                    "email": "juan@example.com"
                },
                "professional": {
                    "target_roles": ["Backend Developer"],
                    "years_of_experience": 3.5
                },
                "experience": [],
                "skills": {
                    "hard_skills": ["Python", "Git"],
                    "soft_skills": ["Comunicación"]
                },
                "languages": []
            })
        }
    }
    mock_post.return_value = mock_response

    # 2. Instanciar el servicio de infraestructura
    service = OllamaAIService()
    
    # 3. Ejecutar la extracción con un texto bruto simulado
    raw_text = "Juan Pérez, mail: juan@example.com, sabe Python y Git."
    profile_dict = service.extract_profile(raw_text)

    # 4. Asertar que la petición HTTP se armó con los parámetros correctos
    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert kwargs["json"]["format"] == "json"
    assert kwargs["json"]["options"]["temperature"] == 0.0

    # 5. Validar que los datos devueltos sirvan para instanciar CandidateProfile exitosamente
    profile = CandidateProfile(**profile_dict)
    assert profile.personal.full_name == "Juan Pérez"
    assert profile.personal.email == "juan@example.com"
    assert "Python" in profile.skills.hard_skills
    assert "Comunicación" in profile.skills.soft_skills
    # Comprobar que los campos ausentes usen los defaults de Pydantic
    assert profile.personal.phone is None