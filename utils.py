def calculate_health(user_specs, game_req):
    if not game_req:
        return 0
    
    ram_score = min(user_specs['ram'] / game_req['ram'], 1) * 100
    cpu_score = min(user_specs['cpu'] / game_req['cpu'], 1) * 100
    gpu_score = min(user_specs['gpu'] / game_req['gpu'], 1) * 100
    
    return int((ram_score + cpu_score + gpu_score) / 3)
