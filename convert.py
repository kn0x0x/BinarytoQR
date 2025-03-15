from PIL import Image

# Binary string
bitstring = ""

# Grid size
size = 25

# Create a 1-bit (black and white) image
img = Image.new('1', (size, size))
pixels = img.load()

# Fill in pixels from the binary string
for i in range(size):
    for j in range(size):
        index = i * size + j
        pixels[j, i] = int(bitstring[index])

# Save the image
img.save('qr.png')
