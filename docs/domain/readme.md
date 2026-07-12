# Modelo del Dominio — PostuLatte

Este directorio contiene la documentación viva del modelo de negocio de PostuLatte. De acuerdo con los principios de Domain-Driven Design (DDD), el núcleo de nuestra aplicación está completamente aislado de la infraestructura, bases de datos o proveedores de IA.

## Lenguaje Ubicuo del Sprint 5

Para asegurar que todos los componentes hablen el mismo idioma, definimos los siguientes términos clave:

* **Candidato:** El profesional que utiliza la aplicación para gestionar su carrera y aplicar a ofertas.
* **Perfil del Candidato (CandidateProfile):** El modelo unificado, estructurado y consolidado que representa la realidad profesional del Candidato en un momento dado. Es la fuente de verdad para el resto de los módulos.
* **Fotografía del Documento:** El concepto de que el perfil inicial extraído por la IA debe reflejar única y exclusivamente lo que el documento original (CV) contenía, sin adulteraciones ni deducciones.
* **Extracción Pura:** El proceso técnico e intelectual de transferir datos desde un formato no estructurado a nuestro modelo, aplicando una política estricta de no invención.

## Modelos Documentados
* [CandidateProfile (Perfil del Candidato)](candidate-profile.md)