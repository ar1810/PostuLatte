# src/domain/entities/job.py
from pydantic import BaseModel, Field


class JobDescription(BaseModel):
    """Representa la oferta laboral objetivo normalizada, independientemente de su origen."""

    title: str = Field(..., description="Título o rol principal de la oferta")
    company: str = Field(default="", description="Nombre de la empresa o consultora")
    experience_years: int | None = Field(
        default=None, description="Años de experiencia solicitados"
    )
    required_skills: list[str] = Field(
        default_factory=list, description="Habilidades o requisitos indispensables"
    )
    desired_skills: list[str] = Field(
        default_factory=list, description="Habilidades o conocimientos deseables"
    )
    responsibilities: list[str] = Field(
        default_factory=list, description="Responsabilidades o tareas del puesto"
    )
    raw_text: str = Field(
        default="", description="Texto bruto u original de la vacante"
    )