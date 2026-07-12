import pytest
from pydantic import ValidationError
from src.domain.entities import CandidateProfile, ExperienceHito

def test_candidate_profile_creation_with_full_data():
    """Verifica que un perfil con datos completos se instancie y tipifique correctamente."""
    data = {
        "personal": {
            "full_name": "Juan Pérez",
            "email": "juan.perez@email.com",
            "phone": "+54 351 1234567",
            "location": "Córdoba, Argentina",
            "linkedin": "linkedin.com/in/juanperez"
        },
        "professional": {
            "target_roles": ["Backend Developer"],
            "years_of_experience": 3.5
        },
        "experience": [
            {
                "company": "Tech Solutions",
                "role": "Python Developer",
                "period_from": "2023-01",
                "period_to": "Actualidad",
                "description": "Desarrollo de APIs REST"
            }
        ],
        "skills": {
            "hard_skills": ["Python", "Git"],
            "soft_skills": ["Trabajo en equipo"]
        },
        "languages": [
            {
                "language": "Inglés",
                "level": "B2"
            }
        ]
    }
    
    profile = CandidateProfile(**data)
    
    # Aserciones (verificaciones)
    assert profile.personal.full_name == "Juan Pérez"
    assert profile.professional.years_of_experience == 3.5
    assert len(profile.experience) == 1
    assert profile.experience[0].company == "Tech Solutions"
    assert "Python" in profile.skills.hard_skills
    assert profile.languages[0].language == "Inglés"


def test_candidate_profile_fallback_with_empty_or_null_data():
    """Verifica la política de extracción pura (ADR 0005): nulos y vacíos no rompen el modelo."""
    # Le pasamos un diccionario completamente vacío
    profile = CandidateProfile()
    
    # Debe instanciar los submodelos con sus valores por defecto o None
    assert profile.personal.full_name is None
    assert profile.personal.email is None
    assert profile.professional.target_roles == []
    assert profile.professional.years_of_experience is None
    assert profile.experience == []
    assert profile.skills.hard_skills == []
    assert profile.languages == []


def test_candidate_profile_validation_error_on_invalid_types():
    """Verifica que el escudo de Pydantic salte ante tipos de datos incompatibles."""
    invalid_data = {
        "professional": {
            # years_of_experience debería ser un número (float/int), no un texto descriptivo
            "years_of_experience": "Muchos años de experiencia"
        }
    }
    
    # Esperamos que Pydantic lance mandatoriamente una excepción ValidationError
    with pytest.raises(ValidationError):
        CandidateProfile(**invalid_data)