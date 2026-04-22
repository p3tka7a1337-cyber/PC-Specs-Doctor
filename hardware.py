def get_user_specs():
    print("\n=== ВЪВЕЖДАНЕ НА ХАРДУЕР ===")

    while True:
        try:
            ram = int(input("RAM (GB): "))
            cpu = int(input("CPU ядра: "))
            gpu = int(input("GPU ниво (1-10): "))

            if ram <= 0 or cpu <= 0 or gpu <= 0:
                print("❌ Стойностите трябва да са положителни.\n")
                continue

            return {
                "ram": ram,
                "cpu": cpu,
                "gpu": gpu
            }

        except ValueError:
            print("❌ Моля въведи число.\n")
