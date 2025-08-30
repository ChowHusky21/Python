# This function clears the terminal screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
# This program converts a score between 0.00 and 1.00 into a letter grade
while True:
    scorei = input("Enter score between 0.00 and 1.00: ")
    score = float(scorei)
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            print(f"The grade for {score:f2} is an A")
        elif score >= 0.8:
            print(f"The grade for {score:f2} is a B")
        elif score >= 0.7:
            print(f"The grade for {score:f2} is a C")
        elif score >= 0.6:
            print(f"The grade for {score:f2} is a D")
        else:
            print(f"The grade for {score:f2} is an F")
        break
    else:
        print(f"Error, {score:f2} entered was not between 0.00 and 1.00.")
quit()
