# principal.py
import pygame
import sys
from serpiente import Serpiente
from manzana import Manzana
from posion_velocidad import PosionVelocidad
from posion_tamaño import PosionTamano

pygame.init()

ANCHO = 720
ALTO = 480
FONDO = pygame.image.load("fondo.png")
WIN = pygame.display.set_mode((ANCHO, ALTO))
SCORE_FONT = pygame.font.SysFont("Arial", 20)

sonido_coin1 = pygame.mixer.Sound("coin1.wav")
sonido_coin2 = pygame.mixer.Sound("coin2.wav")

def main():
    serpiente = Serpiente()
    manzana = Manzana(ANCHO, ALTO)
    posion_velocidad = PosionVelocidad(ANCHO, ALTO, serpiente.velocidad)
    posion_tamano = PosionTamano(ANCHO, ALTO)
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

        WIN.blit(FONDO, (0, 0))
        serpiente.dibujar(WIN, (255, 255, 255))

        if posion_tamano.verificar_colision(serpiente.cuerpo[0], manzanas_comidas):
            posion_tamano.aparecida = True
            serpiente.disminuir_tamano()
            sonido_coin2.play()

        if posion_tamano.aparecer(manzanas_comidas):
            WIN.blit(posion_tamano.imagen, posion_tamano.pos)

        if velocidad >= 1.4:
            manzana.mover()
        WIN.blit(manzana.imagen, manzana.pos)

        if velocidad >= 2.7:
            WIN.blit(posion_velocidad.imagen, posion_velocidad.pos)

            if posion_velocidad.verificar_colision(serpiente):
                posion_velocidad.aparecer(serpiente.velocidad)
                velocidad -= 0.5
                sonido_coin2.play()

        serpiente.mover()

        if manzana.verificar_colision(serpiente):
            manzanas_comidas += 1
            velocidad += 0.1
            manzana.aumentar_velocidad()
            sonido_coin1.play()

        if serpiente.morir(ANCHO, ALTO):
            mostrar_mensaje("Manzanas comidas: {}".format(manzanas_comidas))
            pygame.quit()
            sys.exit()

        texto_manzanas = SCORE_FONT.render("Manzanas: {}".format(manzanas_comidas), 1, (255, 255, 255))
        WIN.blit(texto_manzanas, (20, 20))

        texto_velocidad = SCORE_FONT.render("Velocidad: {:.1f}".format(velocidad), 1, (255, 255, 255))
        WIN.blit(texto_velocidad, (ANCHO - texto_velocidad.get_width() - 20, 20))

        pygame.display.update()

def mostrar_mensaje(mensaje):
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(mensaje, True, (255, 255, 255))
    WIN.blit(text, (ANCHO // 2 - text.get_width() // 2, ALTO // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

if __name__ == "__main__":
    main()