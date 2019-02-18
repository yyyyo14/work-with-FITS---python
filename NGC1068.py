import numpy as np
import  matplotlib
import astropy
import matplotlib.pyplot as plt
from astropy.utils.data import download_file
from astropy.io import fits


hdu_list = fits.open('791wmos.fits')
hdu_list.info()
hdu = hdu_list[0]
hdu.header['MODIFIED'] = '03 Feb 2019' #додає нове ключове слово
print(hdu.header)
#print( hdu.header['HISTORY'])
hdu = hdu_list[0].data
plt.imshow(hdu, cmap='gray')
plt.show()
#hdu_list.writeto('separatefile.fits') #записати hdu в окремий файл