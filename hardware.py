def get_user_specs():
    print("\n" + "=" * 40)
    print("   ВЪВЕЖДАНЕ НА ХАРДУЕР")
    print("=" * 40)

    while True:
        try:
            ram = int(input("RAM (GB): "))
            cpu = int(input("CPU ядра: "))
            gpu = int(input("GPU ниво (1-10): "))

            if ram <= 0 or cpu <= 0 or gpu <= 0:
                print("❌ Стойностите трябва да са положителни.\n")
                continue

            if gpu > 10:
                print("❌ GPU трябва да е между 1 и 10.\n")
                continue

            return {
                "ram": ram,
                "cpu": cpu,
                "gpu": gpu
            }

        except ValueError:
            print("❌ Моля въведи валидни числа.\n")
