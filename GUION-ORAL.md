# Guion del oral · Familia 6: temperatura
Actualizado: 10 de octubre de 2026. Versión coordinada con la presentación del repositorio.

Las frases entre corchetes son acciones del expositor. El tiempo es una meta de ensayo, no una duración comprobada. Mantener el recorrido principal; las conexiones detalladas, curvas de respaldo y mapa de nueve puntos se abren cuando aportan o ante preguntas.

## 1 · Pregunta y criterios — 1:10

¿Mediríamos igual un horno, una cámara a menos dieciocho grados y un producto que pasa por una cinta? Los tres casos requieren medir temperatura, pero cambian el rango, la exactitud, el ambiente y la posibilidad de tocar el objeto.

Por eso vamos a empezar por el proceso y después elegir la tecnología. Una termocupla puede convenir en calor y ambiente severos; una RTD, cuando importan la exactitud y la estabilidad; un termistor, dentro de equipos o como protección. Los integrados se conectan a sistemas electrónicos, y el infrarrojo permite medir una superficie sin tocarla.

[Señalar las tres situaciones iniciales. En criterios, no leer cada fila completa.]

Con cada dispositivo veremos el mismo camino: cómo funciona, qué entrega y cómo se conecta al control.

## 2 · Termocupla — 3:45

La termocupla tiene dos conductores de metales distintos unidos en la punta que va al proceso. Si la temperatura de esa punta es diferente de la de los bornes donde se conecta el instrumento, aparece una tensión. Ese es el efecto Seebeck.

[Señalar punta, dos conductores y bornes en la imagen. Señalar mV en el circuito.]

El elemento genera su señal sin alimentación externa. El instrumento que la lee sí necesita alimentación. La señal es analógica, muy pequeña, de milivoltios, y tiene polaridad. Por eso se conecta a una entrada específica para termocupla o a un transmisor compatible, que puede convertirla en cuatro a veinte miliamperios.

La temperatura de los bornes también importa. Podemos pensarlo así: la señal nos informa de una diferencia entre el proceso y la referencia. Para obtener la temperatura del proceso necesitamos conocer esa referencia.

La junta fría son esos bornes de conexión. No significa que deban estar refrigerados. El instrumento mide su temperatura con un sensor auxiliar y usa ese dato para compensar la lectura.

[En junta fría, dejar el proceso fijo en 200 °C. Mover solo la temperatura de los bornes. Comparar lectura sin compensar y compensada.]

La tensión cambia al cambiar los bornes, pero la lectura compensada conserva la temperatura del proceso en este modelo. La fórmula que mostramos es una aproximación lineal; el instrumento real aplica la curva correspondiente al tipo de termocupla.

También por eso debemos cuidar la prolongación del cable. Se utiliza cable de extensión o compensación adecuado al tipo de termocupla y se respeta la polaridad. No se reemplaza cualquier tramo por cobre común sin considerar dónde quedan las nuevas uniones y sus temperaturas.

[Mostrar una decisión de la guía TC10-C y el dato correspondiente en la ficha. No recorrer todos los pasos.]

La ficha sirve para comprobar el modelo concreto: tipo, rango y clase, vaina, montaje y forma de lectura. La ilustración explica cómo está construida; la ficha confirma qué opciones ofrece esa sonda.

En nuestra línea, la chimenea de la caldera es un ejemplo de temperatura alta y ambiente exigente. En el aceite de prefritura también puede utilizarse una termocupla o una Pt100 adecuada: cubrir el rango no significa que haya una única solución.

[En aplicaciones, señalar rango térmico y robustez. La velocidad de respuesta también depende de la construcción de la sonda.]

## 3 · RTD: Pt100 y Pt1000 — 4:15

La RTD usa otro principio. Es un elemento de platino cuya resistencia aumenta con la temperatura de forma conocida y repetible. No produce una tensión por sí sola: el instrumento tiene que medir esa resistencia.

[Señalar elemento de platino, vaina, conductores y bornes.]

El instrumento hace pasar una corriente pequeña, mide la tensión y calcula la resistencia con la ley de Ohm. Después aplica la curva del platino y convierte los ohms en grados. La corriente debe ser baja para no calentar el propio sensor.

Pt100 significa cien ohms a cero grados. Pt1000 significa mil ohms a cero grados. Ambas usan el mismo principio y una curva normalizada equivalente, pero cambia la escala. Entre cero y cien grados, la sensibilidad media de la Pt100 es aproximadamente 0,385 ohms por grado; la de la Pt1000 es diez veces mayor.

Eso no significa diez veces más exactitud. Lo que aumenta es el cambio de resistencia por cada grado, y eso ayuda a reducir el impacto relativo de los cables.

[Señalar el mismo 1 Ω extra en la comparación.]

En conexión de dos hilos, el instrumento mide el sensor y los conductores juntos. Si el cableado agrega un ohm, en una Pt100 el error es aproximadamente 2,6 grados; en una Pt1000, 0,26 grados. Es el mismo cable con distinto impacto.

Ese problema explica las conexiones de dos, tres y cuatro hilos.

[Recorrer 2 → 3 → 4. Señalar dónde llegan los conductores al sensor.]

Con dos hilos, aceptamos que la resistencia de ida y vuelta se sume a la del sensor. Conviene si el error resultante es admisible.

Con tres hilos, la entrada compensa el efecto del cableado suponiendo resistencias iguales en los conductores. Si no son iguales, queda error. Es una solución frecuente para equilibrar exactitud y costo.

Con cuatro hilos, dos conductores llevan la corriente y otros dos miden la tensión directamente en los extremos del elemento. Por los de medición circula una corriente casi nula, de modo que su caída de tensión es despreciable. Así se reduce prácticamente a cero el error del cableado; la tolerancia propia del sensor sigue existiendo.

La elección depende del error que podemos aceptar, no solo de cuál conexión usa más gente.

[Mostrar en la ficha TR10-C la configuración y corriente de medición. Las restricciones de clases A y AA corresponden a este modelo concreto.]

Por fuera una RTD y una termocupla industrial pueden parecer casi iguales. Por dentro, una cambia resistencia y la otra genera milivoltios. En nuestra línea usamos RTD en mezcladora, horno de cocción y túnel IQF. Para la cámara a menos dieciocho grados, el ejemplo elegido en el mapa es una Pt1000 con registro. El registro lo realiza el equipo que lee el sensor.

## 4 · Termistor, integrado e infrarrojo — 4:00

El termistor también cambia su resistencia, pero utiliza un material semiconductor y su respuesta suele ser más marcada y no lineal.

[Mostrar frío/calor.]

En una NTC, la resistencia baja al aumentar la temperatura. En una PTC, aumenta; algunas PTC de protección presentan una transición muy marcada a cierta temperatura. La NTC puede medir dentro de refrigeración o climatización; una PTC de protección puede detectar sobretemperatura en un bobinado.

El termistor entrega una resistencia. El circuito externo permite leerla. Si hace falta ampliar, la pestaña de circuito muestra un divisor: el cambio de resistencia se convierte en un cambio de tensión. La curva se utiliza para pasar esa lectura a temperatura.

[En el oral, mantener la comparación real. Circuito y curva son ampliaciones opcionales.]

El sensor integrado es otra familia: el chip incluye el elemento sensible y la electrónica que prepara la salida. Ambos ejemplos necesitan alimentación.

El LM35 entrega una tensión analógica de diez milivoltios por grado: a veinticinco grados, doscientos cincuenta milivoltios. El DS18B20 comunica el dato de temperatura por 1-Wire. Una entrada de tensión y una interfaz digital son formas distintas de leerlos.

[Señalar tensión en LM35 y dato en DS18B20.]

Agregar un transmisor a una Pt100 no cambia su principio: sigue siendo una RTD. No pasa a ser un sensor integrado por tener electrónica añadida.

El infrarrojo es diferente porque mide sin contacto. Recibe la radiación térmica de una superficie; la lente la concentra, el detector la convierte en señal y la electrónica estima la temperatura.

[En la imagen del pirómetro, señalar superficie → lente → detector → electrónica.]

Mide la superficie, no el centro del producto. Si necesitamos conocer la temperatura interna, utilizamos una sonda que llegue a ese punto.

Acá aparece la emisividad: cuánto emite una superficie comparada con un emisor ideal. Dos superficies a la misma temperatura pueden emitir distinta radiación. Una superficie pulida también refleja más el entorno, y esa radiación reflejada influye en la medición.

[Comparar las dos superficies de la imagen. En Probar, dejar la temperatura fija, seleccionar metal pulido con ajuste equivocado y luego configurar la emisividad correcta.]

Ajustar la emisividad ayuda, pero no garantiza por sí solo una lectura exacta. Importan la superficie, el entorno y el área observada.

El TW2000 es un ejemplo concreto: mide de cero a 999,5 grados. Para una superficie bajo cero necesitamos otro modelo que cubra ese rango. Tiene salida de cuatro a veinte miliamperios y OUT1 configurable como salida PNP o comunicación IO-Link.

## 5 · Del sensor al PLC — 2:15

Ya vimos cómo mide cada uno. Ahora falta conectar esa medición al sistema de control: el sensor y la entrada del PLC tienen que ser compatibles.

[Mostrar Vista real. Cambiar a Conexión si hace falta señalar los dos caminos.]

La termocupla entrega milivoltios y la RTD cambia ohms. Un transmisor compatible puede convertir cualquiera de esas señales en cuatro a veinte miliamperios. Son dos ejemplos de señales primarias distintas que pueden llegar al PLC con la misma clase de salida industrial. Cada medición usa su canal.

También pueden utilizarse entradas específicas para termocupla o RTD. El termistor necesita un circuito o entrada que admita su curva. El LM35 necesita una lectura de tensión adecuada, y el DS18B20 una interfaz 1-Wire. El TW2000 ya incluye electrónica para sus salidas industriales.

[En la tabla, comparar las filas; no leer cada celda.]

En cuatro a veinte miliamperios, cuatro representa el mínimo del rango configurado y veinte el máximo. Cero miliamperios es una condición anormal, por ejemplo un corte de cable o falta de alimentación. La fuente debe poder cubrir las caídas de tensión del lazo.

PNP y NPN describen una salida conmutada: activa o inactiva. PNP entrega el positivo a la carga; NPN la conecta a cero voltios. Una Pt100 no conmuta. Entre los equipos presentados, el TW2000 tiene salida PNP.

[Lazo y PNP/NPN detallados quedan en respaldo. Abrir una conexión solo si se necesita explicar o responder una pregunta.]

## 6 · Selección y aplicación — 2:20

Volvemos a los tres casos iniciales.

En horno y gases calientes, miramos rango, ambiente y construcción. La termocupla suele convenir en calor severo; una RTD también puede ser válida si el modelo cubre el rango y buscamos exactitud y estabilidad. No existe una frontera universal de seiscientos grados.

En nuestra línea elegimos termocupla para la chimenea. En el horno de cocción, de noventa a ciento veinte grados, usamos Pt100 con transmisor: no todos los hornos requieren el mismo sensor.

Para la cámara a menos dieciocho grados elegimos Pt1000 con registro. Comprobamos el rango, la exactitud y la conexión; elegir una sonda buena no resuelve por sí solo el error de los cables.

En la cinta podemos controlar la superficie sin contacto. Pero superficie y centro son dos puntos de medición distintos.

[Si aporta al caso, abrir el mapa y comparar puntos 4 y 5; aparece la imagen de superficie/centro. Después señalar cámara o chimenea. No recorrer los nueve puntos.]

Si interesa el interior, la sonda tiene que llegar al centro. El infrarrojo no permite deducir por sí solo esa temperatura.

La ficha del modelo concreto confirma rango, exactitud, montaje y salida. La decisión empieza en la necesidad del proceso y termina en una medición que el control pueda leer correctamente.

## 7 · Cierre — 0:45

Volviendo al horno, la cámara y la cinta: elegimos según el proceso. Después comprobamos rango, exactitud, montaje y conexión en la ficha técnica.

Medir la misma variable no significa usar el mismo sensor ni la misma entrada. Tenemos que saber qué mide, qué entrega y cómo llega al control.

Muchas gracias.

[Finalizar en el cierre. El respaldo se abre por sus enlaces, no al avanzar automáticamente.]

## Ensayo del grupo

- Objetivo hablado y visual: 18:30. Margen: 1:30. Total: 20:00.
- Confirmar el reparto de expositores antes del ensayo.
- Cronometrar cada bloque; los tiempos no están validados hasta ensayar.
- Mover una variable por demostración.
- No leer todos los botones ni todas las páginas de las fichas.
- Mantener el mapa y los circuitos detallados disponibles para preguntas.

