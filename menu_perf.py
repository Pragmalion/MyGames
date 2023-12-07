import sys
from text import Text
from const import *


def button(x, y,
           width, height,
           inactive_colour,
           active_colour,
           screen, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_colour, (x+1, y, width, height))
        if click[0] and action is not None:
            action(screen)
    else:
        pygame.draw.rect(screen, inactive_colour, (x+1, y, width, height))


def exit(screen):
    pygame.display.quit()
    pygame.quit()
    quit()

pygame.display.set_caption('Menu of MEGA TIC TAC TOE')
def main_menu(screen, game_action=None, rules_action=None):
    black = 0, 0, 0
    blue = 0, 191, 225
    bright_blue = 0, 0, 0

    game_over = False

    text_object0 = Text("Добро пожаловать", 50)
    text_size = text_object0.get_text_size()
    text_object0.update_position(size[0] / 2 - text_size[0] / 2,
                                 (size[1] - 425 - text_size[1] / 2) - 200)

    text_object01 = Text("в Мега крестики-нолики!", 40)
    text_size = text_object01.get_text_size()
    text_object01.update_position(size[0] / 2 - text_size[0] / 2,
                                 (size[1] - 425 - text_size[1] / 2) - 120)

    text_object1 = Text("PLAY", 80)
    text_size = text_object1.get_text_size()
    btn1 = (size[0] / 2 - text_size[0] / 2, size[1] - text_size[1] / 2 - 400, text_size[0], text_size[1])
    text_object1.update_position(size[0] / 2 - text_size[0] / 2, (size[1] - 400 - text_size[1] / 2))

    text_object2 = Text("RULES", 50)
    text_size = text_object2.get_text_size()
    btn2 = (size[0] / 2 - text_size[0] / 2, size[1] - text_size[1] / 2 - 150, text_size[0], text_size[1] )
    text_object2.update_position(size[0] / 2 - text_size[0] / 2, (size[1] - 150 - text_size[1] / 2) )

    text_object3 = Text("EXIT", 50)
    text_size = text_object3.get_text_size()
    btn3 = (size[0] / 2 - text_size[0] / 2, size[1] - text_size[1] / 2 - 50, text_size[0], text_size[1] )
    text_object3.update_position(size[0] / 2 - text_size[0] / 2, (size[1] - 50 - text_size[1] / 2) )

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)
        screen.blit(image_back, (2, 2))
        button(*btn1, bright_blue, blue, screen, game_action)
        button(*btn2, bright_blue, blue, screen, rules_action)
        button(*btn3, bright_blue, blue, screen, exit)
        text_object1.draw(screen)
        text_object2.draw(screen)
        text_object3.draw(screen)

        text_object0.draw(screen)
        text_object01.draw(screen)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)

