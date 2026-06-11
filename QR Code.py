# pip install pillow
import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=KHYfygE9FYc")
img.save("Tom_youtube.png")

