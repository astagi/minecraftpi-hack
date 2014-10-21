from PIL import Image

im = Image.open('nephilalogo.png')
pixels = im.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        pixel = pixels[i,j]

