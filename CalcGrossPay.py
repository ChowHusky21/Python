# This function clears the terminal screen
import os
os.system('cls' if os.name == 'nt' else 'clear')
# This program calculates gross pay for one week in California
# It accounts for overtime pay (over 40) and double time (over 60)
# It also accounts for hours over 12 in a day (double time)
hrsi = input('Enter Hours:')
hrs = float(hrsi)
ratei = input('At what hourly rate of pay?')
rate = float(ratei)
while True:
    over8i = input('Were any of the hours in a day more than 8 hours,\n but less than 12 hours?\nEnter Y for yes or N for no:')
    if over8i == 'Y' or over8i == 'N':
        if over8i == 'Y':
            timenhalfi = input('For any given day worked less than 12 hours,\n how many hours were over 8 hours?')
            timenhalf = float(timenhalfi)
            grosshalf = timenhalf * (rate * 1.5)
        elif over8i == 'N':
            overtime = float(0)
            grosshalf = float(0)
    while True:
        over12i = input('Were any of the hours in a day more than 12 hours?\nEnter Y for yes or N for no:')
        if over12i == 'Y' or over12i == 'N':
            if over12i == 'Y':
                dubtimei = input('How many hours were after 12 hours in a day?')
                dubtime = float(dubtimei)
                grossdub = (((dubtime - 4) * (rate * 2)) + (4 * (rate * 1.5)))
            elif over12i == 'N':
                dubtime = float(0)
                grossdub = float(0)
        else:
            print ("Error, the answer entered was not a Y or an N")
        if (hrs - timenhalf - dubtime) <= 40:
            gross = ((hrs - timenhalf - dubtime) * rate)
        elif (hrs - timenhalf - dubtime) <= 60:
            gross = (((40) * rate) + ((hrs - 40) * (rate * 1.5)))
        else: 
            gross = (((40) * rate) + (20 * (rate * 1.5))  + ((hrs - 60) * (rate * 2)))
        print (f'The gross pay is ${gross + grosshalf + grossdub:.2f}')
        quit()
