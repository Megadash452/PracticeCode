import json
import pygame

# import ctypes

pygame.init()

# --- Data ---
try:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
except FileNotFoundError:
    with open('settings.json', 'w') as f:
        write = {
            'resolution': {
                'width': 800,
                'height': 500,
                'isFullscreen': False
            }
        }
        json.dump(write, f)
# ---

# --- Window Properties ---
is_fullscreen = settings['resolution']['isFullscreen']
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
if is_fullscreen:
    win = pygame.display.set_mode((monitor_size[0], monitor_size[1]), pygame.FULLSCREEN)
else:
    win = pygame.display.set_mode((settings['resolution']['width'], settings['resolution']['height']), pygame.RESIZABLE)

win_width = win.get_width()
win_height = win.get_height()
pygame.display.set_caption('Game')
# --- ---

# --- Menu Visuals ---
border_margin = 50
# --- ---

# --- Sprites and other images
# crosshair = pygame.image.load('Cross-hair.png')
# --- ---

pygame.mouse.set_pos(int(win_width / 2), int(win_height / 2))


# pygame.mouse.set_visible(False)


def clip(surf, x, y, width, height):
    handle_surf = surf.copy()
    clip_ = pygame.Rect(x, y, width, height)
    handle_surf.set_clip(clip_)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


class file:
    """For the count_instances method, remember to include the
       phrase inside square brackets when calling the method.
        e.g.: count_instances('savedata.txt, ['new'])"""

    def __init__(self, name, phrase):
        self.name = name
        self.phrase = phrase

    def available_(self):
        try:
            with open(self.name, 'r') as f1:
                f1.read()
            return True
        except FileNotFoundError:
            return False

    def count_instances(self):
        try:
            with open(self.name, 'r') as f2:
                read = f2.readlines()

                for inst in self.phrase:
                    lower = inst.lower()
                    inst_count = 0
                    for sentence in read:
                        line = sentence.split()
                        for each in line:
                            alt_line = each.lower()
                            alt_line = alt_line.strip('!')
                            if lower == alt_line:
                                inst_count += 1
                    return inst_count

        except FileNotFoundError:
            create_ = input('File does not exist. Do you want to create one?')
            if create_ == 'no' or str(0):
                print('File not created')

    def where(self):
        with open(self.name, 'r') as f3:
            s = True
            count = 1
            while s:
                s = f3.readline()
                line = s.split()
                if self.phrase in line:
                    print('line number: ' + str(count) + ': ' + s)
                count += 1
        return count


class Font:
    """This class will allow you to write text into a pygame surface when called.
       I highly recommend you to use your own set of fonts if you are using this class.
       Also, the font file must be a picture, such as a PNG or JPEG.
       Size Scaling not available"""

    def __init__(self, path):
        self.spacing = 1
        self.character_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                '.', '-', ',', ':', '+', '\'', '!', '?',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                '(', ')', '/', '_', '=', '\\', '[', ']', '*', '"', '<', '>', ';']
        font_img = pygame.image.load(path).convert()
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def write(self, surf, text, loc):
        x_offset = 0
        for char in text:
            if char != ' ':
                surf.blit(self.characters[char], (loc[0] + x_offset, loc[1]))
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing


game_font = Font('small_font.png')
game_font_height = 8


class background_object:
    """These Background Objects will have a hit-box, though it
       is not necessary to use it. Argument to disable hit-box
       will be added in the future."""

    def __init__(self, txt, x_pos, y_poss, width, height, color):
        self.txt = txt
        self.x_pos = x_pos
        self.y_pos = y_poss
        self.width = width
        self.height = height
        self.color = color
        pygame.draw.rect(win, self.color, (self.x_pos, self.y_pos, self.width, self.height))
        game_font.write(win, self.txt, (int(self.x_pos + self.width / 2 - len(self.txt * 2)), int(self.y_pos + self.height / 2 - game_font_height / 2)))


class button(background_object):
    """Remember that active_ should result in a Boolean. If you
       chose to make a button inactive (by making the active_
       argument False), you should make the color of the button
       at least 10 less."""

    def __init__(self, txt, x_pos, y_pos, width, height, color, hover_color, clicked_color, active_):
        super().__init__(txt, x_pos, y_pos, width, height, color)
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.active_ = active_

    def active(self):
        if self.active_:
            clicked = False
            if self.x_pos < pygame.mouse.get_pos()[0] < self.x_pos + self.width \
                    and self.y_pos < pygame.mouse.get_pos()[1] < self.y_pos + self.height:
                pygame.draw.rect(win, self.hover_color, (self.x_pos, self.y_pos, self.width, self.height))
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.rect(win, self.clicked_color, (self.x_pos, self.y_pos, self.width, self.height))
                    clicked = True
            return clicked
        else:
            return False

    def inactive(self):
        pass


class checkbox(background_object):
    def __init__(self, txt, x_pos, y_pos, width, height, color, checked_color, checked, active_):
        super().__init__(txt, x_pos, y_pos, width, height, color)
        self.checked_color = checked_color
        self.checked = checked
        self.active_ = active_
        if self.checked:
            pygame.draw.rect(win, self.checked_color, (self.x_pos, self.y_pos, self.width, self.height))
        else:
            pygame.draw.rect(win, self.color, (self.x_pos, self.y_pos, self.width, self.height))

    def active(self):
        if self.active_:
            clicked = False
            if self.x_pos < pygame.mouse.get_pos()[0] < self.x_pos + self.width \
                    and self.y_pos < pygame.mouse.get_pos()[1] < self.y_pos + self.height:
                if pygame.mouse.get_pressed()[0]:
                    clicked = True
            return clicked
        else:
            return False


# \-----------------------------------------------------------------------\


def main_menu():
    title = background_object('game', int(border_margin), int(border_margin),
                              int(400), int(75),
                              (255, 255, 255))

    start = button('New Game', int(border_margin), int(title.height + border_margin * 3),
                   int(200), int(75),
                   (255, 255, 255), (255, 0, 0), (0, 255, 0), True)
    if start.active():
        global screen
        screen = 'new game'

    load_file = button('Load', int(border_margin), int(start.y_pos + start.height + border_margin),
                       int(160), int(75),
                       (255, 255, 255), (255, 0, 0), (0, 255, 0), True)  # save_file.available_()
    if load_file.active():
        screen = 'load menu'

    settings_btn = button('Settings', int(win_width - border_margin - 64), int(win_height - border_margin - 64),
                          int(64), int(64),
                          (255, 255, 255), (255, 0, 0), (0, 255, 0), True)
    if settings_btn.active():
        screen = 'settings'


def new_game():
    back_button = button('Back', int(border_margin), int(win_height - border_margin - 64),
                         int(96), int(64),
                         (255, 255, 255), (255, 0, 0), (0, 255, 0), True)
    if back_button.active():
        global screen
        screen = 'main menu'


def load_menu():
    title = background_object('Load', int(border_margin), int(border_margin),
                              400, 75,
                              (255, 255, 255))

    load1 = button('1', int(border_margin * 2), int(border_margin * 3 + title.height),
                   int((win_width - border_margin * 6) / 3), int(win_height - border_margin * 6 - title.height - 64),
                   (255, 255, 255), (0, 0, 255), (0, 255, 0), True)
    if load1.active():
        pass

    load2 = button('2', int(load1.x_pos + load1.width + border_margin), int(load1.y_pos),
                   int((win_width - border_margin * 6) / 3), int(load1.height),
                   load1.color, load1.hover_color, load1.clicked_color, True)
    if load2.active():
        pass

    load3 = button('3', int(load2.x_pos + load2.width + border_margin), int(load1.y_pos),
                   int((win_width - border_margin * 6) / 3), int(load1.height),
                   load1.color, load1.hover_color, load1.clicked_color, True)
    if load3.active():
        pass

    back_button = button('Back', int(border_margin), int(win_height - border_margin - 64),
                         96, 64,
                         (255, 255, 255), (255, 0, 0), (0, 255, 0), True)
    if back_button.active():
        global screen
        screen = 'main menu'


def settings_menu():
    title = background_object('Settings', int(border_margin), int(border_margin),
                              int(400), int(75),
                              (255, 255, 255))
    back_button = button('Back', int(border_margin), int(win_height - border_margin - 64),
                         int(96), int(64),
                         (255, 255, 255), (255, 0, 0), (0, 255, 0), True)
    if back_button.active():
        global screen
        screen = 'main menu'

    res_box = background_object('gie', int(win_width / 2 - 132), int(border_margin * 2 + title.height),
                                264, 64,
                                (200, 200, 200))

    res_reduce = button('<', int(res_box.x_pos - 64 - 10), int(res_box.y_pos),
                        64, 64,
                        (255, 255, 255), (200, 200, 200), (150, 150, 150), True)
    if res_reduce.active():
        if settings['resolution']['width'] > 800:
            settings['resolution']['width'] -= 50
        if settings['resolution']['height'] > 500:
            settings['resolution']['height'] -= 50
        with open('settings.json', 'w') as f4:
            json.dump(settings, f4)

    res_increase = button('>', int(res_box.x_pos + res_box.width + 10), int(res_box.y_pos),
                          64, 64,
                          (255, 255, 255), (200, 200, 200), (150, 150, 150), True)
    if res_increase.active():
        if settings['resolution']['width'] < monitor_size[0]:
            settings['resolution']['width'] += 50
        if settings['resolution']['height'] < monitor_size[1]:
            settings['resolution']['height'] += 50
        with open('settings.json', 'w') as f5:
            json.dump(settings, f5)

    flscrn = checkbox('.', int(res_increase.x_pos + res_increase.width + 10),
                      int(res_increase.y_pos + res_increase.height / 2 - 25 / 2),
                      25, 25,
                      (225, 225, 225), (0, 255, 0), is_fullscreen, True)
    if flscrn.active():
        settings['resolution']['isFullscreen'] = not settings['resolution']['isFullscreen']
        with open('settings.json', 'w') as f6:
            json.dump(settings, f6)


def redrawGameWindow():
    # win.blit(crosshair, (pygame.mouse.get_pos()[0] - 15, pygame.mouse.get_pos()[1] - 15))
    pygame.display.update()


run = True
save_file = file('', '')
screens = {
    1: main_menu(),
    2: settings_menu(),
    3: load_menu(),
    4: new_game()
}
screen = 'main menu'
while run:
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            if not is_fullscreen:
                win_width = event.w
                win_height = event.h
                win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.QUIT:
            if screen == 'in game':
                print('Do you wish to save?')
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_F11]:
        is_fullscreen = not is_fullscreen
        if is_fullscreen:
            win_width = monitor_size[0]
            win_height = monitor_size[1]
            pygame.display.set_mode((monitor_size[0], monitor_size[1]), pygame.FULLSCREEN)
        else:
            win = pygame.display.set_mode((settings['resolution']['width'], settings['resolution']['height']),
                                          pygame.RESIZABLE)

    win.fill((0, 50, 50))

    if screen == 'main menu':
        main_menu()

    elif screen == 'settings':
        settings_menu()

    elif screen == 'new game':
        new_game()

    elif screen == 'load menu':
        load_menu()

    redrawGameWindow()

pygame.quit()
