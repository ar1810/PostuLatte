# src/core/application.py
import logging
from pathlib import Path
from src.domain.entities import CandidateProfile
from src.domain.interfaces import AIService
from src.extraction.factory import ExtractorFactory

class ProfileExtractionPipeline:
    """Orquestador central del sistema.
    Coordina la extracción de texto físico y el procesamiento cognitivo vía LLM.
    """
    
    def __init__(self, ai_service: AIService) -> None:
        self.logger = logging.getLogger(__name__)
        self.ai_service = ai_service

    def execute(self, file_path: str | Path) -> CandidateProfile:
        """Transforma un archivo físico de CV en una entidad CandidateProfile

        completamente tipada y validada por el dominio.
        """
        path = Path(file_path)
        self.logger.info(f"Iniciando procesamiento del archivo: {path.name}")

        # Step 1: Obtener el extractor adecuado según la extensión (.pdf, .docx)
        try:
            extractor = ExtractorFactory.get_extractor(path)
        except ValueError as e:
            self.logger.error(f"Formato de archivo no soportado: {path.suffix}")
            raise

        # Step 2: Extraer el texto crudo del documento
        self.logger.info(f"Extrayendo texto bruto con {extractor.__class__.__name__}")
        raw_text = extractor.extract(path)
        
        if not raw_text.strip():
            self.logger.warning(f"El archivo {path.name} se leyó vacío o sin caracteres procesables.")

        # Step 3: Enviar el texto plano al motor de IA (Ollama)
        self.logger.info("Enviando texto extraído al servicio de IA")
        profile_data = self.ai_service.extract_profile(raw_text)

        # Step 4: Construir y validar el modelo central del dominio
        self.logger.info("Mapeando y validando diccionario de salida en CandidateProfile")
        candidate_profile = CandidateProfile(**profile_data)

        return candidate_profile