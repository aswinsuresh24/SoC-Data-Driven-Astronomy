# fits mean function:
from astropy.io import fits
import numpy as np
def mean_fits(list):
  l=len(list)
  data=(fits.open(list[0])[0]).data
  for i in range(1,len(list)):
    data+=(fits.open(list[i])[0]).data
   
  return data/l
  




if __name__ == '__main__':
  
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # Plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()