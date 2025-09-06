# This function clears the terminal screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
# This program calculates gross pay to demonstrate the use of functions
h = float(input('Enter Hours: '))
r = float(input('Enter Rate: '))
def computepay (h, r):
    return h * r
if h > 40:
    def ot (h, r):
        return (h - 40) * (r * 1.5)
    print (f'Pay {((computepay(40, r)) + ot(h, r)):.2f}')
else:
    print (f'Pay {computepay(h, r):.2f}')