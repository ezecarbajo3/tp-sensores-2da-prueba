# Plan de mejoras · implementación
Actualizado: 10 de octubre de 2026.

## Cambios aplicados

- [x] Mantener la pregunta inicial sobre horno, cámara y cinta.
- [x] Cierre que responde a esa pregunta y selección final con tres situaciones visuales.
- [x] Guion actualizado en [GUION-ORAL.md](GUION-ORAL.md), incluida Pt1000 con registro para la cámara.
- [x] Emisividad: imagen comparativa y pestañas **Qué cambia / Probar**.
- [x] Emisividad explicada como emisión relativa, sin «invisibilidad» ni promesa de exactitud.
- [x] Distinción entre tecnología IR y rango del modelo TW2000 (0–999,5 °C).
- [x] Tabla de cinco familias: **qué entrega / cómo lo lee el control / salida conmutada**.
- [x] Distinguir tensión LM35, dato DS18B20, entrada RTD/TC y salidas del TW2000.
- [x] 4 mA representa el mínimo del rango; 0 mA es una condición anormal, no identifica por sí solo una causa.
- [x] Lazo en respaldo con **Conexión real / Simulador**, conservando control de temperatura y corte de cable.
- [x] PNP/NPN en respaldo con **Conexión / Activar salida**, conservando el umbral interactivo.
- [x] Imagen superficie/centro en el mapa, visible al seleccionar punto 4 o 5.
- [x] El mapa cambia con clic o teclado; mover el mouse no cambia el punto seleccionado.
- [x] Imágenes ampliables con cierre por botón o Escape, proporción conservada y foco de teclado.
- [x] El avance principal termina en el cierre; fuentes y respaldo se abren por enlaces.
- [x] Termocupla: concentrar la información de señal y agregar nota de cable de extensión/compensación compatible.
- [x] Mantener RTD, escala Pt100/Pt1000 y 2/3/4 hilos sin borrar sus controles ni las fichas.

## Patrón visual y didáctico

**Dispositivo → funcionamiento → señal → conexión → aplicación.**

Fondo oscuro, un color por familia, imagen principal grande y notas cortas debajo. La primera vista explica la idea; las pestañas sirven para comparar o profundizar. Las ilustraciones son didácticas; las fichas del fabricante confirman el modelo real.

Recursos nuevos:
- `img/emisividad-comparacion.png`
- `img/lazo-4-20-conexion.png`
- `img/pnp-npn-conexion.png`
- `img/superficie-centro.png`

El lazo ilustrado es un ejemplo de dos hilos, transmisor alimentado por el lazo y entrada de corriente pasiva. PNP/NPN muestra ejemplos genéricos, no dos modelos específicos de temperatura.

## Recorrido del oral

| Bloque | Meta | Demostración |
|---|---:|---|
| Pregunta y criterios | 1:10 | Horno, cámara y cinta |
| Termocupla | 3:45 | Proceso fijo; cambiar temperatura de bornes |
| RTD | 4:15 | Escala y conexiones 2→3→4 |
| Termistor, integrado, IR | 4:00 | Frío/calor, tensión/dato y emisividad |
| Del sensor al PLC | 2:15 | Vista real y tabla |
| Selección | 2:20 | Tres decisiones; mapa opcional |
| Cierre | 0:45 | Responder a las situaciones iniciales |
| Margen | 1:30 | Cambios de expositor y pausas |
| **Total** | **20:00** | |

Los tiempos son objetivos de ensayo. Un simulador sigue **predecir → cambiar una variable → observar → explicar**. El detalle de lazo, conmutación y mapa de nueve puntos queda en respaldo.

## Pendiente del grupo

- [ ] Ensayar con cronómetro; confirmar tiempos reales y reparto de expositores.
- [ ] Comprobar legibilidad desde el proyector y en la pantalla completa que se usará.
- [ ] Confirmar que cada expositor sabe qué control tocar y cuándo avanzar.
- [ ] Llevar copia local del repositorio para problemas de conexión.
- [ ] Actualizar, si se sigue usando, la copia del discurso en Drive a partir de GUION-ORAL.md.

## Verificación técnica

Las comprobaciones de código, controles y publicación se resumen en el mensaje de entrega. Las pruebas del proyector y el ensayo del grupo no pueden reemplazarse por una revisión de código.

## Fuentes

- [ifm TW2000: rango y salidas](https://www.ifm.com/na/en/product/TW2000)
- [Fluke: emisión y reflexión](https://www.fluke.com/en/learn/blog/thermal-imaging/fixing-thermography-reflectivity)
- [NI: lazo 4–20 mA](https://www.ni.com/en/shop/data-acquisition/fundamentals--system-design--and-setup-for-the-4-to-20-ma-curren.html)
- [Omron: carga PNP y NPN](https://www.ia.omron.com/support/faq/answer/41/faq00379/)
- Fichas y bibliografía reunidas en la presentación.

