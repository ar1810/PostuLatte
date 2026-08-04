import json
from pathlib import Path
from unittest.mock import MagicMock
import pytest

from src.domain.entities.analysis import JobAnalysis
from src.domain.entities.candidate import CandidateProfile, PersonalInfo, SkillsInfo
from src.domain.entities.job import JobDescription
from src.workflow.analyze_job import JobAnalyzerWorkflow


@pytest.fixture
def mock_ai_service():
    """Mock del servicio de IA para simular la respuesta de matching en el test de integración."""
    service = MagicMock()
    service.generate_structured.return_value = JobAnalysis(
        match_percentage=90,
        matching_skills=["Python", "SQL", "Git"],
        missing_skills=["FastAPI"],
        key_strengths=["Experiencia sólida en desarrollo backend con Python"],
        improvement_suggestions=["Añadir frameworks modernos como FastAPI al perfil"]
    )
    return service


@pytest.fixture
def sample_job_description():
    """Carga una oferta real desde las fixtures del proyecto."""
    fixture_path = Path("tests/fixtures/jobs/python_developer_job.json")
    with open(fixture_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return JobDescription(**data)


@pytest.fixture
def sample_candidate_profile():
    """Simula un perfil extraído previamente de simple_resume.pdf."""
    return CandidateProfile(
        personal=PersonalInfo(full_name="Candidato Test"),
        summary="Desarrollador con experiencia en Python y bases de datos.",
        skills=SkillsInfo(
            hard_skills=["Python", "SQL", "Git"],
            soft_skills=["Resolución de problemas"]
        )
    )


def test_integration_analyze_job_workflow(mock_ai_service, sample_candidate_profile, sample_job_description):
    """Prueba la integración del workflow usando fixtures reales de ofertas y perfiles."""
    workflow = JobAnalyzerWorkflow(ai_service=mock_ai_service)

    result = workflow.run(
        candidate=sample_candidate_profile,
        job=sample_job_description
    )

    # Validaciones del resultado del análisis de integración
    assert isinstance(result, JobAnalysis)
    assert result.match_percentage == 90
    assert "Python" in result.matching_skills
    assert sample_job_description.title != ""
    mock_ai_service.generate_structured.assert_called_once()