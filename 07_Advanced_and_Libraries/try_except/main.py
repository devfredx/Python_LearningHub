try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division performed successfully.")
finally:
    print("Cleanup operations completed.")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise Exception("Access denied: Under 18.")
    return True

try:
    validate_age(-5)
except ValueError as ve:
    print(f"Validation Error: {ve}")
except Exception as e:
    print(f"System Error: {e}")

try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File was not found on the system.")

data = {"id": 1, "name": "Admin"}
try:
    print(data["role"])
except KeyError:
    print("The requested key does not exist.")

numbers = [1, 2, 3]
try:
    print(numbers[10])
except IndexError:
    print("Index is out of range for this list.")

try:
    import non_existent_module
except ImportError:
    print("The module could not be imported.")