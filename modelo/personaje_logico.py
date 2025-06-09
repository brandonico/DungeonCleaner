class Personaje:
    """Clase base para personajes."""
    def __init__(self, nombre, salud, ataque, velocidad_movimiento, arma):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.velocidad_movimiento = velocidad_movimiento 
        self.arma = arma
        
    def atacar(self, enemigo: "Personaje"):
        if self.ataque + self.arma == 0:
            golpe = 0
        else:
            golpe = (self.ataque + self.arma)
        return enemigo.recibir_danio(golpe)

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
        """metodo que devuelve el atributo protegido nombre"""
        return self.nombre
    
    def mostrar_vida(self):
        """metodo que mustra la vida del personaje"""
        return self.salud