#Fahrenheit, Kelvin, Celsius converter
first_unit = input("Enter the unit you are converting from: ")
second_unit = input("Enter the unit you are converting to: ")
temp_given = float(input(f"Enter the temperature in {first_unit}: "))

if first_unit == 'Fahrenheit' and second_unit == 'Celsius':
    temperature =  (temp_given - 32) * 5/9
elif first_unit == 'Fahrenheit' and second_unit == 'Kelvin':
    temperature = (temp_given - 32) * 5/9 + 273.15
elif first_unit == 'Fahrenheit' and second_unit == 'Fahrenheit':
    temperature = temp_given
elif first_unit == 'Celsius' and second_unit == 'Fahrenheit':
    temperature = temp_given * 9/5 + 32
elif first_unit == 'Celsius' and second_unit == 'Kelvin':
    temperature = temp_given + 273.15
elif first_unit == 'Celsius' and second_unit == 'Celsius':
    temperature = temp_given
elif first_unit == 'Kelvin' and second_unit == 'Fahrenheit':
    temperature = (temp_given - 273.15) * 9/5 + 32
elif first_unit == 'Kelvin' and second_unit == 'Celsius':
    temperature = temp_given - 273.15
elif first_unit == 'Kelvin' and second_unit == 'Kelvin':
    temperature = temp_given
else:
    temperature = "ERROR"

print(f"That is {temperature:.1f} degrees {second_unit}.")