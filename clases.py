import numpy as np
import random

class Board:

    def __init__(self,):
        """
        Inicializa un tablero vacío y guarda el tamaño.
        """
        self.size = size
        self.board = np.full(size, " ")  # Crea un tablero vacío con espacios
        self.ships = []  # Lista para almacenar las posiciones de los barcos

    def generar_barcos(self):
        """
        Genera barcos aleatoriamente en el tablero.
        """
        for _ in range(cantidad):
            colocado = False
            while not colocado:
                x = random.randint(0, self.size[0] - 1)
                y = random.randint(0, self.size[1] - 1)
                orientacion = random.choice(["H", "V"])  # Horizontal o Vertical
                
                if self.comprobar_posicion(x, y, longitud, orientacion):
                    self.colocar_barcos(x, y, longitud, orientacion)
                    self.ships.append((tipo, longitud, (x, y), orientacion))
                    colocado = True

    def comprobar_posicion(self):
        """
        Comprueba si un barco cabe en la posición indicada.
        """
        if orientacion == "H":  # Horizontal
            if y + longitud > self.size[1]:
                return False
            return all(self.board[x, y + i] == " " for i in range(longitud))
        elif orientacion == "V":  # Vertical
            if x + longitud > self.size[0]:
                return False
            return all(self.board[x + i, y] == " " for i in range(longitud))


    def colocar_barcos(self):
        """
        Coloca un barco en el tablero.
        """
        if orientacion == "H":  # Horizontal
            for i in range(longitud):
                self.board[x, y + i] = "O"
        elif orientacion == "V":  # Vertical
            for i in range(longitud):
                self.board[x + i, y] = "O"
        
    def indices_tablero(self):
        """
        Devuelve una lista con las coordenadas del tablero.
        """
        return [(i, j) for i in range(self.size[0]) for j in range(self.size[1])]

    def generar_tablero(self):
        """
        Genera un tablero en forma de string para mostrarlo fácilmente.
        """
        print("  " + " ".join(str(i) for i in range(self.size[1])))
        for i, fila in enumerate(self.board):
            print(f"{i} " + " ".join(fila))

