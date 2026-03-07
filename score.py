def add_points(game, amount):
    if amount < 0:
        raise ValueError("Please enter a positive number")
    elif game["active"] == False:
        return game
    else:
        game["score"] += (amount * game["multiplier"])
        return game


def apply_multiplier(game,multiplier):
    if multiplier < 1:
        raise ValueError("Multiplier must be greater than or equal to 1")
    elif game["active"] == False:
        return game
    else:
        game["multiplier"] = multiplier
        return game
        
def reset_score(game):
    game["score"] = 0
    game["multiplier"] = 1
    return game

def is_high_score(game, threshold):
    if threshold < 0:
        raise ValueError("Threshold must be greater than 0")
    if game["score"] > threshold:
        return True
    else:
        return False
