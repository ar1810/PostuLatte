# src/core/config.py
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
from pydantic import BaseModel, Field

# 📍 Configuración de rutas base dinámicas
CORE_DIR = Path(__file__).resolve().parent      # src/core
SRC_DIR = CORE_DIR.parent                       # src
ROOT_DIR = SRC_DIR.parent                       # Raíz del proyecto
CONFIG_DIR = ROOT_DIR / "config"

# 📑 Modelos de validación con Pydantic v2
class ProviderConfig(BaseModel):
    """Mapea y valida la configuración de un proveedor de IA."""
    api_key_env: str
    model: str
    base_url: Optional[str] = None
    temperature: float = Field(0.2, ge=0.0, le=2.0)
    max_tokens: int = Field(2000, gt=0)

class SearchSettings(BaseModel):
    """Configuración para el agente de búsqueda automatizada."""
    min_match_score: int = Field(70, ge=0, le=100)
    max_results_per_search: int = Field(20, gt=0)
    search_frequency_hours: int = Field(24, gt=0)

class Settings(BaseModel):
    """Contenedor global validado de la aplicación."""
    app_name: str = "AI Job Hunter Agent"
    version: str = "0.1.0"
    environment: str = "development"
    default_provider: str = "ollama"
    
    search: SearchSettings = Field(default_factory=SearchSettings)
    providers: Dict[str, ProviderConfig] = Field(default_factory=dict)

    @property
    def active_ai(self) -> ProviderConfig:
        """Devuelve la configuración del proveedor activo por defecto."""
        return self.providers[self.default_provider]

# 🔄 Funciones de carga
def _load_yaml_file(file_path: Path) -> Dict[str, Any]:
    if not file_path.exists():
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"⚠️ Error al leer {file_path.name}: {e}")
        return {}

def load_settings() -> Settings:
    settings_raw = _load_yaml_file(CONFIG_DIR / "settings.yaml")
    providers_raw = _load_yaml_file(CONFIG_DIR / "providers.yaml")
    
    combined_data = {**settings_raw}
    if "providers" in providers_raw:
        combined_data["providers"] = providers_raw["providers"]
    else:
        # Por si el archivo tiene los proveedores directo en la raíz
        combined_data["providers"] = {k: v for k, v in providers_raw.items() if k != "default_provider"}
        if "default_provider" in providers_raw:
            combined_data["default_provider"] = providers_raw["default_provider"]

    return Settings(**combined_data)

# Instancia global lista para usar
config = load_settings()

if __name__ == "__main__":
    print("--- 🛠️ Test de Carga de Configuración ---")
    print(f"Raíz detectada: {ROOT_DIR}")
    print(f"IA Activa por defecto: {config.default_provider} ({config.active_ai.model})")