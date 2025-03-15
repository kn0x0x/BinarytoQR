# Binary to QR Code Generator

A simple tool to convert a binary string into a QR code image using Python.

## Description
This script takes a binary string (e.g., from a text file) and generates a 25x25 QR code image, where `1` is black and `0` is white.

## Usage
1. Provide a 625-bit binary string.
2. Run the script to generate a QR image saved as `qr.png`.

### Script
```python
from PIL import Image

bitstring = "1111111000011110101111111100000100110101100100000110111010110110111010111011011101010101001101011101101110101001010010101110110000010100101111010000011111111010101010101111111000000001011110100000000010111110001110110011111000111011101100000010100000100011110111100101110111100000100001010100010000011000001000000001011011111100010001010111011100011010100010101001111100110111011100001001100110000011100001100110101011111111100000000110000001000110101111111001111001101010011100000101101001010001000010111010111100011111111011011101011001110011010011101110101010011110010010110000010011011001011100011111111010101010000010111"
size = 25

img = Image.new('1', (size, size))
pixels = img.load()
for i in range(size):
    for j in range(size):
        pixels[j, i] = int(bitstring[i * size + j])
img.save('qr.png')
