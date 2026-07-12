from pathlib import Path

from .docx_extractor import DOCXExtractor
from .exceptions import UnsupportedDocumentError
from .interfaces import DocumentExtractor
from .pdf_extractor import PDFExtractor


class ExtractorFactory:

    _extractors = {
        ".pdf": PDFExtractor,
        ".docx": DOCXExtractor,
    }

    @classmethod
    def get_extractor(cls, file_path: Path) -> DocumentExtractor:

        extension = file_path.suffix.lower()

        extractor = cls._extractors.get(extension)

        if extractor is None:
            raise UnsupportedDocumentError(
                f"Formato de archivo no soportado: {extension}"
            )

        return extractor()