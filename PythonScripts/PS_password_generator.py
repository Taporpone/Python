#
##Script generates a random password, operates in quick mode for a quickie pass and in detailed mode
#Works on OSX. As for other platforms, no idea.
#
import string # string generator (Ab1!)
import random # random engine
import subprocess

#def copy to clipboard func

def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait

#define random str generator function

def generator(size,chars):
    return(''.join(random.choice(chars) for _ in range(size)))

password = []
first_choice = raw_input('To generate a random password press \'Enter\', type \'m\' for more options >  ')
if first_choice == 'm': #user wants to use detailed mode and set up his password
    while True:
        no_of_chars = raw_input('How many characters would you like to use(5 - 50)? >  ')
        if int(no_of_chars) > 50: #start checking if password is in range 5 -50
            print 'Too many. Maximum # of characters is set to 50'
        elif int(no_of_chars) < 5:
            print 'Too few. Minimum # of characters is set to 5!'
        else:
            break
    while True: # if above tests passed, ask user questions about pass he wants
        characters = '' #start with empty var so if first question answered n, script wont break

        answer_upper = raw_input('Would you like your password to consist of upper case letters? (y/n) >  ')
        if answer_upper == 'y':
            characters += string.ascii_uppercase #if answered y, append upercase chars to characters var
            print('Added upper case letters to the mix!\n')
        else:
            pass

        answer_lower = raw_input('Would you like your password to consist of lower case letters? (y/n) >  ')
        if answer_lower == 'y':
            characters += string.ascii_lowercase
            print('Added lower case letters to the mix!\n')
        else:
            pass

        answer_digits = raw_input('Would you like your password to consist of digits? (y/n) >  ')
        if answer_digits == 'y':
            characters += string.digits
            print('Added digits to the mix!\n')
        else:
            pass

        answer_special = raw_input('Would you like your password to consist of special chars (i.e. #!>@)? (y/n) >  ')
        if answer_special == 'y':
            characters += string.punctuation
            print('Added specials to the mix!\n')
        else:
            pass

        if characters == '':
            print('\nSorry, you need to say \'y\' to at least one choice!\n')
        else:
            break

    data = generator(int(no_of_chars),characters) #store in data var so it can be copied to clipboard
    print 'Password:' + data
    setClipboardData(data)
    print('Copied to clipboard!')
else: #quick password mode, just print some random pass
    size = 18
    chars = string.ascii_letters + string.digits + string.punctuation
    data = generator(size,chars)
    print 'Password:' + data
    setClipboardData(data)
    print('Copied to clipboard!')
