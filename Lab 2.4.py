from rasterio.plot import show
import geos
import tensorflow
import rasterio
import geotiff
import tifffile
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing.image import load_img
from keras import src
from keras.preprocessing.image import img_to_array
from keras import src
import cv2
from PIL import Image
# Open the GeoTIFF image
red= rasterio.open("C:\\Users\\ASUS PC\\PycharmProjects\\pythonProject\\Data\\lab2\\shB4.tif")
ir= rasterio.open("C:\\Users\\ASUS PC\\PycharmProjects\\pythonProject\\Data\\lab2\\shB5.tif")
imgred=red.read(1).astype(float)
imgir=ir.read(1).astype(float)
"For error handling for 0 in divisor"
ndvi=(imgir-imgred)/(imgir+imgred)
"close the dataset"
red.close()
ir.close()
plt.title("NDVI of sanghar ")
plt.imshow(ndvi, cmap='viridis')
plt.colorbar()
plt.show()
