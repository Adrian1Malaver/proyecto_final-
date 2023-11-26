# serpiente.py
import pygame

class Serpiente:
    def __init__(self):
        self.cuerpo = [pygame.Rect(320, 240, 20, 20), pygame.Rect(320, 250, 20, 20), pygame.Rect(320, 260, 20, 20)]
        self.direccion = (0, -20)
        self.agregar = False
        self.velocidad = 1
        self.image_cabeza = pygame.image.load("cabeza.png")
        self.image_cabeza = pygame.transform.scale(self.image_cabeza, (20, 20))
        self.image_cuerpo = pygame.image.load("cuerpo.png")
        self.image_cuerpo = pygame.transform.scale(self.image_cuerpo, (20, 20))

    def dibujar(self, superficie, color):
        superficie.blit(self.image_cabeza, self.cuerpo[0].topleft)
        for bloque in self.cuerpo[1:]:
            superficie.blit(self.image_cuerpo, bloque.topleft)

    def mover(self):
        if self.agregar:
            nuevo_bloque = pygame.Rect(self.cuerpo[0].x + self.direccion[0], self.cuerpo[0].y + self.direccion[1], 20, 20)
            self.cuerpo.insert(0, nuevo_bloque)
            self.agregar = False
        else:
            for i in range(len(self.cuerpo) - 1, 0, -1):
                self.cuerpo[i].x = self.cuerpo[i - 1].x
                self.cuerpo[i].y = self.cuerpo[i - 1].y

            self.cuerpo[0].x += self.direccion[0] * self.velocidad
            self.cuerpo[0].y += self.direccion[1] * self.velocidad

    def mover_arriba(self):
        self.direccion = (0, -20)

    def mover_abajo(self):
        self.direccion = (0, 20)

    def mover_derecha(self):
        self.direccion = (20, 0)

    def mover_izquierda(self):
        self.direccion = (-20, 0)

    def morir(self, ancho, alto):
        if (
            self.cuerpo[0].x >= ancho
            or self.cuerpo[0].y >= alto
            or self.cuerpo[0].x <= -20
            or self.cuerpo[0].y <= -20
        ):
            return True

        for i in self.cuerpo[1:]:
            if self.cuerpo[0].colliderect(i):
                return True

        return False
    
    def disminuir_tamano(self):
        if len(self.cuerpo) > 10:
            for _ in range(10):
                self.cuerpo.pop()