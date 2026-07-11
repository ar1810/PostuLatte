# Roadmap del Proyecto

Prioridad Alta

? Importar PDF

? Importar DOCX

? Extraer CandidateProfile

? Revisar datos

? Guardar profile.yaml

## ?? Estado Actual
El proyecto cuenta con una arquitectura base s車lida e higienizada, dise?ada bajo principios de arquitectura limpia/DDD, lista para desarrollo local sin acoplamiento a bases de datos.

## ?? Hitos Alcanzados

### Hito 1: Cimientos y Sanitizaci車n del Entorno (Completado - Julio 2026)
*   **Estructura de Directorios:** Dise?ada e implementada la arquitectura de carpetas completa.
*   **Higiene del Repositorio:** Configuraci車n estricta de `.gitignore` para prevenir fugas de bases de datos locales (`*.db`), perfiles personales (`data/profiles/*`) y entornos virtuales.
*   **Estandarizaci車n de Entorno:** Implementaci車n de `.gitattributes` para forzar finales de l赤nea `LF` (`eol=lf`), garantizando compatibilidad multiplataforma.
*   **Documentaci車n Inicial:** Creaci車n de `architecture.md`, `roadmap.md` y los registros ADR 0001 y 0002.

---

## ?? Pr車ximos Pasos (En Desarrollo)

### Hito 2: Capa Central y Gesti車n de Configuraci車n ?
*   [ ] Definir e implementar `src/core/config.py` utilizando `PyYAML` y `Pydantic`.
*   [ ] Crear archivos de configuraci車n base (`settings.yaml`, `providers.yaml`, `logging.yaml`).
*   [ ] Configurar el sistema de logs centralizado en `config/logging.yaml`.

### Hito 3: Automatizaci車n de B迆squeda y Modelado del Dominio
*   [ ] Definir entidades en `src/domain/` (`JobOffer`, `CandidateProfile`, `MatchResult`).
*   [ ] Dise?ar e implementar la l車gica de extracci車n/b迆squeda autom芍tica de ofertas dentro de `src/workflow/analyze_job.py` o utilidades.

### Hito 4: Motor de Matching e Integraci車n de IA
*   [ ] Dise?ar los prompts estructurados en `data/prompts/` para el an芍lisis de compatibilidad (Scoring de 0 a 100% frente a filtros ATS).
*   [ ] Conectar el flujo con los modelos de lenguaje en `src/ai/`.