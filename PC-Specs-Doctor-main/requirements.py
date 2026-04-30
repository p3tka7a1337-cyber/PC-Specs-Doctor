def get_game_requirements(game):
    games = {
        "GTA 6": {"ram": 16, "cpu": "i7", "gpu": "RTX"},
        "CS2": {"ram": 8, "cpu": "i5", "gpu": "GTX"},
        "Minecraft": {"ram": 4, "cpu": "i3", "gpu": "Intel"},
        "Valorant": {"ram": 4, "cpu": "i3", "gpu": "GTX"},

        "Cyberpunk 2077": {"ram": 16, "cpu": "i7", "gpu": "RTX"},
        "Fortnite": {"ram": 8, "cpu": "i5", "gpu": "GTX"},
        "Warzone": {"ram": 16, "cpu": "i7", "gpu": "RTX"},
        "Apex Legends": {"ram": 8, "cpu": "i5", "gpu": "GTX"},
        "Red Dead Redemption 2": {"ram": 12, "cpu": "i7", "gpu": "GTX"},
        "Elden Ring": {"ram": 12, "cpu": "i7", "gpu": "GTX"},
        "Hogwarts Legacy": {"ram": 16, "cpu": "i7", "gpu": "RTX"},
        "League of Legends": {"ram": 4, "cpu": "i3", "gpu": "Intel"},
        "Dota 2": {"ram": 4, "cpu": "i3", "gpu": "GTX"},
        "PUBG": {"ram": 16, "cpu": "i7", "gpu": "GTX"},
        "Overwatch 2": {"ram": 8, "cpu": "i5", "gpu": "GTX"},
        "The Witcher 3": {"ram": 8, "cpu": "i5", "gpu": "GTX"},
        "Battlefield 2042": {"ram": 16, "cpu": "i7", "gpu": "RTX"},
        "Rainbow Six Siege": {"ram": 8, "cpu": "i5", "gpu": "GTX"},
        "Starfield": {"ram": 16, "cpu": "i7", "gpu": "RTX"},
        "Assassin's Creed Valhalla": {"ram": 16, "cpu": "i7", "gpu": "GTX"},
    }

    return games.get(game)