players = [
    {"name": "Дима","health": 100,"score": 0},
    {"name": "Саня","health": 100,"score": 0},
    {"name": "Арман","health": 100,"score": 0}
]
def show_player(player):
    print("Игрок: ", player["name"])
    print("Здоровье: ", player["health"])
    print("Очки: ", player["score"])
def add_score(player, score):
    if score <= 0:
        print("Очки должны быть положительным числом")
        return
    player["score"] += score
def take_damage(player, damage):
    if damage <= 0:
        print("Урон должен быть положительным")
        return
    player["health"] -= 50
    print("Урон нанесен")
    if player["health"] <= 0:
        player["health"] = 0
        print("У игрока не осталось здоровья. Игрок погиб")
def read_int(text):
    try:
        return int(input(text).strip())
    except ValueError:
        print("Нужно целое число")
        return None
def game(player):
    while True:
        print(" ╔════════════════════════════════╗")
        print(" ║1.      Показать профиль        ║")
        print(" ║2.       Добавить очки          ║")
        print(" ║3.       Нанести урон           ║")
        print(" ║0.          Выход               ║")
        print(" ╚════════════════════════════════╝")
        a = input("Выберите: ").strip()
        if a == "0":
            break
        elif a == "1":
            show_player(player)
        elif a == "2":
            score = read_int("Сколько очков добавить? ")
            if score is not None:
                add_score(player, score)
        elif a == "3":
            damage = read_int("Сколько урона нанести? ")
            if damage is not None:
                take_damage(player, damage)
        else:
            print("Неизвестная команда! Ход не засчитан. Попробуйте снова.")
def menu():
    while True:
        print("              МЕНЮ")
        print(" ╔════════ДОБРО ПОЖАЛОВАТЬ════════╗")
        print(" ║       ВЫБЕРИТЕ ПЕРСОНАЖА:      ║")
        print(" ║1.          Дима                ║")
        print(" ║2.          Саня                ║")
        print(" ║3.          Арман               ║")
        print(" ║0.          Выход               ║")
        print(" ╚════════════════════════════════╝")
        a = (input("Выберите: "))
        if a == "0":
            break
        elif a == "1":
            game(players[0])
        elif a == "2":
            game(players[1])
        elif a == "3":
            game(players[2])
        else:
            print("Неизвестная команда! Ход не засчитан. Попробуйте снова.")
menu()