# principal.py

import pygame
import sys
from serpiente import Serpiente
from manzana import Manzana

pygame.init()

ANCHO = 720
ALTO = 480
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

WIN = pygame.display.set_mode((ANCHO, ALTO))
SCORE_FONT = pygame.font.SysFont("Russo One", 25)


def main():
    serpiente = Serpiente(ANCHO, ALTO)
    manzana = Manzana(ANCHO, ALTO)
    manzanas_comidas = 0
    velocidad = 1  # Inicializamos la velocidad

    fps = pygame.time.Clock()

    while True:
        fps.tick(10 * velocidad)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and serpiente.direccion[1] != 20:
                if event.key == pygame.K_UP:
                    serpiente.mover_arriba()

            if event.type == pygame.KEYDOWN and serpiente.direccion[1] != -20:
                if event.key == pygame.K_DOWN:
                    serpiente.mover_abajo()

            if event.type == pygame.KEYDOWN and serpiente.direccion[0] != -20:
                if event.key == pygame.K_RIGHT:
                    serpiente.mover_derecha()

            if event.type == pygame.KEYDOWN and serpiente.direccion[0] != 20:
                if event.key == pygame.K_LEFT:
                    serpiente.mover_izquierda()

        WIN.fill(VERDE)
        serpiente.dibujar(WIN, AZUL)

        if velocidad >= 1.4:
            manzana.mover()  # Mover la manzana independientemente de la serpiente
        manzana.dibujar(WIN)

        serpiente.mover()

        if manzana.verificar_colision(serpiente):
            manzanas_comidas += 1
            # Aumentar la velocidad cada vez que se come una manzana
            velocidad += 0.1
            manzana.aumentar_velocidad()

        if serpiente.morir(ANCHO, ALTO):
            pygame.quit()
            sys.exit()

        # Posiciona el texto de "Manzanas" a la izquierda
        texto_manzanas = SCORE_FONT.render("Manzanas: {}".format(manzanas_comidas), 1, (255, 255, 255))
        WIN.blit(texto_manzanas, (20, 20))

        # Agrega el texto de velocidad a la derecha
        texto_velocidad = SCORE_FONT.render("Velocidad: {:.1f}".format(velocidad), 1, (255, 255, 255))
        WIN.blit(texto_velocidad, (ANCHO - texto_velocidad.get_width() - 20, 20))

        pygame.display.update()

if __name__ == "__main__":
    main()