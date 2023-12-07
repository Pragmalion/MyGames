# -*- coding: utf-8 -*-
import sys
import pygame
from text import Text




text_array = [
Text("Правила:", 40, 250, 12),
Text(" Это МЕГА крестики нолик, тут после хода одного  ",20, 10, 105 + 5),
Text(" из игроков на маленьком поле игра перемещается в",20, 10, 135 + 5),
Text(" большое поле, соответсвующее тому, на которое   ",20, 10, 165 + 5),
Text(" игрок поставил крестик/нолик. После победы      ",20, 10, 195 + 5),
Text(" одного из игроков на маленьком поле, это поле   ",20, 10, 225 + 5),
Text(" становится недоступным, а при обращении к нему, ",20, 10, 255 + 5),
Text(" следующий игрок может выбрать любое доступное   ",20, 10, 285 + 5),
Text(" поле для хода. Побеждает игрок,первый собравший ",20, 10, 315 + 5),
Text(" комбинацию из классчиеских крестиков-ноликов, но ",20, 10, 345 + 5),
Text(" из выигранных полей.                            ",20, 10, 375 + 5),
Text(" СПРАВКА: нажмите R во время игры чтобы          ",20, 90, 500),
Text(" перезапустить и Q чтобы выйти. Удачи!           ",20, 90, 530),
Text("         <-- ESC чтобы вернуться в меню          ",20, 10, 640)
]

def draw_rule(screen):
    for i in text_array:
        i.draw(screen)

def rules_table(screen):
    #rules_score = text_array

    game_over = False
    game_quit = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True

        screen.fill((0,0,0))
        draw_rule(screen)

        pygame.display.flip()
        pygame.time.wait(20)
        pygame.display.update()
    if game_quit:
        sys.exit(0)
