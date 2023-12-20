from rasterio.plot import show
import geos
import tensorflow
import rasterio
import geotiff
import tifffile
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import cv2
from PIL import Image

"Reading multiple bands"
img = Image.open("C:\\Users\\ASUS PC\\PycharmProjects\\pythonProject\\Data\\Lab 2\\SangharB2.tif")
img2 = Image.open("C:\\Users\\ASUS PC\\PycharmProjects\\pythonProject\\Data\\Lab 2\\SangharB3.tif")
img3 = Image.open("C:\\Users\\ASUS PC\\PycharmProjects\\pythonProject\\Data\\Lab 2\\SangharB4.tif")
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2, 2, 1)
fig2 = plt.figure(figsize=(10, 10))
ax2 = fig2.add_subplot(2, 2, 2)
fig3 = plt.figure(figsize=(10, 10))
ax3 = fig3.add_subplot(2, 2, 3)
ax1.imshow(img, cmap='Blues')
ax2.imshow(img2,cmap='Greens')
ax3.imshow(img3,cmap='Reds')
plt.show()
