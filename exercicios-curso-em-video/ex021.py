#Programa que toca um áudio em mp3

import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('lifelike-126735.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()