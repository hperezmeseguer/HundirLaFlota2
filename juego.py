from tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(1, 4)
        self.lanzar_ataque(1, 4)
        self.lanzar_ataque(1,5)
        self.lanzar_ataque(1, 6)


    def inicializar_naves(self):
        pass

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        print(f"Atacando {x}, {y}")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

if __name__ == '__main__':
    Juego()
