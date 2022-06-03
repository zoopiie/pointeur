from PIL import Image, ImageTk

image = Image.open("chatcasse.png")
resize_image = image.resize((200, 200))
resize_image.save("cible.png")