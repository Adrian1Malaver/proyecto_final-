#posion_velocidad.py

import pygame
import random

class PosionVelocidad:
    def __init__(self, ancho, alto, velocidad_serpiente):
        self.ancho = ancho
        self.alto = alto
        self.velocidad_serpiente = velocidad_serpiente
        self.generar()
        self.imagen = pygame.image.load("posion_velocidad.png")  # Carga la imagen de la poción de velocidad
        self.imagen = pygame.transform.scale(self.imagen, (20, 20))  # Escala la imagen a 20x20

    def generar(self):
        x = random.randrange(0, self.ancho, 20)
        y = random.randrange(0, self.alto, 20)
        self.pos = pygame.Rect(x, y, 20, 20)

    def verificar_colision(self, serpiente):
        if serpiente.cuerpo[0].colliderect(self.pos):
            self.generar()
            serpiente.velocidad_aumentar = True
            return True

        return False

    def aparecer(self, velocidad_serpiente):
        self.velocidad_serpiente = velocidad_serpiente
        self.generar()