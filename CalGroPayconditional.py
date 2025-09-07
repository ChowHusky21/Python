# This function clears the terminal screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).
# Severance, C. (2016). Python for Everybody: Exploring Data Using Python 3. a Creative Commons Attribution.
print ('This program calculates gross pay to /n demonstrate the use of conditional executions.')
h = float(
    input('Enter Hours: '))
r = float(
    input('Enter Rate: '))
if h > 40:
    print (f'Pay {(40 * r) + ((h - 40) * (r * 1.5)):.2f}')
else:
    print (f'Pay {(h * r):.2f}')