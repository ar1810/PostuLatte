# src/ai/__init__.py
from src.ai.ollama_client import OllamaAIService

# Exportamos la clase para que se pueda importar limpiamente desde los workflows
__all__ = ["OllamaAIService"]