# This function clears the terminal screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).
# Severance, C. (2016). Python for Everybody: Exploring Data Using Python 3. a Creative Commons Attribution.
print ('This program calculates gross pay to /n demonstrate the use of functions.')
h = float(
    input('Enter Hours: '))
r = float(
    input('Enter Rate: '))
def computepay (h, r):
    return h * r
if h > 40:
    def ot (h, r):
        return (h - 40) * (r * 1.5)

    print (f'Pay {((computepay(40, r)) + ot(h, r)):.2f}')
else:
    print (f'Pay {computepay(h, r):.2f}')