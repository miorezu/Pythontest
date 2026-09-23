import random

challenges = {
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


def choose_challenge(mood, energy):
    if mood == "happy":
        challenge = random.choice(challenges["happy"])
    elif mood == "tired" or mood == "bored":
        challenge = random.choice(challenges[mood])
    else:
        challenge = random.choice(default_challenges)

    if energy > 7:
        challenge = challenge + " і зроби це просто зараз!"

    return challenge


def calculate_points(energy, mode):
    # TODO: завершити функцію за правилами з умови.
    return 0


print("=== Генератор міні-челенджів ===")

name = input("Як тебе звати? ")
mood = input("Який у тебе настрій? happy / tired / bored: ")
energy = int(input("Скільки в тебе енергії від 1 до 10? "))
mode = input("Обери режим fun або study: ")

challenge = choose_challenge(mood, energy)
points = calculate_points(energy, mode)

print()
print(f"{name}, твій челендж:")
print(challenge)
print(f"Бали за виконання: {points}")