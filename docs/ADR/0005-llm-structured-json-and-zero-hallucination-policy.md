# ADR 0005: Formato JSON Estricto en LLM y Política de Cero Invención de Datos

## Estado
Propuesto

## Contexto
El texto bruto extraído de un currículum por el módulo de infraestructura (Sprint 4) carece de estructura. Para poblar de forma automatizada nuestro núcleo del dominio (`CandidateProfile`), requerimos que el LLM local (`llama3` a través de Ollama) interprete semánticamente el texto y lo convierta a una estructura de datos procesable por Python.

Al trabajar con modelos locales compactos, existen dos riesgos críticos:
1. Que el LLM devuelva texto conversacional ("Aquí tienes el JSON...", "Espero que te sirva") mezclado con el código, rompiendo los parsers tradicionales.
2. Que ante la ausencia de un dato (por ejemplo, que el candidato no haya puesto su número de teléfono o las fechas exactas de un empleo), el modelo "alucine" o deduzca información ficticia para intentar completar el esquema. Esto viola flagrantemente el principio de transparencia del producto.

## Decisión
Se establecen dos reglas de ingeniería de software obligatorias para el pipeline de procesamiento con IA:

1. **Forzado de Formato JSON Nativo:** Se utilizará de manera mandatoria la bandera de formato estructurado provista por la API del cliente de IA (`format="json"` en Ollama). Queda prohibido el parsing manual de texto mediante expresiones regulares basadas en bloques tipo markdown (\`\`\`json). El LLM debe escupir un string JSON puro y plano de forma nativa.
2. **Política de Extracción Pura (Null-Fallback):** Los prompts del sistema se diseñarán bajo una restricción de "cero tolerancia a la asunción". Si un campo requerido por nuestro esquema de datos no está explícitamente mencionado en el texto del currículum, el LLM tendrá la obligación contractual en su instrucción de devolver `null` o contenedores vacíos (`[]`, `{}`). 

## Consecuencias
* **Positivas:**
    * **Robustez del pipeline:** Se eliminan por completo los errores de ejecución por JSONs malformados o texto decorativo del modelo.
    * **Fidelidad absoluta:** El perfil generado será un reflejo idéntico y fidedigno del documento original del usuario, garantizando que el sistema nunca mienta en una postulación técnica.
    * **Validación predecible:** Los valores `null` mapean directamente con los campos `Optional` de nuestros modelos Pydantic V2 sin requerir lógica intermedia de limpieza.
* **Negativas:**
    * **Presión en el prompt engineering:** Exige prompts mucho más rígidos, detallados y penalizadores, lo que consume mayor ventana de contexto y requiere pruebas exhaustivas para asegurar que modelos de 8B de parámetros o menores no ignoren las restricciones.