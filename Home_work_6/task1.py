# Создайте программу для игры в "Крестики-нолики"


def print_board(board_work):
    print("-" * 13)
    for i in range(3):
        print(board_work[0 + i * 3], "|", board_work[1 + i * 3], "|", board_work[2 + i * 3])
    print("-" * 13)


def take_input(symbol):
    valid = False
    while not valid:
        try:
            symbol_place = int(input(f"Куда ставим {symbol} ? "))
        except:
            print("Введите число!")
            continue
        if 1 <= symbol_place <= 9:
            if str(board[symbol_place - 1]) not in "XO":
                board[symbol_place - 1] = symbol
                valid = True
            else:
                print("Клетка занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(board_work):
    win_coord = ((0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 3, 6),
                 (1, 4, 7),
                 (2, 5, 8),
                 (0, 4, 8),
                 (2, 4, 6))
    for symbol in win_coord:
        if board_work[symbol[0]] == board_work[symbol[1]] == board_work[symbol[2]]:
            return board_work[symbol[0]]
    return False


board = list(range(1, 10))
count = 0
win_flag = False
while not win_flag:
    print_board(board)
    if count % 2 == 0:
        take_input("X")
    else:
        take_input("O")
    count += 1
    if count > 4:
        temp = check_win(board)
        if temp:
            print(temp, "выиграл!")
            win_flag = True
            break
    if count == 9:
        print("Ничья!")
        break
print_board(board)
