from pathlib import Path

import fitz

from .interfaces import DocumentExtractor


class PDFExtractor(DocumentExtractor):

    def extract_text(self, file_path: Path) -> str:

        text = []

        with fitz.open(file_path) as pdf:
            for page in pdf:
                text.append(page.get_text())

        return "\n".join(text)