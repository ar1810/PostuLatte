# Roadmap de PostuLatte

Este documento describe la evolucion prevista del proyecto y el estado de cada sprint hasta la version 1.0.

---

# Estado actual

Version objetivo: **v1.0**

Sprint actual: **Sprint 5 ¡X Pipeline CV ¡÷ CandidateProfile**

Estado del proyecto:

- ? Arquitectura base
- ? Configuracion mediante YAML
- ? Integracion con Ollama
- ? Extraccion de documentos (PDF/DOCX)
- ?? Modelado del dominio del candidato

---

# Roadmap

| Sprint | Estado | Objetivo |
|---------|--------|----------|
| Sprint 1 | ? | Arquitectura base |
| Sprint 2 | ? | Sistema de configuracion |
| Sprint 3 | ? | Integracion con Ollama |
| Sprint 4 | ? | Extraccion de documentos |
| Sprint 5 | ?? | Pipeline CV ¡÷ CandidateProfile |
| Sprint 6 | ? | Buscador de ofertas |
| Sprint 7 | ? | Motor ATS |
| Sprint 8 | ? | Generador de CV |
| Sprint 9 | ? | Generador de cartas |
| Sprint 10 | ? | CLI completa |
| Sprint 11 | ? | Interfaz grafica |
| Sprint 12 | ? | Release v1.0 |

---

# Objetivos de cada Sprint

## Sprint 1 ¡X Arquitectura base ?

- Definicion de la arquitectura del proyecto.
- Organizacion del repositorio.
- Configuracion inicial de Git.
- Documentacion base.
- ADR iniciales.

---

## Sprint 2 ¡X Configuracion ?

- Sistema de configuracion basado en YAML.
- Validacion mediante Pydantic.
- Carga centralizada de configuracion.

---

## Sprint 3 ¡X Integracion Ollama ?

- Cliente para Ollama.
- Abstraccion del proveedor LLM.
- Configuracion del proveedor por defecto.

---

## Sprint 4 ¡X Extraccion de documentos ?

- Lectura de archivos PDF.
- Lectura de archivos DOCX.
- API unificada de extraccion.
- Tests unitarios.

---

## Sprint 5 ¡X Pipeline CV ¡÷ CandidateProfile ??

Objetivos:

- Definir el modelo `CandidateProfile`.
- Disenar el PromptBuilder.
- Implementar el parser estructurado.
- Validar respuestas mediante Pydantic.
- Crear los tests correspondientes.

---

## Sprint 6 ¡X Buscador de ofertas ?

Objetivos previstos:

- Modelo `JobOffer`.
- Integracion con buscadores.
- Importacion de ofertas.
- Normalizacion de datos.

---

## Sprint 7 ¡X Motor ATS ?

Objetivos previstos:

- Matching entre perfil y ofertas.
- Sistema de puntuacion.
- Explicacion del resultado.

---

## Sprint 8 ¡X Generador de CV ?

Objetivos previstos:

- Adaptacion automatica del CV.
- Multiples plantillas.
- Exportacion.

---

## Sprint 9 ¡X Generador de cartas ?

Objetivos previstos:

- Generacion personalizada.
- Adaptacion a cada oferta.

---

## Sprint 10 ¡X CLI completa ?

Objetivos previstos:

- Experiencia completa desde terminal.
- Automatizacion de flujos.

---

## Sprint 11 ¡X Interfaz grafica ?

Objetivos previstos:

- Aplicacion de escritorio.
- Gestion visual de perfiles y ofertas.

---

## Sprint 12 ¡X Release v1.0 ?

Objetivos previstos:

- Estabilizacion.
- Optimizacion.
- Documentacion final.
- Publicacion oficial.