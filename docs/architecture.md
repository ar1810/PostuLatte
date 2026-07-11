# Arquitectura del Sistema

Este documento describe la estructura arquitectónica, el flujo de datos y los principios de diseño de la aplicación. El sistema está diseñado bajo los principios de **Arquitectura Limpia (Clean Architecture)** y **Diseño Guiado por el Dominio (DDD)**.

---

## 🏛️ Vista General de las Capas

El código fuente dentro de `src/` se organiza en capas concéntricas. La regla fundamental es que **las capas externas pueden depender de las internas, pero las internas NUNCA deben conocer nada de las externas**.

[ Capa Externa: CLI / run.py ]
             │
             ▼
[ Capa de Automatización y Flujos ] ──► src/workflow/ (analyze_job.py, etc.)
             │
             ▼
[ Capa de Núcleo y Utilidades ]     ──► src/core/ y src/utils/
             │
             ▼
[ Capa del Dominio (Core Puro) ]    ──► src/domain/ (Modelos e Interfaces)

---

## 📂 Responsabilidades por Carpeta

### 1. Dominio (`src/domain/`)
Es el corazón de la aplicación. Contiene las reglas de negocio puras. No tiene dependencias de librerías externas de IA o frameworks de scraping.
*   **Modelos/Entidades:** Clases puras de Python que representan los conceptos del negocio (ej: `JobOffer`, `CandidateProfile`, `MatchResult`).
*   **Interfaces (Contratos):** Clases abstractas (`ABC`) que definen qué acciones se pueden hacer pero sin decir cómo (ej: `class AIService(ABC)`, `class JobFinderService(ABC)`).

### 2. Flujos de Trabajo (`src/workflow/`)
Representa los **Casos de Uso** de la aplicación. Orquesta la lógica del negocio interactuando con las interfaces del dominio para automatizar las tareas.
*   `analyze_job.py`: Orquesta la búsqueda automática de ofertas, la ingesta de datos y el análisis de compatibilidad (Matching).
*   `generate_resume.py` y `generate_cover_letter.py`: Adaptan el perfil a las ofertas seleccionadas.
*   `prepare_interview.py`: Genera guías de preparación basadas en la oferta elegida.

### 3. Inteligencia Artificial (`src/ai/`)
Contiene las implementaciones técnicas y adaptadores del mundo exterior para los Modelos de Lenguaje (LLMs). Aquí se traduce la lógica del negocio a llamadas de API (OpenAI, Anthropic, etc.).

### 4. Núcleo (`src/core/`)
Funcionalidades transversales necesarias para que la aplicación arranque y funcione de manera estable.
*   `config.py`: Carga y validación estricta de archivos YAML (`settings.yaml`, `providers.yaml`, `logging.yaml`).
*   `exceptions.py`: Centralización de errores personalizados del sistema.
*   `application.py`: Inicializador del contexto de la aplicación.

---

## 🔄 Flujo de Datos Típico (Búsqueda y Filtrado Automático)

1. El usuario ejecuta la aplicación desde la raíz mediante `python run.py`.
2. El **`src/cli/`** captura los parámetros y dispara el flujo `AnalyzeJobWorkflow`.
3. El workflow toma el perfil del usuario desde `data/profiles/example_profile.yaml`.
4. El sistema busca de forma automatizada nuevas propuestas en los portales configurados.
5. Las ofertas encontradas se convierten en entidades del dominio (`JobOffer`).
6. El workflow pasa el perfil del usuario y las ofertas al módulo de IA (`src/ai/`) para realizar un análisis de compatibilidad (Matching Score) basado en las palabras clave del ATS (`data/knowledge/ats_keywords.md`).
7. Las propuestas con mayor compatibilidad se almacenan en `data/output/` y quedan listas para la fase de postulación o generación de CV/carta de presentación.