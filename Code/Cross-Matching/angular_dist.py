#Function:
import numpy as np
def angular_dist(ra1,dec1,ra2,dec2):
  r1=np.radians(ra1)
  r2=np.radians(ra2)
  d1=np.radians(dec1)
  d2=np.radians(dec2)
  a=np.sin(np.abs(d1-d2)/2)**2
  b=np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1-r2)/2)**2
  d=2*np.arcsin(np.sqrt(a+b))
  d=np.degrees(d)
  return d



if __name__ == '__main__':
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  print(angular_dist(10.3, -3, 24.3, -29))