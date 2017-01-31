"""Simple module retirning qr code in root folder
Based on: PyQRCode : https://pypi.python.org/pypi/PyQRCode : 'pip install pyqrcode'
"""

import pyqrcode
import png

def create_qr():
    inn = raw_input('To be qr\'ed:\n> ')
    code_name = raw_input('Set filename(without extension):\n> ')
    data = pyqrcode.create(inn)
    with open('code.png', 'w') as inputfile:
        data.png(inputfile, scale =5)

    #data.svg(code_name + '.svg',scale=8)

if __name__ == "__main__":
    create_qr()
