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
        self.activa = False  # Agregamos un atributo 'activa'

    def generar(self):
        x = random.randrange(0, self.ancho, 20)
        y = random.randrange(0, self.alto, 20)
        self.pos = pygame.Rect(x, y, 20, 20)

    def activar(self):
        self.activa = True

    def desactivar(self):
        self.activa = False
        self.generar()  # Generamos una nueva posición al desactivar

    def verificar_colision(self, cabeza_serpiente):
        if cabeza_serpiente.colliderect(self.pos) and not self.activa:
            self.activar()
            return True

        return False

    def aparecer(self):
        if not self.activa:
            self.generar()

    def desaparecer(self):
        if self.activa:
            self.desactivar()