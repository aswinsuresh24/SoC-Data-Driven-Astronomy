# Function
import numpy as np

def query(str):
  cat=np.loadtxt('%s' %str, delimiter=',', usecols=[0,2])
  cat_rad=[]
  for i in range(0,len(cat)):
    if(cat[i][1]>1.0):
      cat_rad.append(cat[i])
      
  radius=[]
      
  for i in range(0,len(cat_rad)):
    radius.append(cat_rad[i][1])
    
  index=np.argsort(radius)
  cat_ordered=[]
  
  for i in range(0,len(cat_rad)):
    cat_ordered.append(cat_rad[index[i]])
    
  return np.array(cat_ordered)
    
   



if __name__ == '__main__':
  result = query('stars.csv')
  print(result)