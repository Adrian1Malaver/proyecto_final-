# manzana.py

import pygame
import random

class Manzana:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 0  # Inicialmente, la velocidad es 0
        self.velocidad_inicial = 1
        self.generar()
        self.imagen = pygame.image.load("manzana.png")  # Carga la imagen de la manzana
        self.imagen = pygame.transform.scale(self.imagen, (20, 20))  # Escala la imagen a 20x20

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

        return False