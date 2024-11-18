import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.nivel = 1
        self.xp = 0

    def atacar(self):
        return random.randint(10, 20) * self.nivel
    
    def recibir_dano(self, dano):
        self.salud -= dano
        if (self.salud) <= 0:
            print(f"{self.nombre} ha muerto ¡Game Over!")
        else:
            print(f"Te quedan {self.salud} putnos de salud")

    def ganar_xp(self, xp):
        print(f"{self.nombre} ha ganado {xp} puntos de experiencia")
        self.xp += xp
        if self.xp >= 100:
            self.nivel += 1
            self.xp = 0
            print(f"{self.nombre} ha subido de nivel a {self.nivel}")