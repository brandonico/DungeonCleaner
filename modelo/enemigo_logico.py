class Enemigo:
    """Clase base para personajes."""
    def __init__(self, nombre, salud, ataque, velocidad_movimiento):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.velocidad_movimiento = velocidad_movimiento

    def atacar(self, enemigo: "Enemigo"):
        if self.ataque + self.arma == 0:
            golpe = 0
        else:
            if self.ataque + self.arma < enemigo.defensa:
                golpe = enemigo.defensa - (self.ataque + self.arma)
            else:
                golpe = (self.ataque + self.arma) - enemigo.defensa 
        return enemigo.defender(golpe)

    def defender(self, golpe):
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
        """metodo que devuelve el atributo protegido nombre"""
        return self.nombre
    
    def mostrar_vida(self):
        """metodo que mustra la vida del personaje"""
        return self.vida