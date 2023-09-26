def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def main():
    print("Welcome to the Unit Converter!")
    print("Choose the unit category you want to convert:")
    print("1. Temperature")
    print("2. Length")
    print("3. Weight")
    
    category_choice = input("Enter the category number: ")
    
    if category_choice == '1':
        temperature = float(input("Enter the temperature in Celsius: "))
        result = celsius_to_fahrenheit(temperature)
        print(f"The temperature in Fahrenheit is: {result} °F")
    elif category_choice == '2':
        length = float(input("Enter the length in meters: "))
        result = meters_to_feet(length)
        print(f"The length in feet is: {result} feet")
    elif category_choice == '3':
        weight = float(input("Enter the weight in kilograms: "))
        result = kilograms_to_pounds(weight)
        print(f"The weight in pounds is: {result} pounds")
    else:
        print("Invalid option. Please choose a valid category.")

if __name__ == "__main__":
    main()