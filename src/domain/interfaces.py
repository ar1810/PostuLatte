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


class CVExtractorService(ABC):
    """Interfaz obligatoria para los extractores técnicos de documentos (PDF, DOCX, etc.)."""
    
    @abstractmethod
    def extract_text(self, file_path: str) -> str:
        """
        Lee un archivo desde el disco y extrae su contenido de texto bruto.
        
        Args:
            file_path (str): Ruta al archivo original (ej: 'profiles/user/original/resume.pdf').
            
        Returns:
            str: El texto crudo extraído listo para ser procesado por la IA.
        """
        pass