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
# Open the GeoTIFF image
img= rasterio.open("C:\\Users\\ASUS PC\\PycharmProjects\\PythonProjects\\Data\\lab2\\composite.tif")

width = img.width
height = img.height
print("Image Size (Width x Height):", width, "x", height)

num_bands = img.count
print("Number of Bands:", num_bands)
metadata=img.meta
print("metadata = ",metadata)
des=img.descriptions
print("descriptions =",des)
crs=img.crs
print("crs=",crs)
rasterio.plot.show_hist(img, bins=50, histtype='stepfilled', lw=0.0, stacked=False, alpha=0.3)
