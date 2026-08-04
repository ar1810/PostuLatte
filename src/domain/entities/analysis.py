# src/domain/entities/analysis.py
from pydantic import BaseModel, Field


class JobAnalysis(BaseModel):
    """Representa el resultado del análisis y brecha entre un CandidateProfile y un JobDescription."""

    match_percentage: int = Field(
        ..., ge=0, le=100, description="Porcentaje estimado de compatibilidad (0-100)"
    )
    matching_skills: list[str] = Field(
        default_factory=list,
        description="Habilidades coincidentes entre el candidato y la oferta",
    )
    missing_skills: list[str] = Field(
        default_factory=list,
        description="Brecha (Gap Analysis): Requisitos de la oferta no presentes en el perfil",
    )
    key_strengths: list[str] = Field(
        default_factory=list,
        description="Fortalezas principales del candidato a destacar para este rol",
    )
    improvement_suggestions: list[str] = Field(
        default_factory=list,
        description="Sugerencias concretas para adaptar el CV o postulación",
    )