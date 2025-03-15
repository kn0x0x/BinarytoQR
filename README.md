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

bitstring = ""
size = 25

img = Image.new('1', (size, size))
pixels = img.load()
for i in range(size):
    for j in range(size):
        pixels[j, i] = int(bitstring[i * size + j])
img.save('qr.png')
