def calculate_health(user, req):
    score = 0

    # RAM (40%)
    ram_ratio = min(user["ram"] / req["ram"], 1)
    score += ram_ratio * 40

    # CPU (30%)
    if req["cpu"].lower() in user["cpu"].lower():
        score += 30

    # GPU (30%)
    if req["gpu"].lower() in user["gpu"].lower():
        score += 30

    return int(score)


def estimate_fps(health):
    if health >= 90:
        return "🔥 Ultra (60+ FPS)"
    elif health >= 70:
        return "🟢 High (40-60 FPS)"
    elif health >= 50:
        return "🟡 Medium (30-40 FPS)"
    elif health >= 30:
        return "🟠 Low (20-30 FPS)"
    else:
        return "🔴 Very Low (<20 FPS)"