while True:

    print("\n1. Calculate grade based on exam score")
    print("2. Check score range based on grade")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        try:
            score = int(input("\nEnter your exam score: "))

            if score == 100:
                grade = 'A+'
            elif score >= 85 and score < 100:
                grade = 'A'
            elif score >= 70 and score < 85:
                grade = 'B+'
            elif score >= 60 and score < 70:
                grade = 'B'
            elif score >= 50 and score < 60:
                grade = 'C+'
            elif score >= 40 and score < 50:
                grade = 'C'
            elif score >= 20 and score < 40:
                grade = 'D'
            elif score >= 0 and score < 20:
                grade = 'F'
            else:
                grade = 'Invalid score. Score must be between 0 and 100.'

            print("Your grade is:", grade)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == '2':
        grade = input("Enter your grade: ")

        if grade == 'A+':
            score_range = '100'
        elif grade == 'A':
            score_range = '99-85'
        elif grade == 'B+':
            score_range = '84-70'
        elif grade == 'B':
            score_range = '69-60'
        elif grade == 'C+':
            score_range = '59-50'
        elif grade == 'C':
            score_range = '49-40'
        elif grade == 'D':
            score_range = '39-20'
        elif grade == 'F':
            score_range = '19-0'
        else:
            score_range = 'Invalid grade.'

        print("\nYour score range for grade", grade, "is:", score_range)

    else:
        print("Invalid choice.")

    another_action = input("\nDo you want to take another action? (y/n): ")
    if another_action.lower() != 'y':
        break
