import pygame


class Text:
    def __init__(self, data, size, x=0, y=0, color=(48, 213, 200)):
        self.position = (x, y)
        self.data = data
        self.size = size
        self.color = color
        self.font = pygame.font.Font('Dpix_8pt.ttf', self.size)
        self.surface = self.font.render(self.data, True, self.color)

    def update_position(self, x, y):
        self.position = (x, y)

    def update_text(self, text):
        self.data = str(text)
        self.surface = self.font.render(self.data, True, self.color)

    def get_text_size(self):
        r = self.surface.get_rect()
        return [r.width, r.height]

    def draw(self, screen):
        screen.blit(self.surface, self.position)



#if __name__ == '__main__':