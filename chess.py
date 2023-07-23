import random


def check_beat(x, y):
    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j] or \
                    y[i] == y[j] or \
                    abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
            else:
                return True


def generate_positions():
    x = list(range(1, 9))
    y = list(range(1, 9))
    for i in range(4):
        random.shuffle(x)
        random.shuffle(y)
        while not check_beat(x, y):
            random.shuffle(x)
            random.shuffle(y)
        print(x, y)

