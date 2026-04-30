def give_advice(user_specs, game_req):
    advice = []
    if user_specs['ram'] < game_req['ram']:
        advice.append(f"Добавете поне {game_req['ram'] - user_specs['ram']}GB RAM.")
    if user_specs['cpu'] < game_req['cpu']:
        advice.append(f"Процесорът е слаб (трябват поне {game_req['cpu']} ядра).")
    if not advice:
        return "Системата е перфектна!"
    return "Съвет: " + " ".join(advice)
