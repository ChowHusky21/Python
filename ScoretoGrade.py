# This function clears the terminal screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
# This program converts a score between 0.00 and 1.00 into a letter grade
while True:
    scorei = input("Enter score between 0.00 and 1.00: ")
    score = float(scorei)
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            print("The grade for {score} is an A")
        elif score >= 0.8:
            print("The grade for {score} is a B")
        elif score >= 0.7:
            print("The grade for {score} is a C")
        elif score >= 0.6:
            print("The grade for {score} is a D")
        else:
            print("The grade for {score} is an F")
        break
    else:
        print("Error, the score entered was not between 0.00 and 1.00.")
quit()
