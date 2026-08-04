from unittest.mock import MagicMock
import pytest

from src.domain.entities.analysis import JobAnalysis
from src.domain.entities.candidate import CandidateProfile, PersonalInfo, SkillsInfo
from src.domain.entities.job import JobDescription
from src.workflow.analyze_job import JobAnalyzerWorkflow


@pytest.fixture
def mock_ai_service():
    """Mock del servicio de IA que retorna una instancia válida de JobAnalysis."""
    service = MagicMock()
    service.generate_structured.return_value = JobAnalysis(
        match_percentage=85,
        matching_skills=["Python", "FastAPI", "PostgreSQL"],
        missing_skills=["Docker", "Kubernetes"],
        key_strengths=["5 años de experiencia en backend", "Sólidos conocimientos en Python"],
        improvement_suggestions=["Destacar proyectos con contenedores o CI/CD si los tenés"]
    )
    return service


@pytest.fixture
def dummy_candidate_profile():
    return CandidateProfile(
        personal=PersonalInfo(full_name="Diego Silva"),
        summary="Backend Developer especializado en Python.",
        skills=SkillsInfo(
            hard_skills=["Python", "FastAPI", "PostgreSQL", "Git"],
            soft_skills=["Trabajo en equipo"]
        )
    )


@pytest.fixture
def dummy_job_description():
    return JobDescription(
        title="Senior Python Developer",
        company="TechCorp",
        required_skills=["Python", "FastAPI", "PostgreSQL", "Docker", "Kubernetes"],
        desired_skills=["AWS", "Redis"],
        raw_text="Buscamos desarrollador backend senior con experiencia en Python y Docker."
    )


def test_analyze_job_success(mock_ai_service, dummy_candidate_profile, dummy_job_description):
    """Verifica que el workflow ejecute el análisis correctamente y devuelva un JobAnalysis."""
    workflow = JobAnalyzerWorkflow(ai_service=mock_ai_service)

    result = workflow.run(
        candidate=dummy_candidate_profile,
        job=dummy_job_description
    )

    # Validaciones
    assert isinstance(result, JobAnalysis)
    assert result.match_percentage == 85
    assert "Python" in result.matching_skills
    assert "Docker" in result.missing_skills
    assert len(result.key_strengths) > 0
    assert len(result.improvement_suggestions) > 0

    # Verificar que el servicio de IA haya sido invocado con el schema correcto
    mock_ai_service.generate_structured.assert_called_once()
    _, kwargs = mock_ai_service.generate_structured.call_args
    assert kwargs.get("response_schema") == JobAnalysis