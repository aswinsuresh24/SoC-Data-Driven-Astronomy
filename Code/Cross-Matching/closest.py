#Function
import numpy as np
def import_bss():
  b=[]
  cat=np.loadtxt('bss.dat',usecols=range(1,7))
  for i in range(0,len(cat)):
    ra=cat[i][0]*15+cat[i][1]/4+cat[i][2]/240
    if cat[i][3]>0:
      dec=cat[i][3]+cat[i][4]/60+cat[i][5]/3600
    else:
      dec=cat[i][3]-cat[i][4]/60-cat[i][5]/3600
    b.append((i+1,ra,dec))
  return b

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

def find_closest(list,a,b):
  mindist=angular_dist(list[0][1],list[0][2],a,b)
  index=1
  for i in range(1,len(list)):
    d=angular_dist(list[i][1],list[i][2],a,b)
    if d<mindist:
      mindist=d
      index=i+1
      
  return index,mindist
  
  

if __name__ == '__main__':
  cat = import_bss()
  
  print(find_closest(cat, 175.3, -32.5))

  print(find_closest(cat, 32.2, 40.7))