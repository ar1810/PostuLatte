# ADR 003: Pipeline de Extracción de CV y Estructura del Dominio con Pydantic V2

## Estado
Aceptado

## Contexto
Para cumplir con la visión core de PostuLatte ("Arrastrá tu CV. Nosotros hacemos el resto"), necesitamos transformar documentos no estructurados (PDF/DOCX) en un perfil profesional altamente tipado (`CandidateProfile`). El sistema no debe obligar al usuario a rellenar formularios extensos. Además, la IA local (`llama3`) debe operar bajo restricciones estrictas de "no invención de datos" (devolviendo `null` si la información no existe).

## Decisión
1. **Adopción de Pydantic V2 para el Dominio:** Se migran las entidades del dominio de `dataclasses` nativas a modelos de Pydantic V2 para garantizar validación de tipos en tiempo de ejecución, serialización limpia a YAML/JSON y manejo robusto de valores faltantes.
2. **Estrategia de Extracción en Dos Pasos:** No se intentará que la IA procese archivos binarios directamente. El pipeline consistirá en: Extractor Técnico (Texto Bruto) -> IA Estructuradora (JSON) -> Validación Pydantic.
3. **Tecnología de Extracción Base:** Se selecciona **PyMuPDF (`PyMuPDF`)** como el extractor principal de PDFs debido a su imbatible velocidad de procesamiento y su capacidad de segmentar por bloques de texto coordinates `(x, y)`, permitiendo leer layouts complejos de dos columnas sin mezclar la información.
4. **Almacenamiento Desacoplado:** La información se almacenará localmente en carpetas de usuario, separando la fuente de verdad (`resume.pdf`), el texto intermedio (`raw_text.txt`) y la salida estructurada (`profile.yaml`).

## Consecuencias
* **Positivas:** 
    * El dominio queda blindado contra respuestas malformadas de la IA.
    * Añadir soporte para nuevos formatos (como `.docx` o imágenes mediante OCR) solo requerirá crear un nuevo extractor que implemente la interfaz correspondiente, sin tocar la lógica de la IA.
    * La instalación para el usuario final en Windows, Linux y macOS se mantiene simple mediante el uso de *wheels* binarias precompiladas que no requieren herramientas de compilación en el sistema.
* **Negativas:**
    * Se añade una dependencia nativa pesada de ~40MB (`PyMuPDF`) al núcleo del proyecto.
    * Entornos de despliegue ultra-reducidos (como Docker con Alpine Linux) requerirán dependencias de compilación adicionales, lo que nos obligará a optar por imágenes basadas en Debian (`python-slim`) en el futuro.