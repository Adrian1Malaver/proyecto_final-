# posion.py

import pygame
import random

class Posion:
    def __init__(self, ancho, alto, velocidad_serpiente):
        self.ancho = ancho
        self.alto = alto
        self.velocidad_serpiente = velocidad_serpiente
        self.generar()

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, (255, 255, 0), self.pos)

    def generar(self):
        x = random.randrange(0, self.ancho, 20)
        y = random.randrange(0, self.alto, 20)
        self.pos = pygame.Rect(x, y, 20, 20)

    def verificar_colision(self, serpiente):
        if serpiente.cuerpo[0].colliderect(self.pos):
            self.generar()
            serpiente.velocidad_disminuir = True
            return True

        return False

    def aparecer(self, velocidad_serpiente):
        self.velocidad_serpiente = velocidad_serpiente
        self.generar()