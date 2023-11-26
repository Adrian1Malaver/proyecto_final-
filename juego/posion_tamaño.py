# posion_tamaño.py
import pygame
import random

class PosionTamano:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.generar()
        self.imagen = pygame.image.load("posion_tamaño.png")
        self.imagen = pygame.transform.scale(self.imagen, (20, 20))
        self.aparecida = False  # Agregamos un atributo 'aparecida'

    def generar(self):
        x = random.randrange(0, self.ancho, 20)
        y = random.randrange(0, self.alto, 20)
        self.pos = pygame.Rect(x, y, 20, 20)

    def aparecer(self, manzanas_comidas):
        casos = {20: True, 30: True, 40: True}
        return casos.get(manzanas_comidas, False) and not self.aparecida

    def desaparecer(self):
        self.aparecida = False
        self.generar()  # Generamos una nueva posición al desaparecer

    def verificar_colision(self, cabeza_serpiente, manzanas_comidas):
        if cabeza_serpiente.colliderect(self.pos) and self.aparecer(manzanas_comidas):
            return True
        return False