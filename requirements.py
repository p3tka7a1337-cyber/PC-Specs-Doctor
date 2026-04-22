games_db = {
    # Тежки игри (High-end)
    "Cyberpunk 2077": {"ram": 16, "cpu": 8, "desc": "Изисква мощна машина за Night City."},
    "Elden Ring": {"ram": 12, "cpu": 6, "desc": "Трябва ви стабилен процесор за отворения свят."},
    "Alan Wake 2": {"ram": 16, "cpu": 8, "desc": "Една от най-тежките игри за 2024/2025 г."},
    
    # Средни игри (Mid-range)
    "Red Dead Redemption 2": {"ram": 12, "cpu": 6, "desc": "Оптимизирана, но изисква памет."},
    "Forza Horizon 5": {"ram": 8, "cpu": 4, "desc": "Добре балансирана състезателна игра."},
    "The Witcher 3": {"ram": 8, "cpu": 4, "desc": "Класика, която върви на повечето съвременни PC-та."},
    "Baldur's Gate 3": {"ram": 16, "cpu": 6, "desc": "Изисква повече RAM за по-късните етапи на играта."},

    # Леки игри (Low-end / Competitive)
    "CS 2": {"ram": 8, "cpu": 4, "desc": "Важно е бързото CPU за повече кадри."},
    "Valorant": {"ram": 4, "cpu": 2, "desc": "Върви дори на „картоф“."},
    "League of Legends": {"ram": 4, "cpu": 2, "desc": "Много лека, подходяща за лаптопи."},
    "Minecraft": {"ram": 4, "cpu": 2, "desc": "Върви на всичко, освен ако не сложите 100 мода."},
    "Roblox": {"ram": 4, "cpu": 2, "desc": "Минимални изисквания."}
}

def check_compatibility(user_specs, game_name):
    if game_name not in games_db:
        return None  # Играта не е намерена
    
    req = games_db[game_name]
    results = {
        "is_compatible": True,
        "missing_ram": 0,
        "missing_cpu": 0,
        "description": req["desc"]
    }
    
    if user_specs['ram'] < req['ram']:
        results["is_compatible"] = False
        results["missing_ram"] = req["ram"] - user_specs['ram']
        
    if user_specs['cpu'] < req['cpu']:
        results["is_compatible"] = False
        results["missing_cpu"] = req["cpu"] - user_specs['cpu']
        
    return results
