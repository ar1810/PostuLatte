from abc import ABC, abstractmethod
from pathlib import Path


class DocumentExtractor(ABC):
    """
    Interfaz base para todos los extractores de documentos.
    """

    @abstractmethod
    def extract_text(self, file_path: Path) -> str:
        """
        Extrae el texto de un documento.
        """
        raise NotImplementedError