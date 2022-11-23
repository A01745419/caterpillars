from dagor import JuegoOrugas, JugadorOrugas, JugadorOrugasAleatorio

class JugadorOrugasEquipo10(JugadorOrugas):

    def heuristica(self, posicion):
        return self.triunfo(posicion) == self.simbolo
    
    def tira(self, posicion):
        posibles = self.posiciones_siguientes(posicion)
        for p in posibles:
            if self.heuristica(p):
                return p
        return posibles[0]

if __name__ == '__main__':
    juego = JuegoOrugas(
        JugadorOrugasEquipo10('Equipo 10'),
        JugadorOrugasAleatorio('RandomBoy'),
        5, 8)
    juego.inicia(veces=100, delta_max=2)