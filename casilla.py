class Casilla:
    def __init__(self):
        # Guarda si en la casilla hay una nave o si ya fue atacada la casilla
        #Por defecto ponemos que no
        self.nave = None
        self.visitada = False

    # Metodo que comprueba el estado de la casilla
    def disparar(self):
        if self.visitada: # Si ya disparamos a la casilla printea eso
            print("Ya disparaste aquí")
            return None

        self.visitada = True

        if self.nave is None: # Si disparamos y no hay ninguna nave printea eso
            print("Agua")
            return 0

        return self.nave.recibir_disparo()