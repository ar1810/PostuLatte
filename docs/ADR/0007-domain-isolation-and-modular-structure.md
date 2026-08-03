# ADR 0007 - Normalización del dominio y separación en módulos independientes

## Estado
Aceptado

## Fecha
Agosto 2026

---

# Contexto

PostuLatte obtiene información desde múltiples fuentes externas:

* Documentos de usuario (PDF, DOCX).
* Ofertas laborales.
* Entrada manual.
* Futuras integraciones con plataformas externas.
* APIs o mecanismos automáticos de búsqueda.

Cada fuente posee formatos, estructuras y limitaciones diferentes.

Permitir que la lógica del sistema trabaje directamente con estas fuentes generaría un acoplamiento innecesario entre la infraestructura y las reglas del negocio.

Además, provocaría que las funcionalidades principales dependan del formato original de los datos, dificultando la evolución del proyecto y la incorporación de nuevas fuentes de información.

Durante la evolución de PostuLatte se identificó además la necesidad de ampliar el dominio del sistema para representar nuevas capacidades relacionadas con el análisis de oportunidades laborales.

Inicialmente el proyecto utilizaba una única estructura centralizada (`entities.py`) que contenía únicamente `CandidateProfile`.

La incorporación futura de nuevas entidades como `JobDescription` y `JobAnalysis` hace necesaria una separación más clara de responsabilidades.

Mantener todas las entidades en un único módulo incrementaría el acoplamiento y dificultaría la evolución del dominio.

---

# Problema

¿Cómo permitir que PostuLatte incorpore información de múltiples fuentes sin que el dominio dependa de ellas, y cómo organizar internamente esas entidades a medida que el dominio crece?

Ejemplos:

* Un CV no debería ser necesario para analizar una oferta después de crear el perfil profesional.
* Una oferta obtenida mediante scraping debería comportarse igual que una oferta ingresada manualmente.
* Cambiar un proveedor externo no debería modificar las reglas del negocio.

---

# Decisión

## Parte 1 - Normalización del dominio

Toda información externa que ingrese al sistema debe ser transformada previamente en una entidad del dominio.

El dominio será la única representación válida utilizada por los casos de uso internos.
Las entidades del dominio constituyen el contrato interno de la aplicación.

Ejemplos:

```
CV PDF/DOCX
      │
      ▼
CandidateProfile
```

```
Oferta laboral
      │
      ▼
JobDescription
```

```
CandidateProfile + JobDescription
      │
      ▼
JobAnalysis
```

Después de la normalización, las funcionalidades del sistema operarán exclusivamente sobre estas entidades.

El dominio no debe conocer:

* el formato original de los datos;
* la fuente de origen;
* el mecanismo utilizado para obtener la información.

## Parte 2 - Separación en módulos independientes

Se establece la separación progresiva de las entidades del dominio en módulos independientes. La estructura del dominio evolucionará hacia una organización donde cada entidad principal tenga una responsabilidad claramente definida.

Ejemplo:

```
src/domain/
│
├── entities/
│   ├── candidate.py
│   ├── job.py
│   ├── analysis.py
│   └── __init__.py
│
├── interfaces.py
└── exceptions.py
```

Las entidades principales serán:

- `CandidateProfile`
  Representa la información profesional estructurada del usuario.
- `JobDescription`
  Representa una oferta laboral normalizada independientemente de su origen.
- `JobAnalysis`
  Representa el resultado del análisis entre un perfil profesional y una oportunidad laboral.

---

# Principios establecidos

## Independencia del origen de datos

Las entidades del dominio no deben conocer si la información proviene de:

- archivos PDF;
- documentos DOCX;
- APIs;
- scraping;
- entrada manual.

Toda información externa debe ser normalizada antes de ingresar al dominio.

## Fuente única de verdad

Las entidades del dominio representan el estado válido del sistema.

Las fuentes externas únicamente sirven para construir o actualizar dichas entidades.

## Lenguaje ubicuo

A medida que el dominio crezca, PostuLatte deberá mantener una terminología común entre:

- código;
- documentación;
- arquitectura;
- futuras contribuciones.

Por este motivo se añadirá progresivamente un documento de referencia:

```
docs/
└── glossary.md
```

Este documento contendrá la definición conceptual de los principales modelos, módulos y términos utilizados dentro del proyecto.

Su objetivo será evitar ambigüedades entre conceptos técnicos y conceptos de negocio.

---

# Consecuencias positivas

* El dominio permanece independiente de la infraestructura.
* Nuevas fuentes de información pueden incorporarse mediante adaptadores sin modificar las reglas del negocio.
* Las entidades del dominio se convierten en contratos estables entre módulos.
* Facilita las pruebas unitarias al trabajar con modelos estructurados.
* Permite reemplazar proveedores externos sin afectar la lógica principal.
* Mayor claridad en las responsabilidades del dominio.
* Menor acoplamiento entre módulos.
* Mayor facilidad para agregar nuevas funcionalidades.
* Mejor mantenimiento del proyecto a largo plazo.
* Facilita la incorporación de nuevos colaboradores.

---

# Consecuencias negativas

* Se requiere una capa adicional de transformación entre fuentes externas y dominio.
* Requiere mantener modelos internos adicionales para representar el dominio, aumentando la cantidad de estructuras que deben ser diseñadas y mantenidas.
* Algunas operaciones simples pueden requerir pasos adicionales de normalización.
* Aumenta la cantidad de archivos del proyecto, al menos inicialmente.
* Requiere mantener correctamente las relaciones entre entidades.

---

# Alternativas consideradas

## Trabajar directamente con documentos o respuestas externas

Descartado.

Generaría dependencia directa entre las funcionalidades del sistema y los formatos de entrada.

## Permitir que cada módulo interprete sus propias fuentes

Descartado.

Duplicaría lógica de transformación y provocaría inconsistencias entre módulos.

## Mantener todas las entidades en un único archivo

Descartado.

Aunque es simple inicialmente, dificulta la escalabilidad del dominio cuando aumenta la cantidad de conceptos representados.

## Crear modelos directamente dentro de cada funcionalidad

Descartado.

Generaría duplicación de estructuras y rompería el principio de un dominio centralizado.

---

# Relación con otros ADR

Este ADR complementa:

* ADR 0003 - Parsing pipeline and data structure.
* ADR 0004 - CandidateProfile core domain.
* ADR 0006 - LLM provider decoupling.

Define la regla general que extiende el concepto de entidades de dominio más allá del procesamiento de CV, y establece la estructura modular en la que dichas entidades se organizarán a medida que el sistema crezca.

---

# Alcance

Este ADR aplica a todas las entidades del dominio presentes y futuras.

Toda nueva funcionalidad que incorpore información externa deberá transformarla previamente en entidades del dominio antes de que pueda ser utilizada por los casos de uso del sistema.

---
# Resultado esperado

PostuLatte dispondrá de un dominio modular y desacoplado de sus fuentes externas, donde cada concepto del negocio tenga una representación clara, independiente y documentada. La separación permitirá evolucionar el sistema sin comprometer la arquitectura existente.