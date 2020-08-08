 #Flipping the image
from PIL import Image
import cv2
# img = Image.open('test.jpg')
# #transposing
# transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
# transposed_img.save('corrected.jpg')
img=cv2.imread('test1.jpg')
clahe=cv2.createCLAHE()
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
enh_img=clahe.apply(gray_img)
cv2.imwrite('enhanced.jpg',enh_img)