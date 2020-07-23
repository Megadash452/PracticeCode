import pygame


pygame.init()


win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))


checked1 = False


class checkbox:
    def __init__(self, x_pos, y_poss, width, height, color, hover_color, checked_color, checked, active_):
        self.x_pos = x_pos
        self.y_pos = y_poss
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.checked_color = checked_color
        self.checked = checked
        self.active_ = active_
        pygame.draw.rect(win, self.color, (self.x_pos, self.y_pos, self.width, self.height))

    def active(self):
        if self.active_:
            if self.x_pos < pygame.mouse.get_pos()[0] < self.x_pos + self.width \
                    and self.y_pos < pygame.mouse.get_pos()[1] < self.y_pos + self.height:
                pygame.draw.rect(win, self.hover_color, (self.x_pos, self.y_pos, self.width, self.height))
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.rect(win, self.checked_color, (self.x_pos, self.y_pos, self.width, self.height))
                    global checked1
                    checked1 = not checked1
            return checked1
        else:
            return False


run = True
while run:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    win.fill((0, 50, 50))

    box = checkbox(int(win_width / 2), int(win_height / 2),
             24, 24, (200, 200, 200), (255, 255, 255), (0, 200, 0), checked1, True)
    if box.active():
        pass

    pygame.display.update()

pygame.quit()
