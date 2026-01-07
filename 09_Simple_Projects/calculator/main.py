print("Welcome to the Basic Calculator!")

while True:
    print("\nCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3]:
        num_inputs = int(input("\nHow many numbers do you want to {}: ".format(
            ["add", "subtract", "multiply"][choice - 1])))
        numbers = [float(input("{}: ".format(i + 1))) for i in range(num_inputs)]
    elif choice == 4:
        num1 = float(input("\nEnter the numerator: "))
        num2 = float(input("Enter the denominator (non-zero): "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        numbers = [num1, num2]
    elif choice == 5:
        print("\nExiting Calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        continue

    if choice == 1:
        result = sum(numbers)
        print("Result:", result)
    elif choice == 2:
        result = numbers[0] - sum(numbers[1:])
        print("Result:", result)
    elif choice == 3:
        result = 1
        for num in numbers:
            result *= num
        print("Result:", result)
    elif choice == 4:
        result = numbers[0] / numbers[1]
        print("Result:", result)