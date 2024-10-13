# Lab 5 - Numerical Conversion
def hex_char_decode(hexnumber):
    i = hexnumber
    if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        ii = int(i)
        return ii
    elif i == 'A' or i == 'a':
        ii = 10
        return ii
    elif i == 'B' or i == 'b':
        ii = 11
        return ii
    elif i == 'C' or i == 'c':
        ii = 12
        return ii
    elif i == 'D' or i == 'd':
        ii = 13
        return ii
    elif i == 'E' or i == 'e':
        ii = 14
        return ii
    elif i == 'F' or i == 'f':
        ii = 15
        return ii
    else:
        return 0

def hex_string_decode(hex_string_):
    hex_string_ = list(hex_string_)
    if hex_string_[0:2] == ['0', 'x'] or hex_string_[0:2] == ['0', 'X']:
        hex_string_ = hex_string_[2:]
    hex_string_.reverse()
    n = 0
    decimal = 0
    for i in hex_string_:
        decimal += hex_char_decode(i) * 16 ** n
        n += 1
    return decimal

def binary_string_decode(binary):
   binary = list(binary)
   if binary[0:2] == ['0','b'] or binary[0:2] == ['0','B']:
       binary = binary[2:]
   binary.reverse()
   n = 0
   decimal = 0
   for i in binary:
       decimal += int(i) * 2 ** n
       n += 1
   return decimal

def binary_to_hex(binary):
    binary = list(str(binary))
    if binary[0:2] == ['0', 'b']:
        binary = binary[2:]
    while len(str(binary)) % 4:
        binary = ['0'] + binary
    hex = ''
    for i in range(0,len(binary),4):
        block = binary[i:i+4]
        block = ''.join(block)
        decimal = binary_string_decode(block)
        if decimal in range(10):
            hex += str(decimal)
        elif decimal == 10:
            hex += 'A'
        elif decimal == 11:
            hex += 'B'
        elif decimal == 12:
            hex += 'C'
        elif decimal == 13:
            hex += 'D'
        elif decimal == 14:
            hex += 'E'
        elif decimal == 15:
            hex += 'F'
    return hex


while True:
    print('Decoding Menu', '-------------', '1. Decode hexadecimal', '2. Decode binary','3. Convert binary to hexadecimal', '4. Quit', '', sep='\n')
    choice = int(input('Please enter an option: '))
    if choice == 1:
        hex_string = input('Please enter the numeric string to convert: ')
        result = hex_string_decode(hex_string)
        print(f"Result: {result}", end ='\n\n')
        continue
    elif choice == 2:
        bin_string = input('Please enter the numeric string to convert: ')
        result = binary_string_decode(bin_string)
        print(f"Result: {result}", end ='\n\n')
        continue
    elif choice == 3:
        bin_string = input('Please enter the numeric string to convert: ')
        result = binary_to_hex(bin_string)
        print(f"Result: {result}", end ='\n\n')
        continue
    elif choice == 4:
        print('Goodbye!')
        break
    else:
        print('Please enter a valid option.')
        continue