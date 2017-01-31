###
###Decrypt binary to characters
###
###

class WelcomeScreen():
    def __init__(self):
        pass
    def menu(self):
        menuLoop = True
        while menuLoop:
            print "\n\tWelcome to binary to letters converter\n"
            print "1. Convert from binary to text"
            print "2. Convert from text to binary\n"
            user_choice = raw_input("> ")
            if user_choice in ("1","2"):
                return user_choice


class ValidateDecrypt():
    def __init__(self):
        pass
    def info(self):
        print """\nWelcome to Binary2Letters converter. \n\nPaste your binary code in blocks of 8 digits consisting of 0 and 1.\nSeparate blocks using space.\nExample: 00001111 00001111 00001111\n\n"""
    def userInput(self):
        user_input = raw_input("Paste binary(0 or 1 or space)\n>")
        return user_input
    def validateInput(self,user_input):
        validation_Fail = False
        for char in user_input:
            if char not in ("0","1"," "):
                print "\nERROR::Use only 0,1 and space\n"
                validation_Fail = True
                return validation_Fail
        return validation_Fail
    def integrityInput(self,user_input):
        user_input = user_input.split(" ")
        integrityFail = False
        block = 0
        while block < len(user_input):
            if len(user_input[block]) != 8:
                print "\nERROR::Make sure each block is exeactly 8 digits!\n"
                integrityFail = True
                return integrityFail
            else:
                block +=1
        return integrityFail

class Decrypt():
    def __init__(self):
        self.ascii = {"32":" ","33":"!","34":'"',"35":"#","36":"$","37":"%","38":"&","39":"'","40":"(","41":")","42":"*","43":"+","44":",","45":"-","46":".","47":"/","48":"0","49":"1","50":"2","51":"3","52":"4","53":"5","54":"6","55":"7","56":"8","57":"9","58":":","59":";","60":"<","61":"=","62":">","63":"?","64":"@","65":"A","66":"B","67":"C","68":"D","69":"E","70":"F","71":"G","72":"H","73":"I","74":"J","75":"K","76":"L","77":"M","78":"N","79":"O","80":"P","81":"Q","82":"R","83":"S","84":"T","85":"U","86":"V","87":"W","88":"X","89":"Y","90":"Z","91":"[","92":"\\","93":"]","96":"`","97":"a","98":"b","99":"c","100":"d","101":"e","102":"f","103":"g","104":"h","105":"i","106":"j","107":"k","108":"l","109":"m","110":"n","111":"o","112":"p","113":"q","114":"r","115":"s","116":"t","117":"u","118":"v","119":"w","120":"x","121":"y","122":"z","123":"{","124":"|","125":"}"}
    def transformToNumber(self,block):
        summ = 0
        exp = [128,64,32,16,8,4,2,1]
        for item in range(8):
            if block[item] == "1":
                summ += exp[item]
        return summ
    def transformToLetters(self,summ):
        letters = []
        for item in summ:
            try:
                letters.append(self.ascii[str(item)])
            except KeyError:
                letters.append("?_?")
        letters = " ".join(letters)
        return letters

class Encrypt():
    def __init__(self):
        self.ascii = {' ': '32', '$': '36', '(': '40', ',': '44', '0': '48', '4': '52', '8': '56', '<': '60', '@': '64', 'D': '68', 'H': '72', 'L': '76', 'P': '80', 'T': '84', 'X': '88', '\\': '92', '`': '96', 'd': '100', 'h': '104', 'l': '108', 'p': '112', 't': '116', 'x': '120', '|': '124', '#': '35', "'": '39', '+': '43', '/': '47', '3': '51', '7': '55', ';': '59', '?': '63', 'C': '67', 'G': '71', 'K': '75', 'O': '79', 'S': '83', 'W': '87', '[': '91', 'c': '99', 'g': '103', 'k': '107', 'o': '111', 's': '115', 'w': '119', '{': '123', '"': '34', '&': '38', '*': '42', '.': '46', '2': '50', '6': '54', ':': '58', '>': '62', 'B': '66', 'F': '70', 'J': '74', 'N': '78', 'R': '82', 'V': '86', 'Z': '90', 'b': '98', 'f': '102', 'j': '106', 'n': '110', 'r': '114', 'v': '118', 'z': '122', '!': '33', '%': '37', ')': '41', '-': '45', '1': '49', '5': '53', '9': '57', '=': '61', 'A': '65', 'E': '69', 'I': '73', 'M': '77', 'Q': '81', 'U': '85', 'Y': '89', ']': '93', 'a': '97', 'e': '101', 'i': '105', 'm': '109', 'q': '113', 'u': '117', 'y': '121', '}': '125'}
    def userInput(self):
        user_input = raw_input("Provide a string to be converted to binary: \n>")
        return user_input
    def inputDecimal(self,user_input):
        decimal = []
        index = 0
        for item in user_input:
            try:
                decimal.append(self.ascii[item])
            except KeyError:
                pass
        return decimal
    def inputBinary(self,decimal):
        binary = []
        for item in decimal:
            res = []
            x = int(item)
            for operand in [128,64,32,16,8,4,2,1]:
                if x >= operand:
                    x = x - operand
                    res.append("1")
                else:
                    res.append("0")
            binary.append(res)

        return binary



###Present welcome screen, grab user choice

user_choice = WelcomeScreen().menu()

if user_choice == "1":

    ValidateDecrypt().info() ###Display usage hints

    validation_Result = True
    integrity_Result = True
    while validation_Result or integrity_Result: ###User input loop, break when input is valid
        user_input = ValidateDecrypt().userInput()
        validation_Result = ValidateDecrypt().validateInput(user_input)
        integrity_Result = ValidateDecrypt().integrityInput(user_input)

    user_input = user_input.split(" ")
    cleared = []

    for item in user_input:
        cleared.append(Decrypt().transformToNumber(item))

    to_print = Decrypt().transformToLetters(cleared) ###Print final version
    

else:

    user_input = Encrypt().userInput()

    input_decimal = Encrypt().inputDecimal(user_input)
    output = Encrypt().inputBinary(input_decimal)
    cleared_output = []
    for item in output:
        printable =  " ".join(item)
        cleared_output.append(printable.replace(" ",""))

    print " ".join(cleared_output)
