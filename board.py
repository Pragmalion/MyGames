from const import *
from board_dim import BoardDim

xplayed = []
yplayed = []


class Board:
    
    def __init__(self, dims=None, linewidth=15, ultimate=False, max=False):
        self.squares = [ [0, 0, 0] for row in range(DIM)]
        self.dims = dims

        if not dims: 
            self.dims = BoardDim(WIDTH, 0, 0)

        self.linewidth = linewidth
        self.offset = self.dims.sqsize * 0.2
        self.radius = (self.dims.sqsize // 2) * 0.7
        self.max = max

        if ultimate: 
            self.create_ultimate()

        self.active = True

    def __str__(self):
        s = ''
        for row in range(DIM):
            for col in range(DIM):
                sqr = self.squares[row][col]
                s += str(sqr)
        return s

    def create_ultimate(self):
        for row in range(DIM):
            for col in range(DIM):

                size = self.dims.sqsize
                xcor, ycor = self.dims.xcor + (col * self.dims.sqsize), self.dims.ycor + (row * self.dims.sqsize)
                dims = BoardDim(size=size, xcor=xcor, ycor=ycor)
                linewidth = self.linewidth - 7
                ultimate = self.max

                self.squares[row][col] = Board(dims=dims, linewidth=linewidth, ultimate=ultimate, max=False)
    
    def render(self, surface):
        for row in range(DIM):
            for col in range(DIM):
                sqr = self.squares[row][col]

                if isinstance(sqr, Board): sqr.render(surface)
        
        # vertical lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor + self.dims.sqsize, self.dims.ycor),                  (self.dims.xcor + self.dims.sqsize, self.dims.ycor + self.dims.size), self.linewidth)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor + self.dims.size - self.dims.sqsize, self.dims.ycor), (self.dims.xcor + self.dims.size - self.dims.sqsize, self.dims.ycor + self.dims.size), self.linewidth)
        
        # horizontal lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.ycor + self.dims.sqsize),                  (self.dims.xcor + self.dims.size, self.dims.ycor + self.dims.sqsize), self.linewidth)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.ycor + self.dims.size - self.dims.sqsize), (self.dims.xcor + self.dims.size, self.dims.ycor + self.dims.size - self.dims.sqsize), self.linewidth)

    def valid_sqr(self, xclick, yclick):

        row = yclick // self.dims.sqsize
        col = xclick // self.dims.sqsize

        if row > 2: row %= DIM
        if col > 2: col %= DIM

        sqr = self.squares[row][col]

        # base case
        if not isinstance(sqr, Board):
            return sqr == 0 and self.active

        # recursive step
        return sqr.valid_sqr(xclick, yclick)

    def mark_sqr(self, xclick, yclick, player, marked):
        
        row = yclick // self.dims.sqsize
        col = xclick // self.dims.sqsize

        if row > 2: row %= DIM
        if col > 2: col %= DIM

        sqr = self.squares[row][col]

        print('marking -> (', row, col, ')')

        marked.append((row, col))


        if not isinstance(sqr, Board):
            self.squares[row][col] = player
            return

        sqr.mark_sqr(xclick, yclick, player, marked)

    def determine_must_field_c(self, xposition):
        
        if xposition < 243:
            if xposition < 81:
                return 0
            if xposition < 162:
                return 1
            return 2
        
        elif xposition < 486:
            if xposition < 243 + 81:
                return 0
            if xposition < 243 + 162:
                return 1
            return 2
        
        else:
            if xposition < 486 + 81:
                return 0
            if xposition < 486 + 162:
                return 1
            return 2
    
    def determine_must_field_r(self, yposition):
        if yposition < 243:
            if yposition < 81:
                return 0
            if yposition < 162:
                return 1
            return 2
        
        elif yposition < 486:
            if yposition < 243 + 81:
                return 0
            if yposition < 243 + 162:
                return 1
            return 2
        
        else:
            if yposition < 486 + 81:
                return 0
            if yposition < 486 + 162:
                return 1
            return 2

    # Орисовка фигур
    def draw_fig(self, surface, xclick, yclick):
        row = yclick // self.dims.sqsize
        col = xclick // self.dims.sqsize

        if row > 2: row %= DIM
        if col > 2: col %= DIM

        sqr = self.squares[row][col]

        if not isinstance(sqr, Board):

            # Крестик
            if sqr == 1:
                # первая диагональ
                ipos = (self.dims.xcor + (col * self.dims.sqsize) + self.offset, 
                        self.dims.ycor + (row * self.dims.sqsize) + self.offset)
                fpos = (self.dims.xcor + self.dims.sqsize * (1 + col) - self.offset, 
                        self.dims.ycor + self.dims.sqsize * (1 + row) - self.offset)
                pygame.draw.line(surface, CROSS_COLOR, ipos, fpos, self.linewidth)

                # вторая диагональ
                ipos = (self.dims.xcor + (col * self.dims.sqsize) + self.offset, 
                        self.dims.ycor + self.dims.sqsize * (1 + row) - self.offset)
                fpos = (self.dims.xcor + self.dims.sqsize * (1 + col) - self.offset, 
                        self.dims.ycor + (row * self.dims.sqsize) + self.offset)
                pygame.draw.line(surface, CROSS_COLOR, ipos, fpos, self.linewidth)


            
            # Нолик
            elif sqr == 2:
                center = (self.dims.xcor + self.dims.sqsize * (0.5 + col),
                          self.dims.xcor + self.dims.sqsize * (0.5 + row))

                pygame.draw.circle(surface, CIRCLE_COLOR, center, self.radius, self.linewidth)

            elif sqr == 3:
                #рисование ничьи
                pygame.draw.line(surface, DRAW_COLOR, self.dims.xcor + self.dims.sqsize,self.dims.xcor + self.dims.sqsize)
                #return

            return

        # рекурсивный шаг
        sqr.draw_fig(surface, xclick, yclick)

    def get_xplayed_positions(self):
        return xplayed
    def get_yplayed_positions(self):
        return yplayed

    def manage_win(self, surface, winner, onmain=False):
        # Прозрачный экран
        transparent = pygame.Surface( (self.dims.size, self.dims.size) )
        transparent.set_alpha( ALPHA )
        transparent.fill( FADE )
        if onmain:
            surface.blit(transparent, (self.dims.xcor, self.dims.ycor))
            surface.blit(transparent, (self.dims.xcor, self.dims.ycor))
        surface.blit(transparent, (self.dims.xcor, self.dims.ycor))
        
        # Отрисовка победы
        if not onmain:
            # Крестик
            if winner == 1:
                # первая диагональ
                ipos = (self.dims.xcor + self.offset, 
                        self.dims.ycor + self.offset)
                fpos = (self.dims.xcor + self.dims.size - self.offset, 
                        self.dims.ycor + self.dims.size - self.offset)
                
                xplayed.append(range(int(ipos[0]), int(fpos[0])))
                yplayed.append(range(int(ipos[1]), int(fpos[1])))
                
                pygame.draw.line(surface, CROSS_COLOR, ipos, fpos, self.linewidth + 7)

                # вторая диагональ
                ipos = (self.dims.xcor + self.offset, 
                        self.dims.ycor + self.dims.size - self.offset)
                fpos = (self.dims.xcor + self.dims.size - self.offset, 
                        self.dims.ycor + self.offset)
                xplayed.append(range(int(ipos[0]), int(fpos[0])))
                yplayed.append(range(int(ipos[1]), int(fpos[1])))
                pygame.draw.line(surface, CROSS_COLOR, ipos, fpos, self.linewidth + 7)

            # Нолик
            if winner == 2:
                center = (self.dims.xcor + self.dims.size * 0.5,
                        self.dims.ycor + self.dims.size * 0.5)

                pygame.draw.circle(surface, CIRCLE_COLOR, center, self.dims.size * 0.4, self.linewidth + 7)
                

        # неактивное поле
        self.active = False

    def is_draw(self, marked):
        flag = False
        marked = marked[::2]
        ret = 0

        for i in range(0, len(marked)):
            if (marked.count(marked[i]) == 9):
                
                # вот тут в неиграбельные поля не добавляются
                xplayed.append((marked[i][0] * 243, marked[i][0] * 243 + 243))
                yplayed.append((marked[i][-1] * 243, marked[i][-1] * 243 + 243))

                flag = True
                ret = marked[i]
        return flag, ret
    
    def check_draw_win(self, surface, ):

        isfull = True

        for row in range(DIM):
            for col in range(DIM):

                sqr = self.squares[row][col]

                if isinstance(sqr, Board) and sqr.active:
                    # other board win
                    winner = sqr.check_draw_win(surface)
                    if winner: # recursive step
                        self.squares[row][col] = winner
                        sqr.manage_win(surface, winner)


                # main
                # Вертикальная победа
                for c in range(DIM):
                    if self.squares[0][c] == self.squares[1][c] == self.squares[2][c] != 0:
                        color = CROSS_COLOR if self.squares[0][c] == 1 else CIRCLE_COLOR
                        # draw win
                        ipos = (self.dims.xcor + self.dims.sqsize * (0.5 + c), 
                                self.dims.ycor + self.offset)
                        fpos = (self.dims.xcor + self.dims.sqsize * (0.5 + c), 
                                self.dims.ycor + self.dims.size - self.offset)
                        pygame.draw.line(surface, color, ipos, fpos, self.linewidth)

                        return self.squares[0][c]

                # Горизонатльная победа
                for r in range(DIM):
                    if self.squares[r][0] == self.squares[r][1] == self.squares[r][2] != 0:
                        color = CROSS_COLOR if self.squares[r][0] == 1 else CIRCLE_COLOR
                        # draw win
                        ipos = (self.dims.xcor + self.offset, 
                                self.dims.ycor + self.dims.sqsize * (r + 0.5))
                        fpos = (self.dims.xcor + self.dims.size - self.offset, 
                                self.dims.ycor + self.dims.sqsize * (r + 0.5))
                        pygame.draw.line(surface, color, ipos, fpos, self.linewidth)

                        return self.squares[r][0]

                # диагональная победа
                # диагональ 1
                if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
                    color = CROSS_COLOR if self.squares[1][1] == 1 else CIRCLE_COLOR
                    # draw win
                    ipos = (self.dims.xcor + self.offset, 
                            self.dims.ycor + self.offset)
                    fpos = (self.dims.xcor + self.dims.size - self.offset, 
                            self.dims.ycor + self.dims.size - self.offset)
                    pygame.draw.line(surface, color, ipos, fpos, self.linewidth)

                    return self.squares[1][1]

                # диагональ 2
                if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
                    color = CROSS_COLOR if self.squares[1][1] == 1 else CIRCLE_COLOR
                    # draw win
                    ipos = (self.dims.xcor + self.offset, 
                            self.dims.ycor + self.dims.size - self.offset)
                    fpos = (self.dims.xcor + self.dims.size - self.offset, 
                            self.dims.ycor + self.offset)
                    pygame.draw.line(surface, color, ipos, fpos, self.linewidth)

                    return self.squares[1][1]