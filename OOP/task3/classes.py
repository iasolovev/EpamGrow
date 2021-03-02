import random


class Move:
    move_time = 0

    def __init__(self):
        Move.move_time = 0

    @staticmethod
    def move_forward():
        print(' ' * Move.move_time, 'vvvvv')
        Move.move_time += 5

    @staticmethod
    def move_left():
        print(' ' * Move.move_time, '<')
        Move.move_time += 1

    @staticmethod
    def move_right():
        print(' ' * Move.move_time, '>')
        Move.move_time += 1


class Skier(Move):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def move(self, move_time):
        move_time += self.move_time
        print('Лыжник', self.name, 'отправился в путь!')
        while self.move_time <= move_time:
            side = random.random()
            if side < 0.333:

                self.move_forward()
            elif side < 0.666:
                self.move_left()
            else:
                self.move_right()

