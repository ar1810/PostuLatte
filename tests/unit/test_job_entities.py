import pytest
from pydantic import ValidationError
from src.domain.entities import JobAnalysis, JobDescription


def test_job_description_instantiation():
    job = JobDescription(
        title="Senior Python Developer",
        company="TechCorp",
        required_skills=["Python", "FastAPI", "Docker"],
        desired_skills=["Ollama", "Redis"],
    )
    assert job.title == "Senior Python Developer"
    assert len(job.required_skills) == 3
    assert "Python" in job.required_skills


def test_job_analysis_valid_percentage():
    analysis = JobAnalysis(
        match_percentage=85,
        matching_skills=["Python", "Git"],
        missing_skills=["Docker"],
        key_strengths=["Experiencia en desarrollo backend"],
        improvement_suggestions=["Mencionar proyectos personales con Docker"],
    )
    assert analysis.match_percentage == 85
    assert len(analysis.missing_skills) == 1


def test_job_analysis_invalid_percentage_raises():
    with pytest.raises(ValidationError):
        JobAnalysis(match_percentage=150)