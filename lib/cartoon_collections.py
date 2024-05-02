def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f"{dwarves.index(dwarf) + 1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [f"{call.capitalize()}!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    for ingredient in strings:
        if ingredient == "gouda" or ingredient == "cheddar" or ingredient == "camembert":
            return ingredient
    return None