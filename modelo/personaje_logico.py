class Personaje:
    """Clase base personaje. Atributos y metodos basicos que comparten el enemigo y el jugador"""
    def __init__(self, nombre, salud, ataque, velocidad_movimiento):
        """inicializa un personje con los valores recibidos como parametros, 
        este metodo puede lanzar excepciones de value error, 
        si el nombre esta vacio o si el ataque es negativo """
        if nombre == '':
            raise ValueError("el nombre no puede estar vacio")
        self.nombre = nombre
        self.salud = salud
        if int(ataque)< 0:
            raise ValueError("el ataque no puede ser negativo")
        self.ataque = ataque
        self.velocidad_movimiento = velocidad_movimiento

    def recibir_danio(self, golpe):
        """metodo que recibe el golpe y se lo resta a la salud. 
        Si el golpe es mayor a la salud, la salud se queda en 0.
        Detecta si el personaje murio"""
        print(f"{self.nombre} tiene {self.salud} puntos de salud.\n\tRecibió {golpe} puntos de daño.")
        self.salud = max(self.salud - golpe, 0)
        if self.salud > 0:
            return self.estado()
        return self.morir()

    def estado(self):
        """metodo que muestra el nombre y la salud del personaje"""
        print(f"\tAhora {self.nombre} tiene {self.salud} puntos de salud.\n----------")
        return False

    def morir(self):
        """metodo que imprime un mensaje si el personaje muere"""
        print(f"\t{self.nombre} ha muerto.\n")
        return True

    def mostrar_nombre(self):
        """metodo que retorna el nombre del personaje"""
        return self.nombre

    def mostrar_vida(self):
        """metodo que retorna la salud del personaje"""
        return self.salud