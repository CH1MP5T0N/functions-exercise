def num_atoms():
    global atom
    atom = float(input("Amount of the element (in grams): "))
    formula = (atom / 196.97) * (6.02214154 * 10**23)
    print(f"If it was the element gold (Au), there would be {formula} atoms!")
    weight = float(input("Atomic weight of the element: "))
    actual_formula = (atom/ weight) * (6.02214154 * 10^23)
    print(actual_formula)

num_atoms()