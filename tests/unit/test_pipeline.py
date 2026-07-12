# tests/unit/test_pipeline.py
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from src.core.application import ProfileExtractionPipeline
from src.domain.interfaces import AIService
from src.domain.entities import CandidateProfile

def test_pipeline_execute_flow_success():
    """Verifica la correcta orquestación del pipeline aislando la fábrica

    de extractores y las llamadas externas de la IA.
    """
    # 1. Configurar Mocks de las fronteras externas
    mock_ai_service = MagicMock(spec=AIService)
    mock_ai_service.extract_profile.return_value = {
        "personal": {"full_name": "Marta Gómez", "email": "marta@example.com"},
        "professional": {"target_roles": ["Data Scientist"]},
        "skills": {"hard_skills": ["Python", "SQL"]}
    }

    mock_extractor = MagicMock()
    mock_extractor.extract.return_value = "Texto extraído del CV de Marta"

    # 2. Instanciar el pipeline inyectando el servicio mockeado
    pipeline = ProfileExtractionPipeline(ai_service=mock_ai_service)

    # 3. Interceptamos el método estático de ExtractorFactory usando la ruta real
    with patch("src.extraction.factory.ExtractorFactory.get_extractor") as mock_factory:
        mock_factory.return_value = mock_extractor

        # 4. Ejecutar el pipeline con un path ficticio
        fake_path = Path("CV_Marta.pdf")
        profile = pipeline.execute(fake_path)

        # 5. Aserciones de comportamiento y validaciones del dominio
        mock_factory.assert_called_once_with(fake_path)
        mock_extractor.extract.assert_called_once_with(fake_path)
        mock_ai_service.extract_profile.assert_called_once_with("Texto extraído del CV de Marta")

        # Verificar integridad del objeto final
        assert isinstance(profile, CandidateProfile)
        assert profile.personal.full_name == "Marta Gómez"
        assert profile.skills.hard_skills == ["Python", "SQL"]