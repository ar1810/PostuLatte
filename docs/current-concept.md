# PostuLatte - Concepto Actual del Proyecto

**Última actualización:** Agosto 2026

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

# Modelo del sistema

PostuLatte está diseñado alrededor de un dominio central que representa la información profesional del usuario y las oportunidades laborales analizadas.

Los datos externos son transformados en modelos estructurados antes de ser utilizados por las distintas funcionalidades del sistema.

La aplicación se organiza siguiendo principios de modularidad, separación de responsabilidades y desacoplamiento entre el núcleo del negocio y sus implementaciones externas.

---

# Modelo mental

PostuLatte no trabaja directamente con documentos.

Los documentos y fuentes externas son utilizados únicamente para construir información estructurada del dominio.

Ejemplo:

CV
↓
CandidateProfile

Oferta laboral
↓
JobDescription

CandidateProfile + JobDescription
↓
JobAnalysis

A partir de estas entidades, las funcionalidades del sistema pueden analizar, adaptar y generar contenido sin depender del formato original de los datos.

---

# Filosofía de IA

La inteligencia artificial es una herramienta de asistencia, no un reemplazo del criterio humano.

La IA no posee autoridad sobre las decisiones del usuario.

PostuLatte está diseñado para utilizar modelos locales o externos sin depender de un proveedor específico.

La IA analiza, propone y facilita tareas repetitivas.

El usuario mantiene siempre el control sobre las decisiones finales.

---

# Perfil profesional

El perfil profesional representa la fuente de verdad del dominio del usuario dentro del sistema.

Los documentos originales son únicamente fuentes de información que permiten construir dicho perfil.

Una vez construido el perfil, las funcionalidades posteriores operan sobre las entidades del dominio y no sobre los documentos originales.

Podrá construirse desde:

- CV PDF
- CV DOCX
- Edición manual
- Futuras integraciones (LinkedIn, GitHub, Portfolio)

Internamente siempre se convertirá a un CandidateProfile.

Si no existe un perfil cargado, PostuLatte debe guiar al usuario para crearlo.

La opción recomendada será importar un CV existente.

Posteriormente el usuario podrá revisar y corregir la información extraída.

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
- Proveedor de IA desacoplado
- Pipeline de construcción de CandidateProfile
- Instalador interactivo
- Documentación inicial
- ADR iniciales documentados

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