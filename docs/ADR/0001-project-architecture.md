# ADR 0001: Estructura del Proyecto basada en Arquitectura Limpia y DDD

## Estado
Aceptado

## Contexto
El proyecto es una herramienta de automatización y optimización de postulación laboral asistida por IA. Al interactuar con múltiples servicios externos (modelos de lenguaje, parsing de PDFs, almacenamiento local, etc.), corremos el riesgo de crear un código acoplado (código "espagueti") donde los cambios en la API de un proveedor de IA o en el formato de los datos rompan la lógica central del negocio.

Necesitamos una arquitectura para:
1. Aislar la lógica de negocio (analizar ofertas, adaptar CVs) de los detalles técnicos (bases de datos, frameworks, APIs de LLMs).
2. Facilitar las pruebas unitarias sin necesidad de levantar servicios reales.
3. Permitir el crecimiento modular del proyecto (ej. migrar de una CLI a una interfaz web o API en el futuro sin reescribir todo).

## Decisión
Se adopta una estructura de directorios inspirada en **(Arquitectura Limpia)** y **Diseño Guiado por el Dominio (DDD)**, organizada de la siguiente manera:

*   `src/domain/`: El corazón del proyecto. Contiene las entidades puras de negocio (`JobOffer`, `CandidateProfile`) e interfaces abstractas. No tiene dependencias externas.
*   `src/workflow/`: Capa de Automatización y Flujos. Orquesta los casos de uso (`analyze_job.py`, `generate_resume.py`). Aquí reside la lógica de qué pasa, cuándo se busca y cómo se cruzan los datos.
*   `src/ai/`: Capa externa de Inteligencia Artificial. Implementaciones concretas de los conectores con los modelos de lenguaje (OpenAI, Anthropic, etc.).
*   `src/core/`: Funcionalidades transversales a la aplicación (gestión de configuración global, excepciones personalizadas, inicialización).
*   `src/cli/` y `run.py`: Puntos de entrada de la aplicación (interfaces de usuario y disparadores).
*   `data/`: Almacenamiento local desacoplado, dividido estrictamente por su ciclo de vida (`knowledge` para RAG/ATS, `storage` para persistencia local, `output` para resultados).

### Regla de Oro de Dependencias:
Las dependencias de código solo pueden apuntar **hacia adentro**. El `domain` no sabe que existe el `workflow`. El `workflow` no sabe qué proveedor de IA específico o base de datos se está usando en `services`. Todo se comunica mediante inversión de dependencias e interfaces.

## Consecuencias
*   **Positivas:** El proyecto es altamente testeable y agnóstico a las herramientas. Podemos cambiar de SQLite a PostgreSQL, o de OpenAI a un modelo local en Ollama, modificando únicamente la capa de `services` o configuración, sin tocar los flujos core en `workflow`.
*   **Negativas:** Introduce una ligera sobrecarga inicial al requerir más archivos y abstracciones (interfaces/clases abstractas) para comunicar las capas en lugar de hacer importaciones directas.