from dagor import JuegoOrugas, JugadorOrugasAleatorio, JugadorOrugasInteractivo
jugador1 = JugadorOrugasInteractivo('Humano')
jugador2 = JugadorOrugasAleatorio('MaquinaTonta')
juego = JuegoOrugas(jugador1, jugador2, 5, 5)
juego.inicia()
