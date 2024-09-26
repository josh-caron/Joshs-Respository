# Scientific Calculator
import math

current_result = 0.0
counter1 = 0 # Sum of calculations
counter2 = 0 # Number of calculations
print(f"Current Result: {current_result}", end="\n\n")
print("Calculator Menu", "---------------", "0. Exit Program", "1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Exponentiation", "6. Logarithm", "7. Display Average", "", sep="\n")
while True:

    menu_selection = int(input("\nEnter Menu Selection: "))
    if menu_selection == 0:
        print("Thanks for using this calculator. Goodbye!")
        break
    elif menu_selection in [1, 2, 3, 4, 5, 6]:
        counter1 += current_result
        counter2 += 1
        first_input = (input("Enter first operand: "))
        second_input = (input("Enter second operand: "))

        if first_input == 'RESULT':
            first_operand = current_result
        else:
            first_operand = float(first_input)
        if second_input == 'RESULT':
            second_operand = current_result
        else:
            second_operand = float(second_input)

        if menu_selection == 1:
            current_result = first_operand + second_operand
        elif menu_selection == 2:
            current_result = first_operand - second_operand
        elif menu_selection == 3:
            current_result = first_operand * second_operand
        elif menu_selection == 4:
            if second_operand == 0:
                print("Error: invalid input!")
            else:
                current_result = first_operand / second_operand
        elif menu_selection == 5:
                current_result = first_operand ** second_operand
        elif menu_selection == 6:
                current_result = math.log(second_operand, first_operand)
    elif menu_selection == 7 and counter2 == 0:
        print("Error: No calculations yet to average!")
        continue
    elif menu_selection == 7:
        counter1 += current_result
        counter2 += 1
        print(f"Sum of calculations: {counter1}")
        print(f"Number of calculations: {counter2-1}")
        average = counter1 / (counter2-1)
        print(f"Average of calculations: {average:.2f}")
        continue
    elif menu_selection not in [0,1,2,3,4,5,6,7]:
        print("Error: Invalid selection!")
        continue
    print(f"Current Result: {current_result}", end="\n\n")
    print("Calculator Menu", "---------------", "0. Exit Program", "1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Exponentiation", "6. Logarithm", "7. Display Average", "", sep="\n")




