# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import time
import random


def bot_play(score):
    if score >= 60:
        return random.randint(25,28)
    elif 60 >= score >= 41:
        return random.randint(1, 20)
    elif 40 >= score >= 33:
        return random.randint(1, 4)
    elif 32 >= score >= 30:
        return random.randint(1, 2)
    elif 30 > score >= 29:
        return 1
    elif score <= 28:
        return score


def player():
    player_one = int(input("Введите какое количество конфет взять, но не больше 28: "))
    if player_one <= 28:
        return player_one
    else:
        return 0

candy = 100
#lottery_result = random.randint(0, 1)


while candy > 0:
    try:
        candy -= player()
        print(f"осталось {candy} конфет")

        if candy == 0:
            print("Победил игрок")
            break

        print("противник берет конфеты...")
        time.sleep(2)

        get_bot = bot_play(candy)
        print(f"бот взял {get_bot} конфет")
        candy -= get_bot
        print(f"осталось {candy} конфет")

        if candy == 0:
            print("победил бот")

    except:
        print("Вводите только целые цисла")


