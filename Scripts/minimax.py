def minimax(self, posicion):
    if self.triunfo(p) == self.simbolo:
        return 1
    posibles = self.posiciones_siguientes(posicion)
    contrario = self.contrario.simbolo
    for p in posibles:
        if self.triunfo(p) == contrario:
            return -1
    for p in posibles:
        return minimax(p)
    
def heuristica(self, posicion):
        if self.triunfo(posicion) == self.simbolo:
            return 1
        rens = self.juego.renglones
        cols = self.juego.columnas
        totaltiros = (rens * cols)//4
        posibles = self.posiciones_siguientes(posicion)
        contrario = self.contrario.simbolo
        for p in posibles:
            if self.triunfo(p) == contrario:
                return -1

        for p in posibles:
            return self.heuristica(p)
