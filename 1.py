def convert_to_days():
    global hours
    hours = eval(input("Enter number of hours: "))
    global minutes
    minutes = eval(input("Enter number of minutes: "))
    global seconds
    seconds = eval(input("Enter number of seconds: "))
convert_to_days()
def get_days():
    formula = (hours / 24) + (minutes / 1440) + (seconds / 86400)
    x = round(formula, 4)
    print(float(x))
get_days()




