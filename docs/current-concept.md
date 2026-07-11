# PostuLatte - Concepto Actual del Proyecto

**Última actualización:** Julio 2026

---

## ¿Qué es PostuLatte?

PostuLatte es un asistente inteligente para la búsqueda de empleo.

Su objetivo no es reemplazar al usuario durante una postulación, sino eliminar las tareas repetitivas para que la persona pueda dedicar más tiempo a mejorar profesionalmente, prepararse para entrevistas o simplemente descansar.

La IA propone.
El usuario decide.

---

# Filosofía

PostuLatte debe ser una herramienta que acompañe al usuario, nunca una que tome decisiones por él.

No envía postulaciones automáticamente sin consentimiento.

No modifica información personal sin aprobación.

No inventa experiencia laboral.

No genera información falsa para aumentar las probabilidades de contratación.

Su función es asistir, sugerir y automatizar tareas repetitivas.

---

# Público objetivo

Está orientado a personas que:

- buscan su primer empleo;
- desean cambiar de trabajo;
- necesitan optimizar el tiempo dedicado a las postulaciones;
- quieren utilizar modelos de IA locales sin pagar suscripciones mensuales.

---

# Objetivos principales

Reducir el tiempo invertido en:

- búsqueda de ofertas;
- análisis de compatibilidad;
- adaptación del CV;
- generación de cartas de presentación;
- preparación de entrevistas.

---

# Arquitectura general

El proyecto sigue una arquitectura modular inspirada en Clean Architecture.

Se divide en:

- Dominio
- Infraestructura
- IA
- Workflow
- CLI
- Configuración

Cada módulo tiene una única responsabilidad.

---

# Filosofía de IA

La IA debe ser reemplazable.

El proyecto nunca dependerá de un único proveedor.

Actualmente:

✔ Ollama

Planificado:

- OpenAI
- Anthropic
- Gemini
- LM Studio
- otros proveedores compatibles

---

# Perfil del usuario

El perfil profesional será el núcleo del proyecto.

Podrá construirse desde:

- CV PDF
- CV DOCX
- edición manual
- futuras integraciones (LinkedIn, GitHub, Portfolio)

Internamente siempre se convertirá a un CandidateProfile.

---

# Experiencia de usuario

La aplicación debe ser fácil de usar.

Principios:

- enseñar sin abrumar;
- descubrir funciones progresivamente;
- evitar menús innecesarios;
- explicar los errores;
- nunca asumir que el usuario sabe cómo funciona la herramienta.

---

# Modos de uso

Se plantea soportar distintos estilos de utilización.

## Modo automático

El usuario solicita que PostuLatte realice el flujo completo.

Ejemplo:

Perfil →
Buscar ofertas →
Analizar →
Generar CV →
Generar carta →
Resumen final

---

## Modo asistido

El sistema guía al usuario paso por paso.

---

## Herramientas individuales

El usuario ejecuta únicamente la herramienta que necesita.

Ejemplos:

- analizar oferta
- generar CV
- preparar entrevista
- exportar documentos

---

# Perfil profesional

Si no existe un perfil cargado, PostuLatte debe guiar al usuario para crearlo.

La opción recomendada será importar un CV existente.

Posteriormente el usuario podrá revisar y corregir la información extraída.

---

# Principios de diseño

✓ Modular

✓ Escalable

✓ Offline First

✓ IA opcional

✓ Transparente

✓ Fácil de mantener

✓ Sin dependencias innecesarias

✓ Código desacoplado

✓ Configuración centralizada

---

# Estado actual

Implementado:

- Arquitectura base
- Dominio
- Interfaces
- Configuración mediante YAML + Pydantic
- Cliente Ollama
- Match ATS mediante IA
- Instalador interactivo
- Documentación inicial
- ADR iniciales

En planificación:

- Importación automática de CV
- Workflow modular
- Buscador de ofertas
- Generador de CV
- Carta de presentación
- Historial de postulaciones
- Preparación de entrevistas
- Exportación de documentos

---

Este documento representa la visión actual del proyecto y podrá evolucionar junto con PostuLatte.