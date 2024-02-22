while True:
    user_input = input("\nEnter a number (or 'x' to exit): ")

    if user_input.lower() == 'x':
        print("\nExiting the program.")
        break

    try:
        num = int(user_input)
    except ValueError:
        print("Enter integer value only.")
        continue

    digit_sum = 0
    temp_num = num
    while temp_num > 0:
        digit_sum += temp_num % 10
        temp_num //= 10

    if num % digit_sum == 0:
        print(num, "is a Harshad number.")
    else:
        print(num, "is not a Harshad number.")
