x = 0
while x < 10:
    print(x)
    x = x + 10

list1 = [10,20,30,40,50]
while 20 in list1:
    print("20 in 'list1'")
    list1.remove(20)
print()

list2 = [10,20,30,40,50]
while 20 in list2:
    print("20 in 'list2'")
    list2.pop()

list3 = [10,20,30,40,50]
print(f"list3 {list3}")

name = input("enter name: ")
print(f"welcome {name}")

p = 0
while p < 20:
    print(f"value of p: {p}")
    p +=2