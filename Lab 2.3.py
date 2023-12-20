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
from keras import src
from keras.preprocessing.image import img_to_array
from keras import src
import cv2
from PIL import Image
# Open the GeoTIFF image
img= rasterio.open("C:\\Users\\ASUS PC\\PycharmProjects\\PythonProjects\\Data\\lab2\\composite.tif")
img_data=img.read()
clipped_img = img_data[:, 300:900, 300:900]
plt.imshow(clipped_img.transpose(1, 2, 0))
plt.show()
