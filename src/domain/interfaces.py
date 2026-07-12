# src/domain/interfaces.py
from abc import ABC, abstractmethod
from src.domain.entities import CandidateProfile

class AIService(ABC):
    """Interfaz abstracta que desacopla el proveedor de IA del dominio (ADR 0006)."""

    @abstractmethod
    def extract_profile(self, raw_text: str, prompt_instructions: str) -> dict:
        """Recibe el texto bruto del CV y las instrucciones estructuradas,
        y devuelve un diccionario compatible con CandidateProfile.
        """
        pass

    # TODO: Implementar en Sprints futuros (Motor de Emparejamiento / ATS)
    # @abstractmethod
    # def match_job(self, profile: CandidateProfile, job_offer: 'JobOffer') -> 'MatchResult':
    #     pass