# ADR 0006 Desacoplamiento Total del Proveedor de IA respecto al Dominio

## Estado
Propuesto

## Contexto
Actualmente, PostuLatte utiliza Ollama de forma local por defecto para resolver las tareas de asistencia e interpretación (consolidado en el Sprint 3). Al implementar el pipeline de estructuración del `CandidateProfile` en este Sprint, surge la necesidad técnica de invocar servicios de IA desde diferentes puntos de la aplicación.

Si permitimos que las entidades del dominio o las reglas de negocio importen directamente clientes de Ollama o dependan de sus especificaciones técnicas, el proyecto perderá flexibilidad. En el futuro, podríamos querer ofrecer configuraciones híbridas (ej. usar OpenAI o Anthropic para perfiles corporativos complejos, o cambiar a otro motor local ligero). El dominio debe permanecer agnóstico a estas decisiones de infraestructura.

## Decisión
Se determina aplicar de forma estricta el principio de Inversión de Dependencias (DIP) de SOLID para todas las interacciones con Inteligencia Artificial

1. Abstracción vía Interfaces El dominio solo interactuará con la IA a través de las firmas definidas en `srcdomaininterfaces.py` (como `AIService`). 
2. Aislamiento en Infraestructura El código específico de SDKs, formateo de payloads, manejo de reintentos y lógica de clientes de Ollama, OpenAI o cualquier otro proveedor residirá única y exclusivamente en la capa de infraestructura (`srcinfrastructure`).
3. Inyección de Dependencias Los casos de uso de la aplicación recibirán la instancia concreta del proveedor de IA en su constructor, programando siempre contra la interfaz abstracta del dominio.

## Consecuencias
 *Positivas
     *Flexibilidad absoluta Intercambiar Ollama por cualquier otra IA del mercado se vuelve una tarea de infraestructura de bajo impacto, requiriendo cero modificaciones en el núcleo del negocio.
     *Testabilidad mejorada Facilita la creación de Mocks o simuladores del servicio de IA para ejecutar pruebas unitarias del pipeline de forma instantánea sin depender de que el servidor de Ollama esté encendido o consuma hardware.
     *Cumplimiento de Clean Architecture Mantiene el centro de la cebolla arquitectónica libre de contaminación por librerías externas de terceros.
 *Negativas
    *Aumenta ligeramente la cantidad de código inicial (boilerplate) debido a la necesidad de mantener adaptadores específicos por cada proveedor de IA soportado.