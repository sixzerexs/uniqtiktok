from PIL import ImageGrab, ImageEnhance, Image
import time

time.sleep(2)
# img_tmp = ImageGrab.grab()
img_tmp = Image.open("template.jpg")


for factor in [0,0.5, 2]:
    img = ImageEnhance.Color(img_tmp).enhance(factor)
    img = ImageEnhance.Contrast(img_tmp).enhance(factor)
    img.save(f'test-Color-{factor}.jpg')