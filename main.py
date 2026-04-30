import time
import sys
import os

from hardware import get_user_specs
from requirements import get_game_requirements
from checker import check_compatibility
from doctor import give_advice
from utils import calculate_health

GAMES = [
    "GTA 6", "CS2", "Minecraft", "Valorant",
    "Cyberpunk 2077", "Fortnite", "Warzone", "Apex Legends",
    "Red Dead Redemption 2", "Elden Ring", "Hogwarts Legacy",
    "League of Legends", "Dota 2", "PUBG", "Overwatch 2",
    "The Witcher 3", "Battlefield 2042", "Rainbow Six Siege",
    "Starfield", "Assassin's Creed Valhalla"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("\n" + "=" * 50)
    print("💻 PC SPECS DOCTOR")
    print("=" * 50)

def print_menu():
    print("\nИзбери игра:\n")
    for i, game in enumerate(GAMES, 1):
        print(f"{i}. {game}")
    print("0. Изход")

def get_game_choice():
    choice = input("\nИзбор: ")

    if choice == "0":
        return "0"

    if not choice.isdigit():
        return None

    index = int(choice) - 1

    if 0 <= index < len(GAMES):
        return GAMES[index]

    return None

def loading_steps():
    steps = [
        "Проверка на RAM",
        "Проверка на CPU",
        "Проверка на GPU",
        "Сравнение с изисквания",
        "Генериране на резултат"
    ]

    print("\n--- Анализ започва ---\n")

    for step in steps:
        print(step + "...", end="")
        sys.stdout.flush()
        time.sleep(0.5)
        print(" ✔")

    print("\n--- Анализ завършен ---\n")

def print_result(is_ok, health, advice):
    print("=" * 50)

    if is_ok:
        print("✅ Системата покрива изискванията!")
    else:
        print("❌ Системата НЕ покрива изискванията!")

    print(f"\nHealth Score: {health}%")

    print("\nПрепоръка:")
    print(advice)

    print("=" * 50)

def main():
    print_header()

    user_specs = get_user_specs()
    if not user_specs:
        return

    print("\n🖥️ Твоят компютър:")
    print(f"CPU: {user_specs['cpu']}")
    print(f"GPU: {user_specs['gpu']}")
    print(f"RAM: {user_specs['ram']} GB")
    input("\nНатисни Enter...")

    while True:
        clear_console()
        print_menu()
        game = get_game_choice()

        if game == "0":
            print("\nИзход...")
            break

        if game is None:
            print("❌ Невалиден избор.")
            continue

        req = get_game_requirements(game)

        loading_steps()

        is_ok = check_compatibility(user_specs, req)
        health = calculate_health(user_specs, req)
        advice = give_advice(user_specs, req)

        print_result(is_ok, health, advice)
        input("\nEnter за меню...")

if __name__ == "__main__":
    main()