from PIL import Image

img = Image.open('init.png')
imgGray = img.convert('L')
imgGray.save('test_gray.png')