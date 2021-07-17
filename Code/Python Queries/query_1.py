# Query function:
import numpy as np

def query(str):
  cat=np.loadtxt('%s' %str, delimiter=',', usecols=[0,2])
  cat_rad=[]
  for i in range(0,len(cat)):
    if(cat[i][1]>1.0):
      cat_rad.append(cat[i])
      
  cat_rad=np.array(cat_rad)
    
  return cat_rad



if __name__ == '__main__':
  result = query('stars.csv')