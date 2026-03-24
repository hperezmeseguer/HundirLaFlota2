from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.lanzar_ataque(1, 1) # Lanzamos los ataques a diferentes ubicaciones (x, y)
        self.lanzar_ataque(1, 2) # Lanzamos los ataques a diferentes ubicaciones (x, y)
        self.lanzar_ataque(1, 3) # Lanzamos los ataques a diferentes ubicaciones (x, y)
        self.lanzar_ataque(1, 4) # Lanzamos los ataques a diferentes ubicaciones (x, y)
        self.lanzar_ataque(1, 4) # Lanzamos los ataques a diferentes ubicaciones (x, y)
        self.lanzar_ataque(1,5) # Lanzamos los ataques a diferentes ubicaciones (x, y)
        self.lanzar_ataque(1, 6) # Lanzamos los ataques a diferentes ubicaciones (x, y)


    def inicializar_naves(self):
        pass

    # Creación de un metodo que muestre el resultado de los ataques

    def mostrar_resultado(self, resultado):
        if resultado == 0: # No se tocó ninguna nave
            print("Agua")
        elif resultado == 1: # Se tocó parte de una nave
            print("Tocado")
        elif resultado == 2: # Se tocaron todas las partes de la nave y se hundió
            print("Hundido")


    # Creación de un metodo que muestre el resultado de los ataques

    def lanzar_ataque(self, x, y):
        print(f"Atacando {x}, {y}")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

if __name__ == '__main__':
    Juego()
