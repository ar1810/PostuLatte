from pathlib import Path

from docx import Document

from .interfaces import DocumentExtractor


class DOCXExtractor(DocumentExtractor):

    def extract_text(self, file_path: Path) -> str:

        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)