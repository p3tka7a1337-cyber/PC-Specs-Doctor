def give_advice(user, req):
    advice = []

    if user["ram"] < req["ram"]:
        advice.append("➡️ Добави повече RAM")

    if req["cpu"] not in user["cpu"]:
        advice.append("➡️ Ъпгрейдни процесора")

    if req["gpu"] not in user["gpu"]:
        advice.append("➡️ Смени видеокартата")

    if not advice:
        return "Всичко е отлично! 🔥"

    return "\n".join(advice)