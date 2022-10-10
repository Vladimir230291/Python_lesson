import json

data_files = {}


def save():
    with open("File.json", 'w', encoding='utf=8') as fh:
        fh.write(json.dumps(data_files, ensure_ascii=False))
    print("Данные успешно сохранены")
    fh.close()


def load():
    with open("File.json", "r", encoding="utf=8") as fh:
        data_files = json.load(fh)
    print("Данные загружены")
    print("")
    fh.close()
    return data_files


def search_film_and_del(arg, dist):
    try:
        del dist[arg]
    except:
        print("Такого фильма нет или вы допустили ошибку при вводе")
    return dist



try:
    data_files = load()
except:
    print("пусто")

while True:

    print("Введите команду '/Start' для начала работы с ботом или '/Stop', что бы оставить работу:")
    command = input(">> ")

    if command.lower() == "/start":
        print("Список фильмов которые вы хотели бы пересмотреть: ")
        print(data_files)
        print("Хотите дополнить список? (/add) или удалить просмотренный? (/del)")
        print("Что бы сохранить изменения введите '/save'")
        command = input(">> ")

        if command.lower() == "/add":  # добавление фильма
            print("Введите название фильма и жанр если необходимо")
            film = input("название фильма: ")
            genre = input("Жанр: ")
            data_files[film] = genre
            print("Фильм добален")
            save()
            print(data_files)

        elif command.lower() == "/del":  # удаление фильма
            flag = True
            while flag:
                print('Введите название фильма который необходимо удалить, что бы завершить введите "0" ')
                film_srh = input(">> ")

                if film_srh == "0":
                    flag = False
                    break
                data_files = search_film_and_del(film_srh, data_files)
                print("Фильм удален")
                save()
                print(data_files)  # контрольный вывод

        elif command.lower() == "/save":
            save()


















    elif command.lower() == "/stop":
        print("Бот завершил свою работу")
        break
