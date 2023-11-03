# manzana.py

import pygame
import random

class Manzana:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.color = (255, 0, 0)
        self.velocidad = 0  # Inicialmente, la velocidad es 0
        self.velocidad_inicial = 1
        self.generar()

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, self.color, self.pos)

    def generar(self):
        x = random.randrange(0, self.ancho, 20)
        y = random.randrange(0, self.alto, 20)
        self.pos = pygame.Rect(x, y, 20, 20)

    def mover(self):
        self.pos.y += self.velocidad

        # Si la manzana sale de la pantalla, la generamos de nuevo
        if self.pos.y > self.alto:
            self.generar()

    def aumentar_velocidad(self):
        self.velocidad += 0.1

    def verificar_colision(self, serpiente):
        if serpiente.cuerpo[0].colliderect(self.pos):
            self.generar()
            serpiente.agregar = True
            if self.velocidad > 0:  # Solo aumentar la velocidad si ya se mueven las manzanas
                self.aumentar_velocidad()
            return True

        for bloque in serpiente.cuerpo[1:]:
            if self.pos.colliderect(bloque):
                self.generar()

        return False