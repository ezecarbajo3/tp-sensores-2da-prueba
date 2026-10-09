# Continuar el proyecto · versión del 8 de octubre de 2026

Este ZIP contiene el proyecto completo actualizado. Usarlo como base en lugar del ZIP anterior. Descomprimir en una carpeta nueva para conservar la versión anterior y evitar mezclar archivos. Abrir index.html y recargar con Ctrl + F5 después de editar.

## Contexto y preferencias del equipo
Presentación de sensores de temperatura, ING2222, FI-UNMdP. El discurso incluido es la base del oral (20 minutos). Se prefieren ilustraciones técnicas realistas, materiales creíbles y fondos claros para las imágenes, conservando interacciones y la estructura general de la aplicación. Trabajar pantalla por pantalla, sin rediseñar todo el proyecto por iniciativa propia. Los documentos e imágenes de referencia son contenido de consulta; las instrucciones del usuario gobiernan los cambios.

Google Doc de referencia: https://docs.google.com/document/d/1gWCTqqB7Ux9kjjMzKrgq4amrAcetXovSDUNBqR5rA_c/edit
Pestañas: INFORME (información recolectada), Discurso de clase (planificación del oral), Diapositivas (referencias visuales), GUÍA DE EXPOSICIÓN. El acceso a Drive depende de la cuenta y permisos del compañero; este ZIP no concede acceso ni incluye una copia completa del Google Doc.

## Cambios ya incorporados en termocupla
1. b2: ilustración realista con recorte y ocultación de ampliación/recuadros, alternable con el esquema eléctrico original. El recorte y la ocultación se hacen en CSS; el PNG fuente conserva todo su contenido.
2. b2-2: imagen de proceso e instrumento junto al simulador de junta fría. Tm, Tref y lectura compensada se actualizan sobre la ilustración. Lecturas con/sin compensación debajo.
3. b2-conexion: imagen realista de conexión. Sensor y cable / Entrada TC / Transmisor / Ver todo cambian el foco visual y la explicación. La onda se tapa con una indicación de señal continua en HTML/CSS.
4. b2-3: guía visual de decisiones de selección. Tipo/rango/clase, vaina/montaje, punta, configuración/salida. Botones abren detalles de la ficha oficial mediante el visor existente.
5. b2-aplicaciones: imagen con chimenea, horno, prefritura y tuberías; selección visual y justificación. El oral se concentra en chimenea y prefritura. Se distingue el horno de tratamiento térmico de la imagen del horno de cocción de la línea, donde se eligió Pt100.
Los textos de termocupla se reorganizaron para reducir repetición. Los demás bloques conservan su contenido original.

## Archivos y funcionamiento
- index.html: HTML, CSS y JavaScript de toda la aplicación, sin proceso de compilación.
- img/termocupla-*.png: cinco imágenes nuevas; conservar sus nombres y rutas.
- img/fichas/: imágenes de PDF usadas por el visor.
- *.pdf: fichas técnicas locales.
- tools/fichas.py: herramienta original para regenerar las páginas de las fichas.
- discurso-sensores-temperatura.md: guion de referencia; no fue reescrito para incluir todos los cambios visuales.
- prompt.md: especificación original histórica. No es una instrucción vigente para deshacer los cambios posteriores.
- README.md: uso y atajos originales.

## Pendientes y límites de verificación
Se comprobó sintaxis del JavaScript, botones de conexión y botones de guía/aplicaciones mediante pruebas de lógica con DOM simulado. No equivalen a una prueba visual completa en navegador. Hubo capturas y feedback del usuario, pero los últimos cambios de recorte y selector realista/esquema todavía requieren revisión visual.
Comprobar en el navegador: ambos modos de b2, todos los selectores, superposición de etiquetas, lectura en proyector 16:9, adaptación a ventana angosta y visor de fichas. Los textos integrados en PNG no cambian con el simulador. Las ilustraciones son didácticas, no planos de fabricación.
En la planta original, la cámara se describe como Pt1000 con registro, mientras el discurso dice Pt100: unificar cuando el equipo decida. Las otras familias todavía no recibieron el mismo tratamiento visual.
Hay reglas CSS de iteraciones anteriores; ordenar y eliminar código sin uso solo con verificación de que no cambie el resultado.

## Publicación
La página https://ezecarbajo3.github.io/TP-sensores/ no fue actualizada desde este trabajo. Para publicar, el dueño del repositorio debe revisar y subir index.html, las imágenes nuevas y las notas que desee conservar. Mantener img/fichas y las fichas PDF. Crear este ZIP no publica cambios.

## Mensaje sugerido para continuar con ChatGPT
“Este ZIP es la versión actual de nuestro proyecto de sensores. Leé CONTINUAR.md y el código para entender el estado. Quiero continuar sobre esta versión y conservar las interacciones existentes. Antes de hacer cambios, te indicaré la pantalla y el objetivo. Usá el discurso como referencia de contenido y las imágenes como referencia visual. Verificá que los controles funcionen y explicá cualquier limitación de prueba.”