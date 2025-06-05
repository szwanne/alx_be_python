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

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

user_input = float(input("Enter the temperature to convert: "))
temperature_type = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature_type == "C":
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * user_input) + 32
    print(f"{user_input}°C is {fahrenheit:}°F")
elif temperature_type == "F":
    celsius = (user_input - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{user_input}°F is {celsius:}°C")
else:
    print("Invalid temperature type. Please enter 'C' or 'F'.")
