# from const import *
# from main import Main
# #import os
#
# from screenTwo import scene_2
#
# init()
# pygame.init()
#
#
# class Main2:
#     def start_game(self):
#         main = Main()
#         main.mainloop()
# main2 = Main2()
#
#
# class Scene1:
#     def __init__(self):
#         self._option_surfaces = []
#         self._callbacks = []
#         self._current_options_index = 0
#         pygame.display.set_caption('Menu of MEGA TIC TAC TOE')
#
#
#     # Добавление опций
#     def append_options(self, option, callback):
#         self._option_surfaces.append(ARIAL_50.render(option, True, (255,255,255)))
#         self._callbacks.append(callback)
#
#
#     # Проверка выбранного пункта
#     def switch(self, direction):
#         self._current_options_index = max(0, min(self._current_options_index + direction, len(self._option_surfaces) - 1))
#
#     def select(self):
#         self._callbacks[self._current_options_index]()
#
#     # Отрисовка меню и его выбор
#     def draw_menu(self, surf, x, y, option_y_padding):
#         for i, option in enumerate(self._option_surfaces):
#             option_rect = option.get_rect()
#             option_rect.topleft = (x, y + i * option_y_padding)
#             if i == self._current_options_index:
#                 draw.rect(surf, (48, 213, 200), option_rect)
#             surf.blit(option, option_rect)
#
#     # Показ меню пользователю
#     def show_menu(self):
#         menuFirst.append_options('Play', main2.start_game)
#         menuFirst.append_options('Rules', scene_2) #os.system('screenTwo.py')
#         #menuFirst.append_options('Rules', lambda: print('Нажатие'))  # os.system('screenTwo.py')
#         #rules_button = menu.append_options('Rules', lambda : print('Нажатие'))
#         menuFirst.append_options('Quit', quit)
#
#
#     def print_text(self):
#     # Создание объекта текста
#         font = pygame.font.Font(None, 40) # Создание шрифта с размером 40
#         font2 = pygame.font.Font(None, 25) # Создание шрифта с размером 25
#
#     # Рендеринг текста (сам текст, антиалиасинг, цвет)
#         text = font.render("Добро пожаловать в МЕГА кретстики нолики!", True, (255, 255, 255))
#         text2 = font2.render("Чтобы передвигаться по меню используй W и S, а для выбора нажми E", True, (255, 255, 255))
#
#
#         # Отображение первого текста на экране
#         text_rect = text.get_rect()
#         text_rect.center = (size[0] // 2, size[1] - (size[1] - 50))  # Расположение текста на экране
#         screen.blit(text, text_rect)
#
#         # Отображение второго текста на экране
#         text2_rect = text.get_rect()
#         text2_rect.center = (size[0] // 2 + 8, size[1] - (size[1] - 90))
#         screen.blit(text2, text2_rect)
#
# class Scene2:
#     def __init__(self):
#         self._option_surfaces = []
#         self._callbacks = []
#         self._current_options_index = 0
#         pygame.display.set_caption('RULES')
#
#     def append_options2(self, option, callback):
#         self._option_surfaces.append(ARIAL_50.render(option, True, (255, 255, 255)))
#         self._callbacks.append(callback)
#
#     def select(self):
#         self._callbacks[self._current_options_index]()
#
#     def draw_menu2(self, surf, x, y, option_y_padding):
#         for i, option in enumerate(self._option_surfaces):
#             option_rect = option.get_rect()
#             option_rect.topleft = (x, y + i * option_y_padding)
#             if i == self._current_options_index:
#                 draw.rect(surf, (48, 213, 200), option_rect)
#             surf.blit(option, option_rect)
#
#     # Показ меню пользователю
#     def show_menu2(self):
#         menuTwo.append_options2('Back to menu', lambda: print("Тут будет кнопка обратно")) #os.system('screenOne.py'))#)
#
#     # Создание объекта текста
#     def print_text2(self):
#         font = pygame.font.Font(None, 40) # Создание шрифта с размером 40
#         font2 = pygame.font.Font(None, 25) # Создание шрифта с размером 25
#
#         # Рендеринг текста (сам текст, антиалиасинг, цвет)
#         text = font.render("Правила:", True, (255, 255, 255))
#         text2 = font2.render("  Это МЕГА крестики нолик, тут после хода одного из игроков на маленьком поле игра  ",True, (255, 255, 255))
#         text3 = font2.render("    перемещается в большое поле, соответсвующее тому, на которое игрок поставил     ",True, (255, 255, 255))
#         text4 = font2.render("крестик/нолик. После победы одного из игроков на маленьком поле, это поле становится",True, (255, 255, 255))
#         text5 = font2.render("недоступным, а при обращении к нему, следующий игрок может выбрать любое доступное  ",True, (255, 255, 255))
#         text6 = font2.render("     поле для хода. Побеждает игрок, первый собравший комбинацию из классчиеских    ",True, (255, 255, 255))
#         text7 = font2.render("                   крестиков-ноликов, но из выигранных полей.                       ",True, (255, 255, 255))
#         text8 = font2.render("    Справка: нажмите R во время игры чтобы перезапустить и Q чтобы выйти. Удачи!    ",True, (255, 255, 255))
#
#         # Отображение первого текста на экране
#         text_rect = text.get_rect()
#         text_rect.center = (size[0] // 2, size[1] - (size[1] - 50))  # Расположение текста на экране
#         screen.blit(text, text_rect)
#
#         otstup = size[0] - (size[0] - 80)
#         # Отображение второго текста на экране и т.д
#         text2_rect = text.get_rect()
#         text2_rect.center = (otstup, size[1] - (size[1] - 90))
#         screen.blit(text2, text2_rect)
#         text3_rect = text.get_rect()
#         text3_rect.center = (otstup - 20, size[1] - (size[1] - 120))
#         screen.blit(text3, text3_rect)
#
#         text4_rect = text.get_rect()
#         text4_rect.center = (otstup, size[1] - (size[1] - 150))
#         screen.blit(text4, text4_rect)
#
#         text5_rect = text.get_rect()
#         text5_rect.center = (otstup, size[1] - (size[1] - 180))
#         screen.blit(text5, text5_rect)
#
#         text6_rect = text.get_rect()
#         text6_rect.center = (otstup, size[1] - (size[1] - 210))
#         screen.blit(text6, text6_rect)
#
#         text7_rect = text.get_rect()
#         text7_rect.center = (otstup + 100, size[1] - (size[1] - 240))
#         screen.blit(text7, text7_rect)
#
#         text8_rect = text.get_rect()
#         text8_rect.center = (otstup, size[1] - (size[1] - 400))
#         screen.blit(text8, text8_rect)
#
# menuFirst = Scene1()
# menuFirst.show_menu()
#
# menuTwo = Scene2()
# menuTwo.show_menu2()
#
#
#
