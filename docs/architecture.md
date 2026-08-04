# Arquitectura del Sistema

Este documento describe la arquitectura lógica de PostuLatte, las responsabilidades de cada capa y el flujo de información entre los distintos componentes del sistema.

La arquitectura sigue los principios de **Clean Architecture** y **Domain-Driven Design (DDD)**, priorizando el desacoplamiento entre el dominio del negocio y los detalles de infraestructura.

El objetivo es que las reglas del negocio permanezcan independientes de proveedores de IA, formatos de documentos, interfaces de usuario o mecanismos de obtención de ofertas laborales.

---

# Principios arquitectónicos

La arquitectura se basa en los siguientes principios:
- El dominio contiene únicamente reglas de negocio puras.
- La infraestructura implementa servicios externos sin contaminar el dominio.
- La capa de aplicación/core orquesta los casos de uso utilizando el dominio.
- Las dependencias siempre apuntan hacia adentro (hacia el dominio).
- El dominio representa la única fuente de verdad del sistema.
- Toda información externa debe normalizarse antes de ingresar al dominio.
- El dominio nunca depende del origen de los datos (CV, API, scraping o entrada manual).

## Principio de Normalización

Toda información externa que ingresa al sistema debe transformarse primero en una entidad del dominio.
A partir de ese momento, el resto de la aplicación opera exclusivamente sobre dichas entidades, sin depender del formato original ni del mecanismo mediante el cual fueron obtenidas.

---

# Arquitectura en capas

                 CLI / GUI
                     │
                     ▼
             Workflow (Flujos)
                     │
                     ▼
        Core (Casos de uso / Orquestación)
                     │
                     ▼
                 Dominio
                     ▲
                     │
     IA · Extraction · Config · Storage

* Las capas externas pueden depender de las internas.
* Las capas internas nunca conocen detalles de implementación de las capas externas.

---

# Responsabilidades de Componentes Clave

## src/domain

- Representa el núcleo del negocio.

- Contiene las entidades, modelos e interfaces que describen la realidad del dominio.

- Todas las operaciones posteriores trabajan exclusivamente sobre estas entidades normalizadas, independientemente del origen de los datos.

## src/core (Application)

- Coordina los casos de uso.

- No contiene reglas de negocio propias.

- Su responsabilidad es orquestar los distintos componentes del sistema utilizando únicamente las abstracciones definidas por el dominio.

## src/workflow

Representa los flujos completos que ejecuta el usuario.

Cada workflow combina uno o varios casos de uso para resolver una tarea concreta:

- Analizar una oferta.
- Adaptar un CV.
- Preparar una entrevista.
- Generar una carta de presentación.

Los workflows coordinan distintos servicios, pero no contienen reglas de negocio.

## src/extraction

- Implementa la transformación de documentos físicos en texto plano.

- Su responsabilidad termina una vez obtenido el contenido textual.

- No interpreta el significado de la información extraída.

## src/ai

- Implementa los proveedores de inteligencia artificial.

- Su responsabilidad consiste únicamente en transformar instrucciones estructuradas en respuestas estructuradas.

- No contiene reglas de negocio ni decisiones funcionales del sistema.

---

# Flujo de Normalización y Análisis

El flujo secuencial de la información se ejecuta de la siguiente manera de principio a fin:

Documento (PDF/DOCX)
        │
        ▼
ExtractorFactory
        │
        ▼
CandidateProfile

Oferta laboral
        │
        ▼
Normalización
        │
        ▼
JobDescription

CandidateProfile + JobDescription
        │
        ▼
Tailoring Engine
        │
        ▼
JobAnalysis

Una vez normalizada, cualquier oferta laboral se convierte en un JobDescription. El motor de adaptación compara esta entidad con el CandidateProfile del usuario y produce un JobAnalysis, que constituye el resultado estructurado del análisis de compatibilidad.

---

La arquitectura está diseñada para permitir la incorporación de nuevas fuentes de información sin modificar las reglas del dominio.

En el futuro podrán añadirse integraciones con APIs, plataformas de empleo, importación manual o scraping de ofertas laborales. Todas ellas deberán transformar la información obtenida en entidades del dominio antes de ser utilizadas por el resto del sistema.

Este principio garantiza el desacoplamiento entre la infraestructura y las reglas del dominio.

Como consecuencia, el proyecto puede evolucionar incorporando nuevos proveedores, nuevas interfaces o nuevas fuentes de datos sin comprometer el núcleo del negocio.

> **Nota:** Esta arquitectura representa el estado actual del proyecto a partir de la versión v0.6.0. Nuevos componentes podrán incorporarse en futuros sprints manteniendo los principios aquí definidos.