import tkinter as tk
import random

# настройки игрового поля
WIDTH = 400
HEIGHT = 400
DIRECTIONS = ["Up", "Down", "Left", "Right"]    # константа возможных направлений для движения
CELL_SIZE = 10                                  # размер одной клетки змейки и еды
DELAY = 100                                     # условная скорость игры

# создаем главное (родительское) окно
root = tk.Tk()                  # создание главног окна
root.title("Змейка | Счет: 0")  # устанавливаем заголовок окна
root.resizable(False, False)    # фиксирует размер окна (по ширине, высоте)

# игровое поле
canvas = tk.Canvas(
    root,                   # родительское окно
    width=WIDTH,            # ширина поля
    height=HEIGHT,          # высота поля
    bg="black",             # цвет фона - черный
    highlightthickness=0    # убираем границу
)
canvas.pack()   # Размещаем canvas в главном окне

# создаем начальное положение змейки
# разме рсегмента принят 10x10 пикселей
snake = [(100, 100), (90, 100), (80, 100)]      # список координат всех сегментов змейки (голова вначале, хвост - в конце)
direction = "Right"                             # переменная, хранящая направление движения змейки
food = None                                     # переменная для хранения координат еды
score = 0                                       # счетчик очков
game_over = False                               # состояние игры

# функция, создающая еду в случайном месте на игровом поле
def create_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

# создание первой еды
food = create_food()

# функция отрисовки еды
def draw_food():
    pass

# some changes for git



# запуск главного цикла программы
root.mainloop()