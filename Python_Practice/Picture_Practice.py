"""
图片读取与处理
pillow操作图像
"""
from PIL import Image,ImageFilter

image = Image.open('006.jpg')
# 旋转
# image.rotate(180).show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()
# 滤镜效果
image.filter(ImageFilter.CONTOUR).show()
