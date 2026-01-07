while True:
    num = input("\nEnter a number or x to exit: ")
    if num.lower() == 'x':
        break
    if not num.isdigit():
        print("Please enter a valid integer.")
        continue
    num = int(num)
    if num <= 1:
        print("Please enter a number greater than 1.")
        continue

    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
