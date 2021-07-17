#Functions
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

def import_super():
  s=[]
  cat=np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0,1])
  for i in range(0,len(cat)):
    s.append((i+1,cat[i][0],cat[i][1]))
  return s
    
  
  


if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)