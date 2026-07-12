# CandidateProfile (Perfil del Candidato)

El `CandidateProfile` es la entidad fundamental de PostuLatte. No es un simple reflejo de un archivo PDF; es una estructura viva sobre la cual se ejecutarán los análisis ATS, las búsquedas de ofertas y las adaptaciones de currículums.

## Estructura Conceptual del Modelo

El perfil se compone de cinco dimensiones clave, diseñadas para ser modulares y extensibles:

### 1. Información Personal (`personal`)
Contiene la identidad básica y canales de contacto directo del candidato.
* **Premisa:** Si un CV omitió datos críticos de contacto (como el teléfono o el enlace a LinkedIn), el sistema los marcará como ausentes para permitir la validación humana posterior, pero nunca asumirá valores ficticios.

### 2. Enfoque Profesional (`professional`)
Define el posicionamiento actual del candidato en el mercado laboral. Incluye los roles objetivo a los que aspira y un cálculo estimado de sus años de experiencia basándose en su trayectoria real.

### 3. Historial de Experiencia (`experience`)
Una secuencia cronológica de los hitos laborales del candidato. Cada hito registra la organización, el rol desempeñado, el periodo temporal y una descripción de responsabilidades o logros.

### 4. Competencias (`skills`)
El inventario de capacidades del candidato, segregado estrictamente para facilitar los cruces de datos en los motores de emparejamiento (Matching):
* **Habilidades Técnicas (*Hard Skills*):** Herramientas, lenguajes, metodologías o tecnologías específicas manejadas por el usuario.
* **Habilidades Blandas (*Soft Skills*):** Competencias interpersonales y de comportamiento profesional.

### 5. Idiomas (`languages`)
El registro de capacidades lingüísticas del candidato junto con sus respectivos niveles de competencia declarados.

---

## Filosofía del Conocimiento y Dinamismo
Aunque el perfil nace como una **fotografía estática del documento**, está diseñado para evolucionar de forma interactiva. El `CandidateProfile` acumula conocimiento a medida que el usuario interactúa con ofertas de empleo, permitiendo adiciones manuales validadas por el humano para complementar los baches informativos de la extracción inicial.