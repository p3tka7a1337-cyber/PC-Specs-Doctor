from hardware import get_user_specs
from requirements import get_game_requirements, check_compatibility
from doctor import give_advice
from utils import calculate_health


def print_header():
    print("=" * 40)
    print("      PC SPECS DOCTOR")
    print("=" * 40)


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
    return mapping.get(choice)


def print_result(is_ok, health, advice):
    print("\n" + "=" * 40)

    if is_ok:
        print("✅ Системата покрива изискванията!")
    else:
        print("❌ Системата НЕ покрива изискванията!")

    print(f"\nHealth Score: {health}%")

    print("\nПрепоръка:")
    print(advice)

    print("=" * 40)


def main():
    print_header()

    user_specs = get_user_specs()
    if not user_specs:
        return

    while True:
        print_menu()
        game = get_game_choice()

        if game is None:
            print("❌ Невалиден избор.\n")
            continue

        if game == "0":
            print("Изход...")
            break

        req = get_game_requirements(game)

        is_ok = check_compatibility(user_specs, req)
        health = calculate_health(user_specs, req)
        advice = give_advice(user_specs, req)

        print_result(is_ok, health, advice)


if __name__ == "__main__":
    main()
