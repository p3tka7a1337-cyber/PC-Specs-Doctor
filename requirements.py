games_db = {
    "GTA 6": {
        "ram": 16,
        "cpu": 8,
        "gpu": 7
    },
    "CS2": {
        "ram": 8,
        "cpu": 4,
        "gpu": 5
    },
    "Minecraft": {
        "ram": 4,
        "cpu": 2,
        "gpu": 3
    }
}


# Връща изискванията за избраната игра
def get_game_requirements(game_name):
    return games_db.get(game_name)


# Проверка дали компютърът покрива изискванията
def check_compatibility(user_specs, game_req):
    if not game_req:
        return False

    return (
        user_specs["ram"] >= game_req["ram"] and
        user_specs["cpu"] >= game_req["cpu"] and
        user_specs["gpu"] >= game_req["gpu"]
    )
