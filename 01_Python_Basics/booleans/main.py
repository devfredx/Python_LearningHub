a=4
b=2
c=12
d=12
e=13
f=14
print(a > b)
print(c == d)
print(f < e)

if b > a:
    print(b, " " + "greater than ",a)
else:
    print(b, " " + "not greater than ",a)

print(bool(""))
print(bool(0))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")