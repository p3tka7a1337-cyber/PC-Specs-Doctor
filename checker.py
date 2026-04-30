def check_compatibility(user, req):
    if user["ram"] < req["ram"]:
        return False

    if req["cpu"] not in user["cpu"]:
        return False

    if req["gpu"] not in user["gpu"]:
        return False

    return True