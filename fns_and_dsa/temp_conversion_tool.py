# FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
# CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# def convert_to_celsius(fahrenheit):
#     return FAHRENHEIT_TO_CELSIUS_FACTOR*(fahrenheit - 32)


# def convert_to_fahrenheit(celsius):
#     return CELSIUS_TO_FAHRENHEIT_FACTOR*celsius + 32


# user_input = float(input("Enter the temperature to convert: "))
# temperature_type = input(
#     "Is this temperature in Celsius or Fahrenheit? (C/F): ")
# if temperature_type == "C":
#     print(f"{user_input}°C is {convert_to_fahrenheit(user_input):}°F")
# elif temperature_type == "F":
#     print(f"{user_input}°F is {convert_to_celsius(user_input):}°C")
# else:
#     print("Invalid temperature type. Please enter 'C' or 'F'.")

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


user_input = float(input("Enter the temperature to convert: "))
temperature_type = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature_type == "F":
    celsius = convert_to_celsius(user_input)
    print(f"{user_input}°F is {celsius:}°C")
elif temperature_type == "C":
    fahrenheit = convert_to_fahrenheit(user_input)
    print(f"{user_input}°C is {fahrenheit:}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")
