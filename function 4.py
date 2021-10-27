import fractions
def calc_new_height():
    width = eval(input("Enter the current width: "))
    height = eval(input("Enter the current height: "))
    desired_width = eval(input("Enter the desired width: "))
    ratio = fractions.Fraction(height, width)
   print(desired_width*ratio)

calc_new_height()