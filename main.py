import time
import sys

from hardware import get_user_specs
from requirements import get_game_requirements, check_compatibility
from doctor import give_advice
from utils import calculate_health


# ===== UI =====
def print_header():
    print("=" * 45)
    print("        PC SPECS DOCTOR")
    print("=" * 45)


def print_menu():
    print("\nИзбери игра:")
    print("1. GTA 6")
    print("2. CS2")
    print("3. Minecraft")
    print("0. Изход")


def get_game_choice():
    mapping = {
        "1": "GTA 6",
        "2": "CS2",
        "3": "Minecraft"
    }

    choice = input("Избор: ")

    if choice == "0":
        return "0"

    return mapping.get(choice)


# ===== REAL LOADING (етапи) =====
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
        time.sleep(0.7)
        print(" ✔")

    print("\n--- Анализ завършен ---\n")


# ===== RESULT UI =====
def print_result(is_ok, health, advice):
    print("=" * 45)

    if is_ok:
        print("✅ Системата покрива изискванията!")
    else:
        print("❌ Системата НЕ покрива изискванията!")

    print(f"\nHealth Score: {health}%")

    print("\nПрепоръка:")
    print(advice)

    print("=" * 45)


# ===== MAIN =====
def main():
    print_header()

    user_specs = get_user_specs()
    if not user_specs:
        return

    while True:
        print_menu()
        game = get_game_choice()

        if game == "0":
            print("\nИзход...")
            break

        if game is None:
            print("❌ Невалиден избор.\n")
            continue

        req = get_game_requirements(game)

        # реален loading процес
        loading_steps()

        is_ok = check_compatibility(user_specs, req)
        health = calculate_health(user_specs, req)
        advice = give_advice(user_specs, req)

        print_result(is_ok, health, advice)


if __name__ == "__main__":
    main()
