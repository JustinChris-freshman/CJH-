import random
import tkinter as tk
import random

# 设置游戏界面的大小
WIDTH = 800
HEIGHT = 600
# 设置蛇的初始位置
INIT_X_POSITION = 200
INIT_Y_POSITION = 300
# 设置蛇每次移动的步长
STEP = 20


class Snake:
    def __init__(self, canvas):
        # 初始化蛇的身体
        self.body = canvas.create_rectangle(INIT_X_POSITION, INIT_Y_POSITION, INIT_X_POSITION + STEP,
                                            INIT_Y_POSITION + STEP, fill='green')
        # 初始化蛇的运动方向
        self.direction = 'Right'

    def move(self, canvas):
        # 根据蛇的运动方向改变蛇的位置
        x, y, _, _ = canvas.coords(self.body)
        if self.direction == 'Right':
            canvas.move(self.body, STEP, 0)
        elif self.direction == 'Left':
            canvas.move(self.body, -STEP, 0)
        elif self.direction == 'Up':
            canvas.move(self.body, 0, -STEP)
        elif self.direction == 'Down':
            canvas.move(self.body, 0, STEP)
        # 判断蛇是否撞墙
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return False
        return True

    def change_direction(self, direction):
        self.direction = direction


class Food:
    def __init__(self, canvas):
        # 在随机位置创建食物
        x = random.randint(0, (WIDTH / STEP) - 1) * STEP
        y = random.randint(0, (HEIGHT / STEP) - 1) * STEP
        self.food = canvas.create_oval(x, y, x + STEP, y + STEP, fill='red')

    def eat(self, snake, canvas):
        # 判断蛇是否吃到了食物
        if canvas.coords(self.food) == canvas.coords(snake.body):
            canvas.delete(self.food)
            return True
        return False


class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('贪吃蛇')
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.score = 0
        self.score_text = self.canvas.create_text(20, 20, text=f'Score: {self.score}', font=('Arial', 16), anchor='nw')
        # 监听键盘事件，以改变蛇的运动方向
        self.root.bind('<Left>', lambda event: self.snake.change_direction('Left'))
        self.root.bind('<Right>', lambda event: self.snake.change_direction('Right'))
        self.root.bind('<Up>', lambda event: self.snake.change_direction('Up'))
        self.root.bind('<Down>', lambda event: self.snake.change_direction('Down'))
        # 开始游戏循环
        self.game_loop()

    def game_over(self):
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text='Game Over', font=('Arial', 32), fill='red')

    def game_loop(self):
        if not self.snake.move(self.canvas):
            # 蛇撞墙，游戏结束
            self.game_over()
            return
        if self.food.eat(self.snake, self.canvas):
            # 蛇吃到食物，增加分数并创建新的食物
            self.score += 1
            self.canvas.delete(self.score_text)
            self.score_text = self.canvas.create_text(20, 20, text=f'Score: {self.score}', font=('Arial', 16),
                                                      anchor='nw')
            self.food = Food(self.canvas)
        self.root.after(100, self.game_loop)  # 控制游戏速度


# 启动游戏
game = Main()
game.root.mainloop()