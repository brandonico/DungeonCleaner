class Espada:
    def __init__(self, nombre, danio, durabilidad, peso):
        """inicializa una Espada con los valores recibidos como parametros"""
        self.nombre = nombre
        if int(danio)< 0:
            raise ValueError("el daño del arma no puede ser negativo")
        self.danio = danio
        self.durabilidad = durabilidad
        self.peso = peso

    def usar(self):
        """metodo para restar la durabilidad del arma e imprime la durabilidad restante"""
        self.durabilidad -= 1
        print(f"La espada {self.nombre} se usó, durabilidad restante: {self.durabilidad}")

    def esta_rota(self):
        """metodo que confirma si la espada esta rota o no, en base a la durabilidad"""
        return self.durabilidad <= 0