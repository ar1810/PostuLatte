# Roadmap de Desarrollo de PostuLatte

Este documento describe la evolución prevista del proyecto y el estado de cada sprint hasta la versión 1.0.

---

# Estado actual

Versión objetivo: **v1.0**
Sprint actual: **Sprint 7 - Generación de documentación personalizada**

Estado del proyecto:
- [x] Arquitectura base consolidada
- [x] Configuración centralizada mediante YAML y Pydantic
- [x] Integración e interfaz de desacoplamiento con Ollama
- [x] Extracción unificada de documentos (PDF/DOCX) con Factory
- [x] Pipeline de construcción de `CandidateProfile`
- [x] Dominio modular (`CandidateProfile`, `JobDescription`, `JobAnalysis`)
- [x] Tailoring Engine para análisis estructurado de ofertas
- [x] CLI con comandos `extract-cv` y `analyze-job`
- [x] Suite de pruebas completamente en verde (17 tests)

---

# Roadmap

| Sprint | Estado | Objetivo |
| :--- | :---: | :--- |
| Sprint 1 | [x] | Arquitectura base |
| Sprint 2 | [x] | Sistema de configuración |
| Sprint 3 | [x] | Integración con Ollama |
| Sprint 4 | [x] | Extracción de documentos |
| Sprint 5 | [x] | Pipeline CV -> CandidateProfile |
| Sprint 6 | [x] | Dominio de ofertas y Tailoring Engine |
| Sprint 7 | [ ] | Generación de documentación personalizada |
| Sprint 8 | [ ] | Motor de búsqueda de ofertas |
| Sprint 9 | [ ] | Historial de postulaciones |
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
- **Suite de pruebas:** Consolidada y ampliada durante los siguientes sprints.

> **Nota de Arquitectura (Sprint 5 - Consolidada):**

## Sprint 6 - Dominio de ofertas y Tailoring Engine [x]
Objetivos alcanzados:
- Diseño e implementación de `JobDescription`.
- Diseño e implementación de `JobAnalysis`.
- Separación del dominio en módulos independientes.
- Implementación del Tailoring Engine.
- Integración del análisis estructurado mediante IA local.
- Incorporación del workflow `analyze-job`.
- Integración de los comandos CLI `extract-cv` y `analyze-job`.
- Consolidación del dominio siguiendo los principios definidos en el ADR 0007.
- Suite completa de pruebas en verde (17 tests).

> **Resultado del Sprint 6:**
> Se consolidó el modelo de dominio para el análisis de ofertas laborales. A partir de este punto, tanto el perfil profesional como las ofertas son representados mediante entidades del dominio (`CandidateProfile` y `JobDescription`), permitiendo que el Tailoring Engine produzca un `JobAnalysis` completamente desacoplado de las fuentes originales de datos.

## Sprint 7 - Generación de documentación personalizada [ ]

Objetivos:

- Diseñar el workflow de generación documental.
- Implementar el generador de cartas de presentación.
- Definir la arquitectura para futuros generadores de CV adaptados.
- Diseñar el modelo de excepciones del dominio.
- Mantener la cobertura de pruebas completamente en verde.

---

*El contenido de los próximos sprints podrá ajustarse conforme evolucione el dominio del proyecto. Este roadmap refleja la planificación actual y prioriza la consolidación del dominio antes de incorporar nuevas integraciones, automatizaciones o interfaces de usuario.*