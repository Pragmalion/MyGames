import pygame
from pygame import *

from const import *

from main import Main

init()
pygame.init()

screen = display.set_mode( size )
ARIAL_50 = font.SysFont('arial', 80)
image_back = pygame.image.load("fire.jpg")

class Main2:
    def start_game(self):
        main = Main()
        main.mainloop()
main2 = Main2()

class Scene1:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_options_index = 0
        pygame.display.set_caption('Menu of MEGA TIC TAC TOE')


    # Добавление опций
    def append_options(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, (255,255,255)))
        self._callbacks.append(callback)


    # Проверка выбранного пункта
    def switch(self, direction):
        self._current_options_index = max(0, min(self._current_options_index + direction, len(self._option_surfaces) - 1))


    # Выбор опции с послдеющим вызовом ее
    def select(self):
        self._callbacks[self._current_options_index]()


    # Отрисовка меню и его выбор
    def draw_menu(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_options_index:
                draw.rect(surf, (48, 213, 200), option_rect)
            surf.blit(option, option_rect)

    # Показ меню пользователю
    def show_menu(self):
        menu.append_options('Play', main2.start_game)
        # menu.append_options('Rules', scene_2)
        menu.append_options('Quit', quit)

    def print_text(self):
    # Создание объекта текста
        font = pygame.font.Font(None, 40) # Создание шрифта с размером 40
        font2 = pygame.font.Font(None, 25) # Создание шрифта с размером 25

    # Рендеринг текста (сам текст, антиалиасинг, цвет)
        text = font.render("Добро пожаловать в МЕГА кретстики нолики!", True, (255, 255, 255))
        text2 = font2.render("Чтобы передвигаться по меню используй W и S, а для выбора нажми E", True, (255, 255, 255))


        # Отображение первого текста на экране
        text_rect = text.get_rect()
        text_rect.center = (size[0] // 2, size[1] - (size[1] - 50))  # Расположение текста на экране
        screen.blit(text, text_rect)

        # Отображение второго текста на экране
        text2_rect = text.get_rect()
        text2_rect.center = (size[0] // 2 + 8, size[1] - (size[1] - 90))
        screen.blit(text2, text2_rect)




menu = Scene1()
menu.show_menu()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                menu.switch(-1)
            elif e.key == K_s:
                menu.switch(1)
            elif e.key == K_e:
                menu.select()


    screen.fill((0, 0, 0))
    screen.blit(image_back, (0, 0))
    menu.print_text()
    menu.draw_menu(screen, 318, 200, 170)
    display.flip()

quit()

if __name__ == '__main__':
    main = Main()

