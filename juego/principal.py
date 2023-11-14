# principal.py

import pygame
import sys
from serpiente import Serpiente
from manzana import Manzana
from posion import Posion

pygame.init()

ANCHO = 720
ALTO = 480
VERDE = (0, 128, 0)
AZUL = (0, 0, 255)

WIN = pygame.display.set_mode((ANCHO, ALTO))
SCORE_FONT = pygame.font.SysFont("Arial", 20)

def main():
    serpiente = Serpiente()
    manzana = Manzana(ANCHO, ALTO)
    posion = Posion(ANCHO, ALTO, serpiente.velocidad)
    manzanas_comidas = 0
    velocidad = 1

    fps = pygame.time.Clock()

    while True:
        fps.tick(10 * velocidad)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mostrar_mensaje("Fin del juego. Manzanas comidas: {}".format(manzanas_comidas))
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
            manzana.mover()
        manzana.dibujar(WIN)

        if velocidad >= 2.7:
            posion.dibujar(WIN)

        serpiente.mover()

        if manzana.verificar_colision(serpiente):
            manzanas_comidas += 1
            velocidad += 0.1
            manzana.aumentar_velocidad()

        if velocidad >= 2.7:
            if posion.verificar_colision(serpiente):
                posion.aparecer(serpiente.velocidad)
                velocidad -= 0.5  # Reducción de velocidad

        if serpiente.morir(ANCHO, ALTO):
            mostrar_mensaje("Manzanas comidas: {}".format(manzanas_comidas))
            pygame.quit()
            sys.exit()

        # Texto de "Manzanas" a la izquierda
        texto_manzanas = SCORE_FONT.render("Manzanas: {}".format(manzanas_comidas), 1, (255, 255, 255))
        WIN.blit(texto_manzanas, (20, 20))

        # Texto de velocidad a la derecha
        texto_velocidad = SCORE_FONT.render("Velocidad: {:.1f}".format(velocidad), 1, (255, 255, 255))
        WIN.blit(texto_velocidad, (ANCHO - texto_velocidad.get_width() - 20, 20))

        pygame.display.update()

def mostrar_mensaje(mensaje):
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(mensaje, True, (255, 255, 255))
    WIN.blit(text, (ANCHO // 2 - text.get_width() // 2, ALTO // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)  # Espera 3000 milisegundos (3 segundos)

if __name__ == "__main__":
    main()