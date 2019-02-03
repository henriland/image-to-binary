import os
import sys
import binascii

filename = sys.argv[1]
with open(filename, 'rb') as file:
    image_data = file.read()

data = binascii.hexlify(image_data)

binary = bin(int(data, 16))
binary = binary[2:].zfill(32)

parsed_filename = os.path.splitext(os.path.basename(filename))[0]
binary_filename = parsed_filename + '.bin'
with open(binary_filename, 'wb') as file:
    file.write(binary.encode());