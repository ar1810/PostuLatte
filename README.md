# PostuLatte

> Versión actual: **v0.5.0**

> **Automatizá las tareas repetitivas de tu búsqueda laboral. Vos seguís tomando las decisiones.**

PostuLatte es un asistente de búsqueda laboral impulsado por Inteligencia Artificial diseñado para ayudar a las personas a ahorrar tiempo durante el proceso de postulación.

El objetivo del proyecto no es reemplazar el criterio del usuario, sino encargarse de las tareas repetitivas: analizar ofertas, evaluar compatibilidad, generar documentación personalizada y organizar la información para que la persona pueda concentrarse en lo realmente importante.

---

# ¿Por qué existe?

Buscar trabajo suele implicar dedicar horas a tareas repetitivas:

* Leer decenas de ofertas.
* Comparar requisitos con el perfil profesional.
* Adaptar el CV para cada postulación.
* Redactar cartas de presentación.
* Decidir cuáles oportunidades realmente valen la pena.

PostuLatte busca reducir ese tiempo.

En lugar de invertir horas preparando documentación para ofertas poco compatibles, el sistema ayuda a identificar las mejores oportunidades y automatiza gran parte del trabajo previo.

El tiempo recuperado puede utilizarse para estudiar, prepararse para entrevistas o simplemente disfrutar de un mejor equilibrio entre la búsqueda laboral y la vida personal.

---

# Filosofía del proyecto

PostuLatte fue diseñado siguiendo algunos principios simples.

* 🤝 **La IA ayuda, nunca reemplaza al usuario.**
* 🧠 **La decisión final siempre es humana.**
* 🏠 **Prioridad por modelos locales siempre que sea posible.**
* 🔒 **Respeto por la privacidad del usuario.**
* 🧩 **Arquitectura modular y extensible.**
* ⚙️ **Automatizar tareas repetitivas, no decisiones personales.**

---

# Características actuales

Actualmente el proyecto incluye:

* ✅ Arquitectura modular basada en capas.
* ✅ Integración con Ollama para ejecutar modelos locales.
* ✅ Sistema de configuración mediante YAML.
* ✅ Validación de configuración con Pydantic.
* ✅ Análisis de compatibilidad entre un perfil profesional y una oferta laboral.
* ✅ Respuestas estructuradas en JSON para evitar resultados ambiguos.
* ✅ Preparado para soportar múltiples proveedores de IA.

---

# Funcionalidades planificadas

El objetivo es incorporar progresivamente:

* 📄 Generación de CV adaptados a cada oferta.
* ✉️ Generación de cartas de presentación.
* 📊 Historial de postulaciones.
* 📁 Exportación a PDF.
* 🔍 Búsqueda automática de ofertas laborales.
* 🤖 Soporte para múltiples proveedores de IA.
* 📈 Métricas y estadísticas de postulaciones.
* 🎤 Preparación para entrevistas técnicas y de RR. HH.

---

# Arquitectura

El proyecto sigue una arquitectura modular donde cada componente tiene una responsabilidad específica.

```text
Usuario
   │
   ▼
Workflow
   │
   ├── Candidate Profile
   ├── Job Offer
   ├── AI Provider
   ├── Match Analyzer
   ├── Resume Generator
   ├── Cover Letter Generator
   └── Exporters
```

El dominio permanece completamente desacoplado de cualquier proveedor de IA, permitiendo incorporar nuevos modelos sin modificar la lógica principal del sistema.

---

# Modelos de IA

PostuLatte está pensado para funcionar con diferentes proveedores.

Actualmente:

| Proveedor | Estado           |
| --------- | ---------------- |
| Ollama    | ✅ Disponible     |
| OpenAI    | 🚧 En desarrollo |
| Anthropic | 🚧 Planificado   |
| Gemini    | 🚧 Planificado   |

La prioridad del proyecto es ofrecer una excelente experiencia utilizando modelos ejecutados localmente, evitando la dependencia obligatoria de suscripciones o servicios en la nube.

---

# Estado del proyecto

**Versión actual:** `v0.5.0`

🚧 **En desarrollo activo.**

PostuLatte cuenta actualmente con una base técnica sólida sobre la que se desarrollarán las funcionalidades principales.

En esta versión ya se encuentran implementados:

- ✅ Arquitectura basada en Domain-Driven Design (DDD) y Clean Architecture.
- ✅ Sistema de configuración mediante YAML y Pydantic V2.
- ✅ Integración con Ollama como proveedor LLM local por defecto.
- ✅ Extracción unificada de documentos PDF y DOCX.
- ✅ Tests unitarios para los módulos implementados.
- ✅ Documentación arquitectónica y ADR del proyecto.

Actualmente el desarrollo se centra en el **Sprint 5**, cuyo objetivo es construir el modelo de dominio `CandidateProfile`, que servirá como núcleo para todas las funcionalidades futuras del proyecto.

La API y la estructura interna todavía pueden evolucionar antes de la primera versión estable (`v1.0.0`), aunque la arquitectura principal ya se considera estable.

---

# Instalación

La documentación de instalación estará disponible a medida que el proyecto avance.

Por el momento se requiere:

* Python 3.12 o superior
* Git
* Ollama (opcional, recomendado)
* Un modelo compatible (por ejemplo: Llama 3)

---

# Roadmap

## v0.1 a v0.5 (Hitos Alcanzados)

* [x] Arquitectura inicial y división en capas.

* [x] Configuración centralizada mapeada con Pydantic V2.

* [x] Integración hermética con Ollama y contratos de desacoplamiento.

* [x] Extractor físico polimórfico (PDF/DOCX).

* [x] Pipeline definitivo de orquestación y mapeo semántico hacia CandidateProfile.

## Próximas versiones

* [ ] Motor de búsqueda e ingesta de ofertas (JobOffer).

* [ ] Sistema de matching y análisis ATS.

* [ ] Motor de generación de CV.

* [ ] Cartas de presentación adaptativas.

* [ ] Historial de postulaciones y exportación a PDF.

---

# Contribuciones

Actualmente PostuLatte es un proyecto personal en desarrollo.

En esta etapa el código no acepta contribuciones externas mientras la arquitectura continúa evolucionando.

---

# Licencia

Todos los derechos reservados.

El código fuente se publica únicamente con fines de consulta y seguimiento del desarrollo.

No está permitido copiar, redistribuir ni utilizar este proyecto o partes del mismo sin autorización expresa del autor.

---

## Una última idea

La inteligencia artificial no debería decidir tu futuro profesional.

Debería ayudarte a invertir menos tiempo en tareas repetitivas para que puedas dedicar más tiempo a crecer profesionalmente.

Esa es la razón de ser de **PostuLatte**.
