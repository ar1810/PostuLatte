# PostuLatte

> Versión actual: **v0.6.0**

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

* ✅ Arquitectura basada en Clean Architecture y Domain-Driven Design (DDD).
* ✅ Dominio modular con entidades especializadas (`CandidateProfile`, `JobDescription` y `JobAnalysis`).
* ✅ Pipeline de extracción de perfiles profesionales desde documentos PDF y DOCX.
* ✅ Tailoring Engine para el análisis estructurado entre un perfil profesional y una oferta laboral.
* ✅ Integración con Ollama para ejecutar modelos locales.
* ✅ Sistema de configuración mediante YAML y Pydantic V2.
* ✅ CLI basada en `argparse`.
* ✅ Suite de pruebas unitarias e integración.
* ✅ Proveedores de IA desacoplados mediante interfaces.

---

# Funcionalidades planificadas

El objetivo es incorporar progresivamente:

* 📄 Generación de CV adaptados.
* ✉️ Generación de cartas de presentación.
* 🎯 Motor de compatibilidad ATS.
* 📊 Historial de postulaciones.
* 📁 Exportación de documentos.
* 🤖 Nuevos proveedores de IA.
* 🎤 Preparación de entrevistas.

---

# Arquitectura

El proyecto sigue una arquitectura modular donde cada componente tiene una responsabilidad específica.

```text
Documento (PDF/DOCX)
          │
          ▼
 CandidateProfile

Oferta laboral
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

**Versión actual:** `v0.6.0`

🚧 **En desarrollo activo.**

PostuLatte cuenta actualmente con una base técnica sólida sobre la que se desarrollarán las funcionalidades principales.

En esta versión ya se encuentran implementados:

- ✅ Clean Architecture y DDD.
- ✅ Configuración mediante YAML + Pydantic V2.
- ✅ Integración con Ollama.
- ✅ Extracción de documentos PDF y DOCX.
- ✅ Construcción de `CandidateProfile`.
- ✅ Normalización de ofertas laborales (`JobDescription`).
- ✅ Tailoring Engine.
- ✅ Generación de `JobAnalysis`.
- ✅ CLI mediante argparse.
- ✅ Suite de pruebas (17 tests).
- ✅ Documentación y ADR.

Actualmente el desarrollo se encuentra en el **Sprint 7**, enfocado en la evolución del motor de compatibilidad ATS y las funcionalidades construidas sobre `JobAnalysis`.

La arquitectura principal del proyecto ya se considera estable y los nuevos desarrollos se centran en ampliar las capacidades del dominio y los workflows.

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

## v0.1 a v0.6 (Hitos Alcanzados)

* [x] Arquitectura inicial y división en capas.

* [x] Configuración centralizada mapeada con Pydantic V2.

* [x] Integración hermética con Ollama y contratos de desacoplamiento.

* [x] Extractor físico polimórfico (PDF/DOCX).

* [x] Pipeline definitivo de orquestación y mapeo semántico hacia `CandidateProfile`.

* [x] Dominio modular (`CandidateProfile`, `JobDescription`, `JobAnalysis`).

* [x] Tailoring Engine para análisis estructurado de compatibilidad.

* [x] CLI con comandos `extract-cv` y `analyze-job`.

## Próximas versiones

* [ ] Motor de búsqueda e normalización de ofertas laborales.

* [ ] Motor de compatibilidad ATS.

* [ ] Generador de CV adaptado.

* [ ] Generador de cartas de presentación.

* [ ] Historial de postulaciones.

* [ ] Exportación de documentos.

* [ ] Preparación de entrevistas.

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
