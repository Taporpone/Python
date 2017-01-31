import sys

class Occurance:
    def __init__(self,alphabet,word):
        self.alphabet = alphabet
        self.word = word

    def sharp_representation(self,value,word):
        if len(word) < 500:
            sharp = '#' * value
            return sharp
        if len(word) >= 500 and len(word) < 1000:
            sharp = '#' * int(value/2)
            return sharp
        if len(word) >= 1000 and len(word) < 3000:
            sharp = '#' * int(value/3)
            return sharp
        else:
            sharp = '#' * int(value/4)
            return sharp

    def counter(self):
        for item in self.word:
            if item.lower() in alphabet:
                self.alphabet[item.lower()] += 1

    def printer(self):
        for key,value in sorted(self.alphabet.items()):
            if value != 0:
                sharp = Occurance.sharp_representation(self,value,self.word)
                print('%s: %d %s') % (key,value,sharp)

alphabet = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"w":0,"x":0,"y":0,"z":0}

def intro_screen():
    word = raw_input("Please provide a phrase you would like to process\n> ")
    return word

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


if len(sys.argv) == 1:
    word = intro_screen()
    inst = Occurance(alphabet,word)
    inst.counter()
    inst.printer()
else:
    input_file = sys.argv[1]
    line_count = file_len(input_file) - 1 #Starting from 0 not 1
    n = 0
    while n <= line_count:
        with open('dupadupa') as f:
            lines = f.readlines()
            word = lines[n]
            inst = Occurance(alphabet,word)
            inst.counter()
            print('Line %d of %d processed!') %(n + 1,line_count + 1) #Although we start from 0, printable version is 'human oriented'
        n += 1
    inst.printer()
