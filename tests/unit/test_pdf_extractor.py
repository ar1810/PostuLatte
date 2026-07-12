from pathlib import Path

from src.extraction.pdf_extractor import PDFExtractor


def test_extract_text_from_pdf():

    extractor = PDFExtractor()

    pdf = Path("tests/fixtures/pdf/simple_resume.pdf")

    text = extractor.extract_text(pdf)

    assert isinstance(text, str)
    assert len(text) > 0