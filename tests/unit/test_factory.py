from pathlib import Path

from src.extraction.factory import ExtractorFactory
from src.extraction.pdf_extractor import PDFExtractor


def test_factory_returns_pdf_extractor():

    extractor = ExtractorFactory.get_extractor(
        Path("cv.pdf")
    )

    assert isinstance(extractor, PDFExtractor)