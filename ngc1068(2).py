import numpy as np
import  matplotlib
import astropy
import matplotlib.pyplot as plt
from astropy.utils.data import download_file
from astropy.io import fits

hdu_list = fits.open('791wmos.fits')
hdu = hdu_list[0].data
n = hdu.shape
print(n[0]) #ширина зображення
print(n[1]) #висота зображення

print(type(hdu))
print(hdu[5][4])



