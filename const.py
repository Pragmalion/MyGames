import pygame
from pygame import *

init()

WIDTH = 729 # 3^6
HEIGHT = 729

BG_COLOR = (255, 255, 255)
LINE_COLOR = (90, 90, 90)
CROSS_COLOR = (255, 77, 102)
CIRCLE_COLOR = (77, 144, 255)
DRAW_COLOR = (250, 0, 196)
FADE = (150, 150, 150)
size = (729,729)
screen = display.set_mode( size )
#ARIAL_50 = font.SysFont('Dpix_8pt', 80)
#image_back = pygame.image.load("fire.jpg")
image_back = pygame.image.load("tic.jpg")

ALPHA = 80 #прозрачность победы

DIM = 3