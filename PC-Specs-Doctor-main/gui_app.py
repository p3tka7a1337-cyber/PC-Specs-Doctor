import customtkinter as ctk
import threading
import time

from hardware import get_user_specs
from requirements import get_game_requirements
from checker import check_compatibility
from doctor import give_advice
from utils import calculate_health, estimate_fps

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

GAMES = [
    "GTA 6", "CS2", "Minecraft", "Valorant",
    "Cyberpunk 2077", "Fortnite", "Warzone", "Apex Legends",
    "Red Dead Redemption 2", "Elden Ring", "Hogwarts Legacy",
    "League of Legends", "Dota 2", "PUBG", "Overwatch 2",
    "The Witcher 3", "Battlefield 2042", "Rainbow Six Siege",
    "Starfield", "Assassin's Creed Valhalla"
]

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PC Specs Doctor ")
        self.geometry("900x550")

        self.user = get_user_specs()

        # SIDEBAR
        self.sidebar = ctk.CTkFrame(self, width=220)
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(self.sidebar, text="💻 PC Doctor", font=("Arial", 20, "bold")).pack(pady=20)

        self.combo = ctk.CTkComboBox(self.sidebar, values=GAMES)
        self.combo.set("Избери игра")
        self.combo.pack(pady=10, padx=10)

        ctk.CTkButton(self.sidebar, text="Анализ", command=self.start).pack(pady=20)

        # MAIN
        self.main = ctk.CTkFrame(self)
        self.main.pack(expand=True, fill="both")

        self.info = ctk.CTkLabel(self.main, text=self.get_info(), justify="left")
        self.info.pack(pady=20)

        self.progress = ctk.CTkProgressBar(self.main)
        self.progress.set(0)
        self.progress.pack(pady=10, padx=60)

        self.result = ctk.CTkLabel(self.main, text="", font=("Arial", 15))
        self.result.pack(pady=20)

    def get_info(self):
        if not self.user:
            return "Error detecting PC"

        return (
            f"CPU: {self.user['cpu']}\n"
            f"GPU: {self.user['gpu']}\n"
            f"RAM: {self.user['ram']} GB"
        )

    def start(self):
        game = self.combo.get()
        if game not in GAMES:
            return

        threading.Thread(target=self.analyze, args=(game,), daemon=True).start()

    def analyze(self, game):
        self.progress.set(0)
        self.result.configure(text="🔍 Анализиране...")

        for i in range(5):
            time.sleep(0.4)
            self.progress.set((i + 1) / 5)

        req = get_game_requirements(game)

        ok = check_compatibility(self.user, req)
        health = calculate_health(self.user, req)
        fps = estimate_fps(health)
        advice = give_advice(self.user, req)

        text = (
            f"{'✅ OK' if ok else '❌ NOT OK'}\n\n"
            f"Health: {health}%\n"
            f"FPS: {fps}\n\n"
            f"{advice}"
        )

        self.result.configure(text=text)


if __name__ == "__main__":
    app = App()
    app.mainloop()