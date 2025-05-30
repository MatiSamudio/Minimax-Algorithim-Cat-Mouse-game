# Minimax-Algorithim-Cat-Mouse-game

El Gato y el Ratón - Simulador con Minimax
Este proyecto es un simulador donde un gato intenta atrapar a un ratón en un tablero 5x5. Ambos personajes se mueven de forma automática usando el algoritmo Minimax, que les permite tomar decisiones "inteligentes" según su objetivo:
El gato quiere atrapar al ratón.
El ratón quiere escapar hasta llegar a la cantidad maxima de turnos.

# Qué hace este programa?
Crea un tablero 5x5.
Coloca al gato en la esquina superior izquierda y al ratón en la inferior derecha.
Cada uno se mueve por turnos.
El gato trata de acorralar al ratón, y el ratón intenta huir.

El juego termina si:
El gato atrapa al ratón.
Se llega a la cantidad máxima de turnos y el ratón logra escapar.

# Qué logré?
Implementé el algoritmo Minimax para ambos personajes.
Separé la lógica en funciones claras: evaluación del tablero, posibles movimientos y decisiones por turno.
Logré una versión funcional, aunque todavía no se nota mucha “inteligencia” en los movimientos. Es un buen punto de partida.

# Qué no funcionó (todavía):
El comportamiento de los agentes, aunque funcional, no demuestra una "gran inteligencia". Sus decisiones pueden parecer arbitrarias en ciertas situaciones.
El Minimax no incluye **poda alfa-beta**, por lo que podría optimizarse significativamente.
  
# Momentos Ajá!:
Entender como mover a los personajes dentro del tablero con los indices de las listas.
Entender cómo una función de evaluación bien ajustada cambia radicalmente el comportamiento del agente fue revelador. La estructura del Minimax puede estar perfecta, pero sin una buena evaluación, el "cerebro" del jugador está ciego.
