myName = "fred"
myName.upper()
print(myName)
print()

#input
def hiPython():
    print("Hi python")
hiPython()
print()

def hello_name(name):
    print("Hello " , name)
hello_name("fred")
print()

def sum_example(num1, num2):
    print(num1 + num2)
sum_example(10,12)
print()

def hello_surname(surname="ada"):
    print("Hello " , surname)
hello_surname()
print()

#return

def summation(num1, num2, num3):
    print(num1+num2+num3)
summation(10,20,30)

x = summation(5,10,15)
print(x)
print(type(x))

def return_summation(num1, num2, num3):
    return num1+num2+num3
print(return_summation(20,25,30))
x = return_summation(20,25,30)
print(x)

#input & return

def return_summation(num1, num2, num3):
    result = num1+num2+num3
    print(result)
    return result

x = return_summation(3,6,9)
print(x)

def control_string(s):
    if s[0] == "a":
        print("a")

control_string("ada")
control_string("python")

#args, kwargs (arguments, key word arguments)

def args_sum(*args):
    return sum(args)

print(args_sum(10,15,20,25,30))

def args_example(*args):
    print(args)

args_example(9,4,5,3,1,6)

def kwargs_example(**kwargs):
    print(kwargs)

kwargs_example(apple=100,banana=150,melon=200)

def kwargs_example2(**kwargs):
    if "apple" in kwargs:
        print("apple!")
    else:
        print(":(")
kwargs_example2(apple=10, banana=15)
kwargs_example2(banana=15)

