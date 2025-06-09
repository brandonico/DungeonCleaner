class Espada:
    def __init__(self, nombre, daño, durabilidad, peso):
        self.nombre = nombre
        self.daño = daño
        self.durabilidad = durabilidad
        self.peso = peso

    def usar(self):
        if self.durabilidad > 0:
            self.durabilidad -= 1
            print(f"La espada {self.nombre} se usó, durabilidad restante: {self.durabilidad}")
        else:
            print(f"La espada {self.nombre} está rota y no puede usarse.")

    def esta_rota(self):
        return self.durabilidad <= 0