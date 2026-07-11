# src/domain/entities.py
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

@dataclass
class CandidateProfile:
    """Representa el perfil profesional consolidado del usuario."""
    full_name: str
    email: str
    location: str
    target_roles: List[str]
    skills: List[str]
    experience_years: float
    experience_summary: str
    education: List[Dict[str, Any]] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)
    raw_resume_text: str = ""

@dataclass
class JobOffer:
    """Representa una oferta de trabajo encontrada en internet."""
    id: str
    title: str
    company: str
    location: str
    description: str
    source_portal: str
    url: str
    extracted_keywords: List[str] = field(default_factory=list)
    found_at: datetime = field(default_factory=datetime.now)

@dataclass
class MatchResult:
    """Representa el veredicto de compatibilidad hecho por la IA."""
    job_id: str
    score: int
    matching_skills: List[str]
    missing_skills: List[str]
    justification: str
    is_approved: bool = False