numbers = [1, 2, 3, 4]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

text = "PYTHON"
text_iter = iter(text)

print(next(text_iter))
print(next(text_iter))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_class = MyNumbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

for num in Countdown(3):
    print(num)

data = [10, 20, 30]
data_iter = iter(data)
while True:
    try:
        item = next(data_iter)
        print(item)
    except StopIteration:
        break