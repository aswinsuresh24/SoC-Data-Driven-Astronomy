# load_fits function
from astropy.io import fits
import numpy as np
def load_fits(str):
  hdulist=fits.open(str)
  data=hdulist[0].data
  shp=data.shape
  index=np.argmax(data)
  brightness_max=np.unravel_index(index,shp)
  return brightness_max
  
  
  




if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()