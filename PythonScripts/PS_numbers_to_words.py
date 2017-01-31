#created by taporpone@gmail.com
"""Simple script changing numbers to words - 123 - one hundred twenty three."""
def numberstowords(): ### wrapped it up in a function for looping purposes - see eof
    while True:
        inp = raw_input('Enter a number using digits > ') ###declare variable inp(ut) by user
        def int_check(inp): ### check if var is an int not str or anything else
            try:
                int(inp)
            except ValueError:
                return False
            else:
                return True
        if int_check(inp) == False: ### don't input anything but numbers
            print('You need to provide a number in digits, like 1234, try again')
        elif int(inp) >= 10000: ### We have a 10,000 cap
            print('Provided number is too high. Please enter a number between 0 and 10,000')
        elif str(inp[0]) == '0': ### don't start with 0
            print('Please provide a number that doesn\'t start with 0. 100 is ok, 0100 is not')
        else:
            break
### Dictionaries containing numbers        
    numbersa = { 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven',
12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen',
17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}

    numbersb = {20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70:'seventy', 80: 'eighty', 90: 'ninety'}

    numbersc = {100: 'One hundred', 200: 'Two hundreds', 300: 'Three hundreds', 400: 'Four hundreds', 500: 'Five hundreds', 600: 'Six hundreds', 700: 'Seven hundreds', 800: 'Eight hundreds', 900: 'Nine hundreds'}

    numbersd = {1000: 'One thousand', 2000: 'Two thousands', 3000: 'Three thousands', 4000: 'Four thousands', 5000: 'Five thousands', 6000: 'Six thousands', 7000: 'Seven thousands', 8000: 'Eight thousands', 9000: 'Nine thousands'}
### count length of inp and decide how big the number is 
    inp = str(inp)
    if len(inp) == 1:
        print numbersa[int(inp)].title()

    elif len(inp) == 2:
        if inp == '10':
            print numbersa[10].title()
        elif int(inp) > 10 and int(inp) < 20:
            print numbersa[int(inp)].title()
        elif inp[1] == '0':
            x = int(inp[0]) * 10
            print numbersb[x].title()
        else:
            inp = str(inp)
            x = int(inp[0]) * 10
            y = int(inp[1]) * 1 
            print ('%s %s') % (numbersb[x].title(), numbersa[y])
    elif len(inp) == 3:
        if inp == '100':
            print numbersc[100]
        elif inp[1] == '0' and inp[2] == '0':
            x = int(inp[0]) * 100
            print numbersc[x]
        elif inp[2] == '0':
            x = int(inp[0]) * 100
            y = int(inp[1]) * 10
            print ('%s %s') % (numbersc[x],numbersb[y])
        elif inp[1] == '0' and inp[2] != '0':
            x = int(inp[0]) * 100
            y = int(inp[2]) * 1
            print ("%s %s") %(numbersc[x], numbersa[y])
        else:
            inp = str(inp)
            x = int(inp[0]) * 100
            y = int(inp[1]) * 10
            z = int(inp[2]) * 1
            print ('%s %s %s') % (numbersc[x],numbersb[y],numbersa[z])
    elif len(inp) == 4:
        if inp == '1000':
            print numbersd[1000]
        elif inp[3] == '0' and inp[2] == '0' and inp[1] == '0':
            x = int(inp[0]) * 1000
            print numbersd[x]
        elif inp[0] != '0' and inp[1] == '0' and inp[2] != '0' and inp[3] == '0':
            x = int(inp[0]) * 1000
            y = int(inp[2]) * 10
            print ('%s %s') % (numbersd[x],numbersb[y])
        elif inp[0] != '0' and inp[1] == '0' and inp[2] == '0' and inp[3] != '0':
            x = int(inp[0]) * 1000
            y = int(inp[3]) * 1
            print ('%s %s') % (numbersd[x],numbersa[y])
        elif inp[3] == '0':
            x = int(inp[0]) * 1000
            y = int(inp[1]) * 100
            z = int(inp[2]) * 10
            print ('%s %s %s') %(numbersd[x],numbersc[y], numbersb[z])
        elif inp[2] == '0' and inp[3] != '0':
            x = int(inp[0]) * 1000
            y = int(inp[1]) * 100
            z = int(inp[3]) * 1
            print('%s %s %s')%(numbersd[x],numbersc[y],numbersa[z])
        elif inp[1] == '0' and inp[2] != '0' and inp[3] != '0':
            x = int(inp[0]) * 1000
            y = int(inp[2]) * 10
            z = int(inp[3]) * 1
            print('%s %s %s')%(numbersd[x],numbersb[y],numbersa[z])
        else:
            inp = str(inp)
            x = int(inp[0]) * 1000
            y = int(inp[1]) * 100
            z = int(inp[2]) * 10
            q = int(inp[3]) * 1
            print ('%s %s %s %s') %(numbersd[x],numbersc[y], numbersb[z],numbersa[q])
while True: ### loop whole script
    numberstowords() ### call the script in a loop
    if raw_input('Another one? [y/n]') != 'y': ### loop or escape
        break
    else:
        pass
print('The program will now close') # bye message
