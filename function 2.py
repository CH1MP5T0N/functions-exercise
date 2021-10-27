def calc_weight_on_jupiter():
    global user
    user = float(input("Enter weight on Earth: "))
    weight_on_jupiter = (user / 9.8) * 23.1
    print(f"Your weight on Jupiter would be {weight_on_jupiter}")
def calc_weight_on_planet():
    surface_gravity = eval(input("Enter surface gravity of a planet: "))
    weight = (user / 9.8) * surface_gravity
    print(weight)
calc_weight_on_jupiter()
calc_weight_on_planet()



