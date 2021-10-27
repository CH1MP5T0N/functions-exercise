def temp():
    global temperature
    temperature = eval(input("Enter the temperature in farenheit: "))
def convert_to_celsius():
    return 5/9*(temperature - 32)
def convert_to_kelvin():
    return 5 / 9 * (temperature - 32) + 273.15
    return convert_to_kelvin()
def convert_temp():
    print(f"The temperature in Farenheit is: {temperature}")
    print(f"The temperature in Celsius is: {convert_to_celsius()}")
    print(f"The temperature in Kelvin is {convert_to_kelvin()}")
temp()
convert_temp()