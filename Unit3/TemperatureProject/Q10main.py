from temperature.celsius_to_fahrenheit import c_to_f
from temperature.fahrenheit_to_celsius import f_to_c
from temperature.celsius_to_kelvin import c_to_k

print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

try:
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit:", c_to_f(c))

    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius:", f_to_c(f))

    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        print("Kelvin:", c_to_k(c))

    else:
        print("Invalid choice")

except Exception as e:
    print("Error:", e)