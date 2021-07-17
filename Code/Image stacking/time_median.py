# median fits function
import time, numpy as np
from astropy.io import fits

def median_fits(list):

  start = time.time()   
  FITSlist = []
  for i in list: 
    hdulist = fits.open(i)
    FITSlist.append(hdulist[0].data)
    hdulist.close()

  FITSstack = np.dstack(FITSlist)
  median = np.median(FITSstack, axis=2)

  memory = FITSstack.nbytes
  memory /= 1024
  
  stop = time.time() - start   
  return median, stop, memory



if __name__ == '__main__':
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])