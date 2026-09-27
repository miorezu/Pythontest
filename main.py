import random

fun_challenges = {
    "happy": [
        "Придумай назву для своєї гри",
        "Напиши 3 речі, які сьогодні вдалися"
    ],
    "tired": [
        "Зроби перерву на 5 хвилин",
        "Намалюй простий план свого дня"
    ],
    "bored": [
        "Придумай нове правило для улюбленої гри",
        "Зміни маленьке правило у своїй кімнаті"
    ]
}

default_challenges = [
    "Випий води",
    "Запиши одну маленьку ціль на сьогодні"
]

study_challenges = [
    "Поясни будь-яку функцію своєму другу та як її застосувати",
    "Придумай новий функціонал в програмці",
    "Напиши мінімум 3-4 нові строки у коді так, щоб у консолі був якийсь вивід"
]

def choose_challenge(mood, energy, mode):
    if mode == "study":
        challenge = random.choice(study_challenges)
    elif mood in fun_challenges:
        challenge = random.choice(fun_challenges[mood])
    else:
        challenge = random.choice(default_challenges)

    if energy >= 7:
        challenge += " і зроби це просто зараз!"

    return challenge


def calculate_points(energy, mode):
    # -----------------------------------
    # - базово кожен користувач отримує 5 балів
    # - якщо енергія від 7 до 10 , додати ще 3 бали
    # - якщо енергія від 1 до 3 , додати 1 бал
    # - якщо енергія менша за 1 або більша за 10 , повернути 0
    # - якщо режим study , додати ще 2 бали
    # -----------------------------------
    points = 5
    if energy < 1 or energy > 10:
        return 0

    if 7 <= energy <= 10:
        points += 3

    if 1<= energy <= 3:
        points += 1

    if mode == "study":
        points += 2
    return points

def ask_name():
    name = input("Як тебе звати? ").strip()

    if not name:
        name = "Друже"
    return name

def ask_mood():
    mood = input(
        "Який у тебе настрій? happy / tired / bored: "
    ).strip().lower()
    return mood

def ask_energy():
    while True:
        try:
            energy = int(input("Скільки в тебе енергії від 1 до 10? "))
        except ValueError:
            print("Введи ціле число, наприклад 7.")
            continue

        if 1 <= energy <= 10:
            return energy
        print("Число має бути від 1 до 10.")

def ask_mode():
    mode = input("Обери режим fun або study: ").strip().lower()
    while mode not in ["fun", "study"]:
        mode = input("Обери режим fun або study: ").strip().lower()
    return mode

def main():
    print("=== Генератор міні-челенджів ===")

    name = ask_name()
    mood = ask_mood()
    energy = ask_energy()
    mode = ask_mode()

    challenge = choose_challenge(mood, energy, mode)
    points = calculate_points(energy, mode)

    print()
    print(f"{name}, твій челендж:")
    print(challenge)
    print(f"Бали за виконання: {points}")


if __name__ == "__main__":
    main()