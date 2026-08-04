# Glosario

Este documento define el lenguaje ubicuo utilizado por PostuLatte.

Solo se documentan conceptos implementados o formalizados mediante ADR.
Las definiciones deben permanecer breves, estables y orientadas al dominio.

---

## CandidateProfile

> Representa el perfil profesional estructurado del usuario.

# Responsabilidad

Centralizar toda la información profesional del candidato.

# Relacionado con

- PersonalInfo
- ProfessionalFocus
- ExperienceHito
- SkillsInventory
- LanguageCompetence
- ProfileExtractionPipeline

---

## PersonalInfo

> Representa la información personal básica del candidato.

# Responsabilidad

Centralizar los datos de identificación y contacto.

# Relacionado con

- CandidateProfile

---

## ProfessionalFocus

> Representa el posicionamiento profesional del candidato.

# Responsabilidad

Describir los roles objetivo y la experiencia general del candidato.

# Relacionado con

- CandidateProfile

---

## ExperienceHito

> Representa un hito dentro de la experiencia laboral del candidato.

# Responsabilidad

Describir una experiencia profesional específica.

# Relacionado con

- CandidateProfile

---

## SkillsInventory

> Representa el conjunto de habilidades del candidato.

# Responsabilidad

Organizar las habilidades técnicas y blandas.

# Relacionado con

- CandidateProfile

---

## LanguageCompetence

> Representa el conocimiento de un idioma.

# Responsabilidad

Registrar un idioma y el nivel declarado por el usuario.

# Relacionado con

- CandidateProfile

---

## AIService

> Define el contrato que deben implementar los proveedores de inteligencia artificial.

# Responsabilidad

Desacoplar el dominio de cualquier proveedor de IA.

# Relacionado con

- OllamaAIService
- ProfileExtractionPipeline

---

## OllamaAIService

> Implementa el contrato AIService utilizando Ollama.

# Responsabilidad

Transformar texto bruto en información estructurada del dominio.

# Relacionado con

- AIService
- PromptBuilder
- CandidateProfile

---

## PromptBuilder

> Construye las instrucciones enviadas al modelo de IA.

# Responsabilidad

Generar prompts consistentes para la extracción estructurada de información.

# Relacionado con

- OllamaAIService

---

## ProfileExtractionPipeline

> Orquesta la construcción de un CandidateProfile a partir de un documento.

# Responsabilidad

Coordinar la extracción, el procesamiento mediante IA y la validación del dominio.

# Relacionado con

- CandidateProfile
- AIService
- ExtractorFactory

---

## ExtractorFactory

> Selecciona el extractor adecuado según el tipo de documento.

# Responsabilidad

Desacoplar el procesamiento del formato físico del documento.

# Relacionado con

- PDFExtractor
- DOCXExtractor
- ProfileExtractionPipeline

---

## JobDescription

> Representa los requisitos y detalles de una oferta laboral.

# Responsabilidad

Centralizar las exigencias, el rol y las competencias requeridas por un puesto.

# Relacionado con

- JobAnalysis
- CandidateProfile

---

## JobAnalysis

> Representa el resultado de la evaluación entre un candidato y un puesto.

# Responsabilidad

Consolidar el nivel de compatibilidad, brechas identificadas y recomendaciones.

# Relacionado con

- CandidateProfile
- JobDescription

---

## DomainException

> Representa un error de regla de negocio o falla en las validaciones del dominio.

# Responsabilidad

Garantizar que las violaciones de invariantes de dominio sean capturadas de forma explícita.

# Relacionado con

- CandidateProfile
- JobDescription
- JobAnalysis

---

## JobAnalyzerWorkflow

> Orquesta la comparación entre el perfil de un candidato y una oferta laboral.

# Responsabilidad

Ejecutar el análisis de compatibilidad (gap analysis) utilizando la IA para generar un informe estructurado.

# Relacionado con

- CandidateProfile
- JobDescription
- JobAnalysis
- AIService