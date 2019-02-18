import numpy as np
import  matplotlib
import astropy
import matplotlib.pyplot as plt
from astropy.utils.data import download_file
from astropy.io import fits
from matplotlib.colors import LogNorm

image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)
hdu_list = fits.open(image_file) #відкриваємо скачаний fits файл
hdu_list.info() #що знаходиться в fits файлі
image_data = hdu_list[0].data #поміщаємо дані в двовимірний масив
print(type(image_data))
n = image_data.shape
print(n[0]) #щоб дізнатися розміри зображення

#plt.imshow(image_data, cmap='gray') #перегляд даних зображення
#plt.colorbar()

#базова статистика
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

#відображення даних в логарифмічній шкалі
plt.imshow(image_data, cmap='gray', norm=LogNorm())
plt.show()

#гістограма
#щоб створити гістограму matplot.pyplot.hist() треба
#перетворити дані з двовимірного масиву в одновимірний ndarray.flatten()
#print(type(image_data.flatten()))
#NBINS = 1000
#histogram = plt.hist(image_data.flatten(), NBINS)
#plt.show()
hdu_list.close()