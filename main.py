import sys

from const import *
from game import Game
from menu_perf import main_menu
from rules import rules_table



def mainloop(screen):
    pygame.display.set_caption('MEGA TIC TAC TOE')
    game = Game(ultimate=True, max=False)

    screen.fill( BG_COLOR )
    game.render_board(screen)

    available_xfields = range(0, 729)
    available_yfields = range(0, 729)
    played_xpos = []
    played_ypos = []
    marked = []
    draw_fields = []

    running = True
    while running:

        for event in pygame.event.get():
            # клик
            if event.type == pygame.MOUSEBUTTONDOWN and game.playing:
                xclick, yclick = event.pos

                isDraw, rem = game.board.is_draw(marked)
                if isDraw:

                    #проверка на то, какое поле в ничье последнее, если обращение
                    #к ничье, выполняется это
                    available_xfields = range(0, 729)
                    available_yfields = range(0, 729)

                    played_ypos = game.board.get_yplayed_positions()
                    played_xpos = game.board.get_xplayed_positions()

                    for j in range(9):
                        ind = marked.index(rem)
                        marked.pop(ind)
                        marked.pop(ind + 1)

                for i in range(len(played_xpos)):
                    if (played_xpos[i] in available_xfields and played_ypos[i] in available_yfields):
                        available_xfields = range(0, 729)
                        available_yfields = range(0, 729)
            
                if xclick not in available_xfields:
                    break
                if yclick not in available_yfields:
                    break


                if game.board.valid_sqr(xclick, yclick):
                    game.board.mark_sqr(xclick, yclick, game.player, marked)
                    game.board.draw_fig(screen, xclick, yclick)

                    played_ypos = game.board.get_yplayed_positions()
                    played_xpos = game.board.get_xplayed_positions()

                    winner = game.board.check_draw_win(screen)
                    # ultimate winner
                    if winner:
                        game.board.manage_win(screen, winner, onmain=True)
                        game.ultimate_winner(screen, winner)

                    must_field_c = game.board.determine_must_field_c(xclick)
                    must_field_r = game.board.determine_must_field_r(yclick)

                    if game.board.squares[must_field_r][must_field_c] not in (1, 2):
                        available_xfields = range(must_field_c * 243, (must_field_c + 1) * 243)
                        available_yfields = range(must_field_r * 243, (must_field_r + 1) * 243)
                    else:
                        available_xfields = range(0, 729)
                        available_yfields = range(0, 729)

                    game.next_turn()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    available_xfields = range(0, 729)
                    available_yfields = range(0, 729)
                    game.restart()
                    screen.fill( BG_COLOR )
                    game.render_board(screen)
                elif event.key == pygame.K_q:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    main_menu(screen, mainloop, rules_table)
                    #pygame.quit()
                    #sys.exit()

            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    main_menu(screen, mainloop, rules_table)
