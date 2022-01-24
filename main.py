from tkinter import *

import os
import pygame
from apple import *
from setting import *
from pygame.locals import *
from snake import Snake

os.environ['SDL_VIDEO_CENTERED'] = '1'  # помещение в центр экрана


class StartScreen:
    """    Класс, отвечающий за вывод на экран стартового интерфейса    """

    def __init__(self):
        global intro
        # Загрузка изображения названия игры и расположение на экране
        image = load_image(fonn)
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = W // 3 - image.get_width() // 2
        sprite.rect.y = 0

    def print_text(self):
        """        Вывод текста стартового окна        """
        for i in range(len(intro)):
            if intro[i][1] == 0:
                color = pygame.Color("white")
            else:
                color = pygame.Color("yellow")
            font = pygame.font.Font(None, 50)
            text = font.render(intro[i][0], 1, (color))
            start_x = W // 2 - text.get_width() // 2
            start_y = H // 2 + text.get_height() // 2 + 90
            text_x = start_x
            text_y = start_y + i * 50
            screen.blit(text, (text_x, text_y))


def start_screen_on():
    """    Стартовый интерфейс    """
    global mouse_on_screen
    pygame.mouse.set_visible(False)
    while True:
        show_start_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEMOTION:
                change_text_start(event.pos)
                if pygame.mouse.get_focused():
                    change_place(event.pos)
                    mouse_on_screen = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:
                # Кнопка "Начать игру"
                if f1:
                    return
                # Кнопка "Таблица рекордов"
                elif f2:
                    record_menu()
                    return
                #  Кнопка "Выход"
                elif f3:
                    terminate()
        pygame.display.flip()


def record_menu(end=False):
    """     Меню рекордов     """
    global mouse_on_screen, mouse_on_screen
    color_back = pygame.Color("white")
    f4 = False
    file_path = os.path.join('results.txt')
    file_records = open(file_path, mode='r')
    data = file_records.readlines()
    file_records.close()

    while True:
        if end:
            show_record_menu(data, color_back, True)
        else:
            show_record_menu(data, color_back)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                if 50 <= event.pos[0] <= 170 and 450 <= event.pos[1] <= 500:
                    color_back = pygame.Color("yellow")
                else:
                    color_back = pygame.Color("white")
                if end:
                    show_record_menu(data, color_back, True)
                else:
                    show_record_menu(data, color_back)
                if pygame.mouse.get_focused():
                    change_place(event.pos)
                    mouse_on_screen = event.pos

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= event.pos[0] <= 170 and 450 <= event.pos[1] <= 500:
                    start_screen_on()
                    return
        pygame.display.flip()


def show_record_menu(data, color, end=False):
    """     Отрисовка меню рекордов     """
    global mouse_on_screen
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 45)

    pygame.draw.rect(screen, pygame.Color("white"),
                     ([10, 10],
                      [500, 300]), 5)
    pygame.draw.line(screen, pygame.Color("white"), [250, 10], [250, 305], 5)
    if data:
        data_1 = data[:4]
        for i in range(len(data_1)):
            line = data_1[i]
            pos_1 = (50, 60 + i * 70)
            pos_2 = (300, 60 + i * 70)
            line = line.strip('\n').split()
            line[0], line[1] = line[1], line[0]

            string_rendered = font.render(line[0], 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect().move(pos_2)
            screen.blit(string_rendered, intro_rect)

            string_rendered = font.render(line[1], 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect().move(pos_1)
            screen.blit(string_rendered, intro_rect)

    string_rendered = font.render('Назад', 1, color)
    intro_rect = string_rendered.get_rect().move(100, 450)
    screen.blit(string_rendered, intro_rect)


def controls_screen():
    """     Обработка действий с окном управления    """
    global mouse_on_screen, f4, color_back
    while True:
        for event in pygame.event.get():
            # Выход из игры
            if event.type == pygame.QUIT:
                terminate()
                # Изменение цвета кнопки "Назад" при наведении
                x, y = event.pos
                if 100 <= x <= 100 + 125 and 450 <= y <= 450 + 61 and not f4:
                    color_back = 1
                    f4 = True
                elif f4 and not (100 <= x <= 100 + 125 and 450 <= y <= 450 + 61 and not f4):
                    color_back = 0
                    f4 = False
                # Обработка движения курсора
                if pygame.mouse.get_focused():
                    change_place(event.pos)
                    mouse_on_screen = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:
                # Возвращение в главный экран
                if f4:
                    start_screen_on()
                    return
        pygame.display.flip()


def change_place(pos):
    """    Изменение положения курсора //позиция курсора в данный момент    """
    image = load_image(cursor)
    screen.blit(image, (pos[0], pos[1]))


def change_text_start(pos):
    """    Изменение цвета текста меню при наведении курсором    """
    global f1, f2, f3, intro
    x, y = pos
    # Изменение цвета "Начать игру"
    if 251 <= x <= 364 and 344 <= y <= 369 and not f1:
        intro[0][1] = 1
        f1 = True
    elif f1 and not (251 <= x <= 364 and 344 <= y <= 369):
        intro[0][1] = 0
        f1 = False
    # Изменение цвета "Таблица рекордов"
    elif 142 <= x <= 466 and 397 <= y <= 419 and not f2:
        intro[1][1] = 1
        f2 = True
    elif f2 and not (142 <= x <= 466 and 397 <= y <= 419):
        intro[1][1] = 0
        f2 = False
    # Изменение цвета "Выход"
    elif 250 <= x <= 368 and 449 <= y <= 478 and not f3:
        intro[2][1] = 1
        f3 = True
    elif f3 and not (250 <= x <= 368 and 449 <= y <= 478):
        intro[2][1] = 0
        f3 = False


def show_start_screen():
    """    Отрисовка всех элементов стартового интерфейса    """
    global mouse_on_screen
    fon = pygame.transform.scale(load_image(fonn), (W, H))
    screen.blit(fon, (0, 0))
    StartScreen.print_text(start)
    if mouse_on_screen and pygame.mouse.get_focused():
        change_place(mouse_on_screen)


def print_text(font, text, color, textpos=None):
    font = pygame.font.SysFont(font[0], font[1])
    text = font.render(text, 1, color)
    if textpos is None:
        textpos = text.get_rect(centerx=W / 2, centery=H / 2)
    screen.blit(text, textpos)


def draw_text():
    text = " Яблоки:{}      Баллы: {}        Жизни: {}".format(apple.count, snake.points, snake.lives)
    print_text(SCORE_FONT, text, BLACK, (10, 10))


def write_file():
    '''работа с файлом с рекордами'''
    try:
        f = open("results.txt", "r")
        n = f.read().count(player_name) + 1
        f.close()
    except FileNotFoundError:
        f = open("results.txt", "w")
        f.close()
        n = 0

    f = open("results.txt", "a")
    f.write("{} {} {} \n".format(player_name + str(n), apple.count, snake.points))
    f.close()


def draw_walls():
    for wall in walls_list:
        pygame.draw.rect(screen, pygame.Color("wheat"), wall, 0)


# ///////////////////стартовая страница//////////////////////////////////////////
def load_image(name, color_key=None):
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)

    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def terminate():
    pygame.quit()
    sys.exit


def countdown():
    global start, seconds
    pygame.time.wait(1000)
    screen.fill('wheat')
    print_text(LARGE_FONT, "{}".format(seconds), BLACK)
    seconds -= 1
    pygame.display.flip()


class Walls(object):
    def createList(self, size):
        '''создание рамок'''
        walls = []
        walls.append(pygame.Rect((0, 0), (W, size)))  # верхняя
        walls.append(pygame.Rect((W - size, 0), (size, H)))  # правая
        walls.append(pygame.Rect((0, H - size), (W, size)))  # нижняя
        walls.append(pygame.Rect((0, 0), (size, H)))  # левая
        return walls


def ate_apple():
    head = snake.body[0]
    head_rect = pygame.Rect((head[0] * cells, head[1] * cells, cells, cells))
    return head_rect.colliderect(apple.rect)


def popup(msg):
    popupwin = Tk()  # окно для ввода имени

    def center(win):  # размещение окна в центре
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry("+%d+%d" % (x, y))

    center(popupwin)

    def set_name(event=None):
        global player_name
        player_name = entry.get().strip()
        if not player_name:  # на случай отсутствия имени
            player_name = 'Player'
        popupwin.destroy()

    popupwin.title("!")
    label = Label(popupwin, text=msg, font=NORM_FONT)  # окно имени
    label.pack(side="top", fill="x", pady=10)
    entry = Entry(popupwin, width=15)  # ввод имени
    entry.pack()
    entry.insert(0, 'Player')
    entry.bind("<Return>", set_name)
    entry.focus_set()
    b1 = Button(popupwin, text="OK", command=set_name)
    b1.pack()
    popupwin.mainloop()


pygame.init()
pygame.display.set_icon(pygame.image.load(icon))
intro = [["Играть", 0],
         ["Таблица рекордов", 0],
         ["Выход", 0]]
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Змейка')
walls_list = Walls.createList(Walls(), cells)
snake = Snake(image)  # змея
f1, f2, f3, f4 = False, False, False, False
clock = pygame.time.Clock()
apple = Apple(cells)  # яблоки
start = False
game_over = False
seconds = 3  # отсчет времени


def main():
    global mouse_on_screen
    global start, game_over

    mouse_on_screen = None
    snake.draw(screen)  # появление змейки
    apple.draw(screen)  # появление яблочка
    draw_walls()  # появление стен
    draw_text()  # прорисовка меню

    # Начало игры
    start = StartScreen()
    start_screen_on()

    while seconds > 0:
        countdown()  # обратный отсчет
    start = True

    while True:  # основной цикл игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not game_over:
                    write_file()  # результаты в файл
                terminate()
                break
            elif event.type == KEYDOWN:  # определение движения
                snake.set_direction(event.key)
            elif event.type == KEYUP:
                snake.speed = 10
        '''обновление экрана'''
        fon = pygame.transform.scale(load_image(fon_igra), (W, H))
        screen.blit(fon, (0, 0))
        draw_walls()
        draw_text()
        snake.draw(screen)
        apple.draw(screen)

        if not game_over:
            snake.move()  # движение змейки

            if ate_apple():  # яблоко ам
                snake.points += apple.size
                apple.set_random_xy()  # позиция яблока
                Apple.count += 1
            else:
                snake.body.pop()

        if snake.hit_walls(walls_list):  # встреча со стенкой(((
            apple.set_random_xy()
            if snake.lives <= 0:
                game_over = True
                print_text(LARGE_FONT, "GAME OVER", RED)
                popup("Введите имя")
        clock.tick(snake.speed)  # FPS
        pygame.display.flip()  # обновление экрана
        if game_over:
            write_file()  # рекорды в файл
            pygame.time.wait(2000)
            break


if __name__ == "__main__":
    main()
