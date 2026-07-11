# src/domain/interfaces.py
from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import CandidateProfile, JobOffer, MatchResult

class AIService(ABC):
    """Interfaz obligatoria para cualquier proveedor de IA (Ollama, OpenAI, Claude)."""
    
    @abstractmethod
    def analyze_compatibility(self, profile: CandidateProfile, job: JobOffer) -> MatchResult:
        pass

    @abstractmethod
    def extract_keywords(self, text: str) -> List[str]:
        pass

class JobFinderService(ABC):
    """Interfaz obligatoria para los componentes que busquen ofertas en portales."""
    
    @abstractmethod
    def search_offers(self, target_roles: List[str], location: Optional[str] = None) -> List[JobOffer]:
        pass