import os
import sys
import binascii

filename = sys.argv[1]
binFile = open(filename,'rb')
binaryData = binFile.read()
hexData = '%0*X' % ((len(binaryData) + 3) // 4, int(binaryData, 2))
hexData = hexData.decode('hex')

parsed_filename = os.path.splitext(os.path.basename(filename))[0]
png_filename = parsed_filename + '_from_binary.png'
with open(png_filename, 'wb') as file:
    file.write(hexData)