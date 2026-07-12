# ADR 0004: CandidateProfile como Núcleo Central Desacoplado del Dominio

## Estado
Aceptado

## Contexto
En el Sprint 4 consolidamos la capacidad técnica de extraer texto bruto desde archivos PDF y DOCX. Al ingresar al Sprint 5, nos enfrentamos al desafío de diseñar cómo consumirán la información los módulos subsiguientes (Buscador de Ofertas, Motor ATS, Generador de CVs). 

Mantener una dependencia directa de los documentos originales o reprocesar el texto crudo en cada funcionalidad introduce acoplamiento innecesario, ineficiencia computacional por llamadas repetidas a los LLMs y una alta fragilidad ante cambios de formatos de archivos.

## Decisión
Se decide establecer la entidad **`CandidateProfile`** (implementada mediante Pydantic V2) como el núcleo central, único punto de verdad y modelo de datos unificado de PostuLatte.

1. **Fotografía de Información:** El pipeline de IA procesará el documento original **una única vez** al inicio para poblar este objeto del dominio.
2. **Abandono del Documento:** Una vez generado, validado y guardado el `CandidateProfile`, el resto del sistema (Motores de emparejamiento, generadores de cartas, etc.) trabajará exclusivamente consumiendo este objeto del dominio. Nunca se volverá a abrir el PDF/DOCX de origen para flujos de lógica de negocio.
3. **Evolución Dinámica:** El modelo no será estático. Permitirá la inyección interactiva de datos provistos por el usuario para enriquecer o corregir la "fotografía" inicial.

## Consecuencias
* **Positivas:**
    * **Desacoplamiento total:** Los módulos de análisis ATS o búsqueda de empleo no tienen idea de si el perfil nació de un PDF, un DOCX, un JSON o una carga manual.
    * **Eficiencia:** Reducimos drásticamente el consumo de tokens y procesamiento local, ya que la IA solo se utiliza en la fase de ingesta.
    * **Consistencia:** Todo el desarrollo futuro se programa contra una interfaz tipada y predecible.
* **Negativas:**
    * Si la extracción inicial omite información semántica relevante por fallas en el prompt, los módulos futuros no tendrán acceso a ella, delegando la responsabilidad de la completitud en la fase de validación humana obligatoria.