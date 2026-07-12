from typing import List, Optional
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Submodelos del Perfil
# ---------------------------------------------------------------------------

class PersonalInfo(BaseModel):
    """Información básica e identidad del candidato."""
    full_name: Optional[str] = Field(None, description="Nombre y apellido completo")
    email: Optional[str] = Field(None, description="Correo electrónico de contacto")
    phone: Optional[str] = Field(None, description="Número de teléfono con código de área")
    location: Optional[str] = Field(None, description="Ciudad, provincia/estado y país")
    linkedin: Optional[str] = Field(None, description="URL del perfil de LinkedIn")
    website: Optional[str] = Field(None, description="URL de portfolio, GitHub o sitio web personal")


class ProfessionalFocus(BaseModel):
    """Posicionamiento actual del candidato en el mercado."""
    target_roles: List[str] = Field(default_factory=list, description="Roles o puestos a los que aspira")
    years_of_experience: Optional[float] = Field(None, description="Años estimados de experiencia total")


class ExperienceHito(BaseModel):
    """Un hito o puesto específico en el historial laboral."""
    company: Optional[str] = Field(None, description="Nombre de la empresa u organización")
    role: Optional[str] = Field(None, description="Puesto o cargo desempeñado")
    period_from: Optional[str] = Field(None, description="Fecha de inicio (ej: '2022-03' o 'Marzo 2022')")
    period_to: Optional[str] = Field(None, description="Fecha de finalización o 'Actualidad'")
    description: Optional[str] = Field(None, description="Responsabilidades, logros y tecnologías usadas")


class SkillsInventory(BaseModel):
    """Inventario de habilidades segregado."""
    hard_skills: List[str] = Field(default_factory=list, description="Habilidades técnicas, lenguajes, herramientas")
    soft_skills: List[str] = Field(default_factory=list, description="Habilidades blandas o interpersonales")


class LanguageCompetence(BaseModel):
    """Registro de competencias lingüísticas."""
    language: str = Field(..., description="Idioma (ej: 'Inglés')")
    level: Optional[str] = Field(None, description="Nivel declarado (ej: 'B2', 'Avanzado', 'Nativo')")

# ---------------------------------------------------------------------------
# Modelo Núcleo Central
# ---------------------------------------------------------------------------

class CandidateProfile(BaseModel):
    """El núcleo central del sistema: la fotografía limpia de la realidad del candidato."""
    personal: PersonalInfo = Field(default_factory=PersonalInfo)
    professional: ProfessionalFocus = Field(default_factory=ProfessionalFocus)
    experience: List[ExperienceHito] = Field(default_factory=list)
    skills: SkillsInventory = Field(default_factory=SkillsInventory)
    languages: List[LanguageCompetence] = Field(default_factory=list)