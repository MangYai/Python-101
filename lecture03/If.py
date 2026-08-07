score1 = int(input("Enter your score for test 1: "))
score2 = int(input("Enter your score for test 2: "))
score3 = int(input("Enter your score for test 3: "))
average = (score1 + score2 + score3) / 3
    
print(f"Your average score is: {average}")

if average >= 95:
    print("congratulations!")
    print("You have a high average score!")

    