# tests/integration/test_integration_extraction.py
from pathlib import Path
import pytest
from src.extraction.factory import ExtractorFactory
from src.ai.ollama_client import OllamaAIService
from src.domain.entities import CandidateProfile

@pytest.mark.integration
def test_full_extraction_pipeline_with_fixture():
    """Valida la extracción de datos de un CV anónimo de prueba en PDF usando el paquete src.extraction."""
    
    fixture_path = Path("tests/fixtures/pdf/simple_resume.pdf")
    assert fixture_path.exists(), f"❌ No se encontró el fixture en {fixture_path.resolve()}"
    
    print(f"\n📄 Probando extracción con el fixture anónimo: {fixture_path.name}...")

    # 1. Extracción de texto usando src.extraction.factory
    extractor = ExtractorFactory.get_extractor(fixture_path)
    raw_text = extractor.extract_text(fixture_path)

    assert len(raw_text) > 0, "❌ El texto extraído está vacío"

    # 2. Invocación al servicio de IA local desde src.ai.ollama_client
    service = OllamaAIService()
    profile_dict = service.extract_profile(raw_text)

    # 3. Validación con el Modelo de Dominio
    profile = CandidateProfile(**profile_dict)

    assert profile is not None
    assert isinstance(profile, CandidateProfile)