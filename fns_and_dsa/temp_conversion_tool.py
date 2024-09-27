FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():

    try:
        temp = float(input("Enter the temperature to convert: "))
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if temp_type =='C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f'{temp}°C is {converted_temp}°F')
        elif temp_type == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f'{temp}°F is {converted_temp}°C')
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
        
