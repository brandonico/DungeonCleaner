class Personaje:
    def __init__(self, nombre, salud, ataque, velocidad_movimiento):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.velocidad_movimiento = velocidad_movimiento

    def recibir_danio(self, golpe):
        print(f"{self.nombre} tiene {self.salud} puntos de salud.\n\tRecibió {golpe} puntos de daño.")
        self.salud = max(self.salud - golpe, 0)
        if self.salud > 0:
            return self.estado()
        return self.morir()

    def estado(self):
        print(f"\tAhora {self.nombre} tiene {self.salud} puntos de salud.\n----------")
        return False

    def morir(self):
        print(f"\t{self.nombre} ha muerto.\n")
        return True

    def mostrar_nombre(self):
        return self.nombre

    def mostrar_vida(self):
        return self.salud