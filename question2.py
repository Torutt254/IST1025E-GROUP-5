# This is a program that accepts temperature in Farenheit and converts it to Celsuis.
#Creating of function to convert Farenheit to Celcius
def fahrenheit_to_celsius(fahrenheit):
    if isinstance(fahrenheit, (int, float)):
        celcius = (fahrenheit -32) * 5.0/9.0
        return celcius
    else:
        return "Invalid input. Please enter a valid number."


fahrenheit = float(input("Enter temperature in Farenheit: "))
celcius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} Farenheit is equal to {celcius} Celcius.")

if celcius < 20:
    print("IT'S COLD HERE!")
else:
    print("IT'S WARM HERE!")
