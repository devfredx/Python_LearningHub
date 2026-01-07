print("Welcome to the General Knowledge Quiz!")

total_questions = 5
correct_answers = 0

print("\nQuestion 1: What is the largest planet in our solar system?")
print("a) Venus")
print("b) Jupiter")
print("c) Saturn")
answer1 = input("Your answer: ")
if answer1.lower() == "b":
    correct_answers += 1

print("\nQuestion 2: Who painted the Mona Lisa?")
print("a) Leonardo da Vinci")
print("b) Vincent van Gogh")
print("c) Pablo Picasso")
answer2 = input("Your answer: ")
if answer2.lower() == "a":
    correct_answers += 1

print("\nQuestion 3: What is the tallest mammal in the world?")
print("a) Elephant")
print("b) Giraffe")
print("c) Hippopotamus")
answer3 = input("Your answer: ")
if answer3.lower() == "b":
    correct_answers += 1

print("\nQuestion 4: Which planet is known as the Red Planet?")
print("a) Venus")
print("b) Mars")
print("c) Jupiter")
answer4 = input("Your answer: ")
if answer4.lower() == "b":
    correct_answers += 1

print("\nQuestion 5: Who was the first man to walk on the moon?")
print("a) Neil Armstrong")
print("b) Buzz Aldrin")
print("c) Yuri Gagarin")
answer5 = input("Your answer: ")
if answer5.lower() == "a":
    correct_answers += 1


print("\nThanks for playing the General Knowledge Quiz!")
print("You got", correct_answers, "out of", total_questions, "questions correct.")
