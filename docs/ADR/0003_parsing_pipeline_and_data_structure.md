# ADR 0003: Pipeline de Importación y Normalización del Perfil Profesional

## Estado

Aceptado

---

## Contexto

Uno de los objetivos principales de PostuLatte es reducir al mínimo el tiempo que el usuario dedica a tareas repetitivas durante la búsqueda laboral.

La experiencia deseada es sencilla:

> "Importá tu CV. Nosotros hacemos el resto."

El usuario no debería verse obligado a completar formularios extensos para crear su perfil profesional. En su lugar, la aplicación deberá transformar documentos no estructurados (como PDF o DOCX) en un perfil profesional validado y estructurado.

Además, el sistema debe cumplir los siguientes principios:

- La IA nunca debe inventar información inexistente.
- La información extraída debe validarse antes de ser utilizada.
- El pipeline debe ser extensible para soportar nuevos formatos de entrada en el futuro.
- El documento original siempre debe conservarse para permitir un reprocesamiento posterior.

---

## Decisión

Se adopta una arquitectura de importación basada en un pipeline compuesto por etapas independientes.

### 1. Extracción del documento

Los archivos proporcionados por el usuario (PDF, DOCX u otros formatos futuros) serán procesados por un extractor especializado cuya única responsabilidad será obtener el texto del documento.

La IA nunca procesará directamente archivos binarios.

---

### 2. Normalización mediante IA

El texto extraído será enviado al proveedor de IA configurado para convertirlo en un objeto JSON estructurado.

La IA deberá respetar estrictamente las siguientes reglas:

- No inventar información.
- Devolver `null` cuando un dato no exista.
- Responder únicamente con JSON válido.

---

### 3. Validación del dominio

La salida generada por la IA será validada mediante modelos de **Pydantic V2**, que representan el dominio del proyecto.

Esto garantiza:

- validación de tipos;
- valores por defecto consistentes;
- serialización sencilla a YAML y JSON;
- detección temprana de respuestas inválidas.

---

### 4. Almacenamiento desacoplado

Cada perfil profesional conservará separadas las distintas etapas del proceso.

Ejemplo:

```
workspace/
└── profile/
    ├── resume.pdf
    ├── raw_text.txt
    └── profile.yaml
```

Esto permitirá reprocesar el documento original cuando existan mejoras en los modelos de IA o en el pipeline de extracción.

---

## Arquitectura del Pipeline

```
Documento (PDF / DOCX)
            │
            ▼
Document Extractor
            │
            ▼
      Texto plano
            │
            ▼
 AI Structuring Service
            │
            ▼
      JSON estructurado
            │
            ▼
 Validación Pydantic
            │
            ▼
  CandidateProfile
            │
            ▼
     profile.yaml
```

---

## Alternativas consideradas

### Procesar directamente el PDF con la IA

Descartado.

Acopla el proyecto al proveedor de IA, dificulta el soporte para distintos modelos y obliga a depender de capacidades específicas de cada proveedor.

---

### Parsear el CV mediante expresiones regulares

Descartado.

Los CV presentan demasiadas estructuras y formatos distintos, lo que haría el mantenimiento extremadamente complejo y poco fiable.

---

### Mantener el documento original únicamente

Descartado.

Obligaría a reprocesar completamente el CV cada vez que el sistema necesite acceder a la información del perfil.

---

### Utilizar únicamente un formulario manual

Descartado.

Contradice uno de los principales objetivos del proyecto: minimizar el tiempo invertido por el usuario en tareas repetitivas.

---

## Consecuencias

### Positivas

- El dominio queda completamente desacoplado del formato original del documento.
- La IA puede reemplazarse sin modificar el resto del pipeline.
- Es sencillo añadir nuevos formatos (DOCX, imágenes mediante OCR, Markdown, HTML, etc.).
- Los modelos de Pydantic garantizan que la aplicación trabaje únicamente con datos válidos.
- El documento original permanece disponible para futuros reprocesamientos.

### Negativas

- Se incorpora una dependencia adicional (`PyMuPDF`) para la extracción de PDFs.
- El proceso de importación añade una etapa más respecto a un análisis directo mediante IA.
- Algunos entornos extremadamente reducidos pueden requerir dependencias adicionales para la instalación de PyMuPDF.

---

## Notas

Esta decisión constituye uno de los pilares fundamentales de PostuLatte.

Todo perfil profesional utilizado por la aplicación deberá convertirse previamente en un `CandidateProfile`, independientemente de su origen (PDF, DOCX, LinkedIn, GitHub, Portfolio u otros formatos futuros).