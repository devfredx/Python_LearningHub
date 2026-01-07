while True:
    user_input = input("\nEnter a number (or 'x' to exit): ")

    if user_input.lower() == 'x':
        print("Exiting the program.")
        break

    try:
        num = int(user_input)
    except ValueError:
        print("Enter integer value only.")
        continue

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    if divisors_sum > num:
        print(num, "is an abundant number.")
    else:
        print(num, "is not an abundant number.")
        
