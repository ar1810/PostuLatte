# Roadmap de Desarrollo de PostuLatte

Este documento describe la evolución prevista del proyecto y el estado de cada sprint hasta la versión 1.0.

---

# Estado actual

Versión objetivo: **v1.0**
Sprint actual: **Sprint 6 - Dominio de ofertas y Tailoring Engine**

Estado del proyecto:
- [x] Arquitectura base consolidada
- [x] Configuración centralizada mediante YAML y Pydantic
- [x] Integración e interfaz de desacoplamiento con Ollama
- [x] Extracción unificada de documentos (PDF/DOCX) con Factory
- [x] Pipeline e ingesta cognitiva de CV hacia `CandidateProfile` con la suite de pruebas en verde

---

# Roadmap

| Sprint | Estado | Objetivo |
| :--- | :---: | :--- |
| Sprint 1 | [x] | Arquitectura base |
| Sprint 2 | [x] | Sistema de configuración |
| Sprint 3 | [x] | Integración con Ollama |
| Sprint 4 | [x] | Extracción de documentos |
| Sprint 5 | [x] | Pipeline CV -> CandidateProfile |
| Sprint 6 | [ ] | Dominio de ofertas y Tailoring Engine |
| Sprint 7 | [ ] | Motor de Compatibilidad ATS |
| Sprint 8 | [ ] | Generador de CV |
| Sprint 9 | [ ] | Generador de cartas |
| Sprint 10 | [ ] | CLI completa |
| Sprint 11 | [ ] | Interfaz gráfica |
| Sprint 12 | [ ] | Release v1.0 |

> **Nota:** Los sprints representan hitos funcionales de alto nivel. La implementación interna puede reorganizarse cuando una decisión arquitectónica mejore la escalabilidad del proyecto, siempre que se mantengan la visión, la filosofía y los objetivos funcionales definidos en este roadmap.
---

# Objetivos de cada Sprint

## Sprint 1 - Arquitectura base [x]
- Definición de la arquitectura del proyecto.
- Organización del repositorio y configuración inicial de Git.
- Documentación base y ADR iniciales (0001, 0002).

## Sprint 2 - Configuración [x]
- Sistema de configuración basado en YAML.
- Validación estricta mediante Pydantic.
- Carga centralizada de configuraciones del sistema.

## Sprint 3 - Integración Ollama [x]
- Cliente base para Ollama local.
- Abstracción inicial del proveedor LLM.

## Sprint 4 - Extracción de documentos [x]
- Lectura y parsing de archivos PDF y DOCX.
- API unificada de extracción mediante `ExtractorFactory`.
- Cobertura de pruebas unitarias sobre archivos de prueba.

## Sprint 5 - Pipeline CV -> CandidateProfile [x]
- Definición completa del modelo `CandidateProfile` en 5 dimensiones.
- Diseño e implementación de `PromptBuilder` con política estricta de contenedores vacíos y cero alucinación (ADR 0005).
- Estabilización de `OllamaAIService` forzando modo JSON nativo y temperatura 0.0.
- Implementación del orquestador `ProfileExtractionPipeline` en la capa Core.
- **Suite de pruebas:** 12 tests ejecutados exitosamente (`12 passed`).

> **Nota de Arquitectura (Sprint 5 - Consolidada):**
> Durante este sprint se decidió posponer deliberadamente el modelado del dominio de ofertas y del motor de adaptación para evitar acoplamientos prematuros con la ingesta de vacantes. Dichas entidades (`JobDescription` y `AdaptationResult`) se implementarán al inicio del Sprint 6, manteniendo la estabilidad de la arquitectura y de la suite de pruebas.

## Sprint 6 - Dominio de ofertas y Tailoring Engine [ ]
Objetivos:
- Diseñar el modelo de dominio `JobDescription`.
- Implementar la entidad `JobDescription`.
- Diseñar e implementar el modelo `JobAnalysis` como resultado estructurado del análisis entre un candidato y una oferta laboral.
- Implementar las entidades de dominio siguiendo los principios establecidos para `CandidateProfile`.
- Definir la arquitectura base del Tailoring Engine y su integración con el dominio.
- Incorporar pruebas unitarias para las nuevas entidades del dominio.
- Mantener la suite de pruebas completamente en verde.

> **Nota de Arquitectura:**
Durante este sprint se consolidará el lenguaje ubicuo del dominio relacionado con las ofertas laborales. El objetivo es establecer un modelo independiente de cualquier fuente de datos (scraping, APIs o importación manual), permitiendo que las futuras integraciones operen exclusivamente sobre entidades del dominio.
---

*El contenido de los próximos sprints podrá ajustarse conforme evolucione el dominio del proyecto. Este roadmap refleja la planificación actual y prioriza la consolidación del dominio antes de incorporar nuevas integraciones, automatizaciones o interfaces de usuario.*