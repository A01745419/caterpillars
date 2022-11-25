from dagor import JuegoOrugas, JugadorOrugas, JugadorOrugasAleatorio, JugadorOrugasInteractivo

class JugadorOrugasEquipo10(JugadorOrugas):

    def heuristica(self, posicion, rango):
        if self.triunfo(posicion) == self.simbolo:
            return 1
        posibles = self.posiciones_siguientes(posicion)
        simbolocontrario = self.contrario.simbolo
        for p in posibles:
            if self.triunfo(p) == simbolocontrario:
                return -1
        acumulado = 0
        for p in posibles:
            acumulado += self.heuristica(p, rango)
            if acumulado > rango or acumulado < 1:
                return acumulado
        return acumulado
    
    def tira(self, posicion):
        posibles = self.posiciones_siguientes(posicion)
        puntos = 0
        rens = self.juego.renglones
        cols = self.juego.columnas
        totaltiros = (rens * cols)
        mejortiro = posibles[0]
        for p in posibles:
            intento = self.heuristica(p, totaltiros)
            if intento >= puntos:
                puntos = intento
                mejortiro = p
        return mejortiro

if __name__ == '__main__':
    juego = JuegoOrugas(
        JugadorOrugasEquipo10('Equipo 10'),
        JugadorOrugasAleatorio('RandomBoy'),
        10, 10)
    juego.inicia(veces=100, delta_max=2)
