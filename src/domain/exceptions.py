# src/domain/exceptions.py
"""Excepciones base y específicas del dominio de PostuLatte."""


class PostuLatteException(Exception):
    """Excepción base para todos los errores del sistema PostuLatte."""

    pass


class DomainError(PostuLatteException):
    """Excepción base para violaciones de reglas de negocio o inconsistencias en el dominio."""

    pass


class DomainValidationError(DomainError):
    """Se lanza cuando los datos de una entidad no superan las validaciones de negocio."""

    pass


class ExtractionError(PostuLatteException):
    """Se lanza cuando ocurre un fallo durante la ingesta o lectura física de documentos (PDF/DOCX)."""

    pass


class LLMProviderError(PostuLatteException):
    """Se lanza cuando la comunicación con el proveedor de IA (Ollama, etc.) falla."""

    pass


class LLMResponseValidationError(LLMProviderError):
    """Se lanza cuando la respuesta JSON de la IA no se ajusta al esquema esperado."""

    pass