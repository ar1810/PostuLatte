# Arquitectura del Sistema

Este documento describe la arquitectura de PostuLatte, las responsabilidades de cada capa y el flujo general de información dentro de la aplicación.

El proyecto sigue los principios de **Arquitectura Limpia (Clean Architecture)** y **Diseño Guiado por el Dominio (DDD)**.

---

# Principios arquitectónicos

La arquitectura se basa en cuatro principios fundamentales:

- El dominio contiene únicamente reglas de negocio.
- La infraestructura implementa servicios externos sin afectar al dominio.
- La aplicación orquesta los casos de uso utilizando el dominio.
- Las dependencias siempre apuntan hacia el dominio.

---

# Arquitectura en capas

```
CLI / GUI
     │
     ▼
Application
     │
     ▼
Domain
     ▲
     │
Infrastructure
```

Las capas externas pueden depender de las internas.

Las capas internas nunca conocen detalles de implementación externos.

---

# Responsabilidades

## Domain

Representa el corazón del proyecto.

Contiene:

- Modelos del dominio
- Value Objects
- Interfaces (Contratos)
- Reglas de negocio

El dominio nunca conoce:

- Ollama
- OpenAI
- Archivos
- YAML
- CLI
- GUI

---

## Application

Implementa los casos de uso.

Ejemplos:

- Importar CV
- Analizar ofertas
- Generar CV
- Generar carta
- Preparar entrevista

La capa Application coordina los servicios necesarios para completar una tarea, pero no contiene reglas de negocio complejas.

---

## Infrastructure

Implementa la comunicación con el mundo exterior.

Incluye:

- Proveedores LLM
- Lectores PDF
- Lectores DOCX
- Configuración
- Persistencia
- Logging

Toda dependencia externa permanece confinada a esta capa.

---

# Flujo principal

La información fluye de la siguiente manera:

```
Documento

↓

Extractor

↓

Texto

↓

PromptBuilder

↓

Proveedor LLM

↓

JSON

↓

CandidateProfile

↓

Casos de uso
```

Una vez generado el `CandidateProfile`, el documento original deja de ser necesario para el funcionamiento normal del sistema.

Todas las funcionalidades posteriores trabajan sobre el modelo del dominio.

---

# Modelo de dominio

El modelo `CandidateProfile` constituye el núcleo de PostuLatte.

Representa una fotografía estructurada del perfil profesional del usuario obtenida a partir de la documentación importada.

Las funcionalidades futuras reutilizan este modelo para evitar reprocesar continuamente los documentos originales.

---

# Independencia de proveedores

El dominio nunca conoce el proveedor de IA utilizado.

Actualmente el proveedor por defecto es Ollama, pero la arquitectura permite incorporar nuevos proveedores sin modificar las reglas de negocio.

La comunicación con cualquier modelo de lenguaje se realiza mediante interfaces definidas por el dominio e implementadas por la infraestructura.