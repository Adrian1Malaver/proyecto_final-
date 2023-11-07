# serpiente.py

import pygame

class Serpiente:
    def __init__(self, ancho, alto):
        x_centro = (ancho // 2) // 20 * 20  # Aseguramos que la posición sea múltiplo de 20
        y_centro = (alto // 2) // 20 * 20
        self.cuerpo = [pygame.Rect(x_centro, y_centro, 20, 20),
                       pygame.Rect(x_centro, y_centro + 10, 20, 20),
                       pygame.Rect(x_centro, y_centro + 20, 20, 20)]
        self.direccion = (0, -20)
        self.agregar = False

    def dibujar(self, superficie, color):
        for bloque in self.cuerpo:
            pygame.draw.rect(superficie, color, bloque)

    def mover(self):
        if self.agregar:
            nuevo_bloque = pygame.Rect(self.cuerpo[0].x + self.direccion[0], self.cuerpo[0].y + self.direccion[1], 20, 20)
            self.cuerpo.insert(0, nuevo_bloque)
            self.agregar = False
        else:
            for i in range(len(self.cuerpo) - 1, 0, -1):
                self.cuerpo[i].x = self.cuerpo[i - 1].x
                self.cuerpo[i].y = self.cuerpo[i - 1].y

            self.cuerpo[0].x += self.direccion[0]
            self.cuerpo[0].y += self.direccion[1]

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