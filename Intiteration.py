# This function clears the terminal screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Exercise 5.1: Write a program that repeatedly reads integers until the user enters
# “done”. Once “done” is entered, print out (the total, count, and average revised out) the maximum and the minimum of the
# integers. If the user enters anything other than an integer, detect their mistake
# using try and except and print an error message and skip to the next integers.
# Severance, C. (2016). Python for Everybody: Exploring Data Using Python 3. a Creative Commons Attribution.
n = int(0)
s = int(0)
mini = None
maxi = None
while True:
    i = input('Enter a number or type "done" if finished: ')
    if i == 'done':
        break
    try:
        i = int(i)
        n = n + 1
        s = s + i
        if maxi is None:
            maxi = i
        if i > maxi:
            maxi = i 
        if mini is None:
            mini = i
        if i < mini:
            mini = i
    except:
        print ('Invalid input')
        continue
#print ('ALL DONE')
#print ('Total:', s)
#print ('Count:', n)
#print ('Average:', s / n)
print ('Maximum is', (maxi))
print ('Minimum is', (mini))