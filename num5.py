import random

print(
    "Доброго времени суток, уважаемый игрок и добро пожаловать в мою игру! \n"
    "Правила: В начале игры мы случайным образом определим изначальное количество камней в куче.\n"
    "Далее игроки будут по очереди выбирать какое количество камней они хотят убрать из кучи (1 - 3 камня).\n"
    "Победителем будет считается тот игрок, после окончания хода которого, в куче остался один камень.\n")


def player_step(input_data):
    for char in input_data:
        if char not in "012345678":
            return False
        if (int(input_data) < 1) or (int(input_data) > 3):
            return False
        return True


def koordinal_step(number_stones):
    if number_stones <= 4:
        return 1, abs(1 - number_stones)
    koordinal_step = random.randint(1, 3)
    return number_stones - koordinal_step, koordinal_step


number_stones = random.randint(4, 30)
win = "logout"

while win == "logout":
    print(f"\nТекущее значение камней в куче: {number_stones}\n")
    print("Ваш ход\n"
          "Введите число камней, которое хотите убрать из кучи (1 - 3 камня): ")

    input_data = input()

    if player_step(input_data):
        player_stone = int(input_data)
        number_stones = number_stones - player_stone

        if number_stones == 1:
            print("\nCongratulations!")
            win = "Player_win"
        elif number_stones < 1:
            print("Вы уверены, что ввели верное значение?")
        elif number_stones > 1:
            print(f"\nТекущее значение камней в куче: {number_stones}\n")
            print("Ход другого игрока ...")
            number_stoners, koordinal_stone = koordinal_step(number_stoners)

            if koordinal_stone == 1:
                print(f"Другой игрок убрал {koordinal_stone} камень из кучи")
            else:
                print(f"Другой игрок убрал {koordinal_stone} камня(-ей-) из кучи")

            if number_stones == 1:
                print(f"\nТекущее значение камней в куче: {number_stones}\n")
                print("You are dead. Game over!")
                win = "koordinal_win"

    else:
        print("Введено неверное значение. Введите возможное количество.")
