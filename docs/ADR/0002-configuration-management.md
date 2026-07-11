# ADR 0002: Gestión de Configuración mediante YAML y Pydantic

## Estado
Propuesto

## Contexto
El proyecto requiere leer múltiples parámetros de configuración que gobernarán el comportamiento de la aplicación, tales como credenciales de proveedores de IA, niveles de logging y variables de entorno globales. Necesitamos un sistema que sea:
1. Humanamente legible y fácil de mantener (evitando JSONs complejos para configuración).
2. Altamente estructurado y tipado en tiempo de ejecución para evitar errores de tipo `KeyError`.
3. Modular, separando las configuraciones generales de las específicas de proveedores de IA.

## Decisión
Se decide utilizar archivos **YAML** localizados en la carpeta `config/` (`settings.yaml` y `providers.yaml`) combinados con **Pydantic** para el parseo, tipado y validación de datos en Python. 

La lectura se centralizará en `src/core/config.py`, exponiendo un objeto `config` global y validado.

### Razones de la elección:
* **Legibilidad:** YAML permite anidación clara y comentarios, ideal para estructurar perfiles de modelos de lenguaje (prompts, temperaturas, tokens).
* **Seguridad (Pydantic v2):** Garantiza que si falta un parámetro obligatorio o el tipo de dato es incorrecto (ej. una temperatura que debería ser *float* viene como *string*), la aplicación falle inmediatamente al arrancar y no en medio de un flujo crítico de IA.
* **Autocompletado:** Al mapear el YAML a clases de Pydantic, el IDE nos ofrecerá autocompletado nativo en todo el proyecto (`config.providers['openai'].model`).

## Consecuencias
* Se agregan `pyyaml` y `pydantic` como dependencias obligatorias del proyecto.
* Cualquier cambio estructural en los archivos de configuración requerirá actualizar su respectivo modelo de datos en `src/core/config.py`.