from pathlib import Path

from src.extraction.docx_extractor import DOCXExtractor


def test_extract_text_from_docx():

    extractor = DOCXExtractor()

    docx = Path("tests/fixtures/docx/simple_resume.docx")

    text = extractor.extract_text(docx)

    assert isinstance(text, str)
    assert len(text) > 0