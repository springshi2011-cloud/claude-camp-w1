# Temperature Converter — Celsius and Fahrenheit

print("=== Temperature Converter ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose conversion type (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")

else:
    print("Invalid input. Please enter 1 or 2.")