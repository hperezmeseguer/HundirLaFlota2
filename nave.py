class Nave:
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    # Metodo que recibe el disparo y gestiona las vidas de las naves
    def recibir_disparo(self):
        self.vida -= 1 # Si una nave fue tocada le resta una vida
        print(f"[LOG] Vidas restantes de {self.nombre}: {self.vida}")

        if self.vida == 0: # Si le quedan cero vidas printea que se hundió esa nave
            print(f"[LOG] Nave hundida")
