# Arquitectura del Sistema

Este documento describe la arquitectura de PostuLatte, las responsabilidades de cada capa y el flujo general de información dentro de la aplicación.

El proyecto sigue los principios de **Arquitectura Limpia (Clean Architecture)** y **Diseño Guiado por el Dominio (DDD)**.

---

# Principios arquitectónicos

La arquitectura se basa en cuatro principios fundamentales:
- El dominio contiene únicamente reglas de negocio puras.
- La infraestructura implementa servicios externos sin contaminar el dominio.
- La capa de aplicación/core orquesta los casos de uso utilizando el dominio.
- Las dependencias siempre apuntan hacia adentro (hacia el dominio).

---

# Arquitectura en capas

CLI / GUI
│
▼
src/core (Application)
│
▼
src/domain (Entities / Interfaces)
▲
│
src/infrastructure (AI / Extraction / Config)

* Las capas externas pueden depender de las internas.
* Las capas internas nunca conocen detalles de implementación de las capas externas.

---

# Responsabilidades de Componentes Clave

## src/domain
Representa el corazón inmutable de PostuLatte.
- **`entities.py`:** Contiene los modelos base (`CandidateProfile`, `PersonalInfo`, `SkillsInventory`, etc.) validados rígidamente mediante Pydantic V2.
- **`interfaces.py`:** Define los contratos y abstracciones puras (`AIService`) que el dominio exige para operar, completamente desacoplado de proveedores específicos.

## src/core (Application)
- **`application.py` (`ProfileExtractionPipeline`):** Actúa como el orquestador de casos de uso. Coordina la fábrica de extracción física para obtener texto de los archivos, despacha el procesamiento semántico a la infraestructura de IA inyectada y retorna el perfil de dominio construido.

## src/infrastructure
Implementa la comunicación directa con tecnologías de terceros y el sistema operativo.
- **`src/extraction/`:** Aloja los lectores físicos independientes (`PDFExtractor`, `DocxExtractor`) junto a su `ExtractorFactory`.
- **`src/ai/`:** Contiene el cliente específico de infraestructura `OllamaAIService` que interactúa con la API de Ollama (forzando `format="json"` y `temperature=0.0`) y el `PromptBuilder` que formatea las directivas rígidas del sistema.

---

# Flujo Principal de Ingesta (Sprint 5)

El flujo secuencial de la información se ejecuta de la siguiente manera de principio a fin:

[Archivo Físico .pdf/.docx]
│
▼ (ExtractorFactory)
[Texto Bruto Extraído]
│
▼ (PromptBuilder + AIService)
[JSON Estructurado desde Ollama]
│
▼ (Pydantic Validation)
[CandidateProfile (Entidad de Dominio)]

Una vez generado el `CandidateProfile`, el documento original deja de ser necesario para el funcionamiento del sistema. Todas las capacidades posteriores (búsqueda, matching, generación) operan de manera exclusiva sobre este modelo unificado del dominio.