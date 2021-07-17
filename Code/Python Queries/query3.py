# Function
import numpy as np

def query(str1,str2):
  s_cat=np.loadtxt('%s' %str1, delimiter=',', usecols=[0,2])
  p_cat=np.loadtxt('%s' %str2, delimiter=',', usecols=[0,5])
  radius_ratio=[]
  
  for i in range(0,len(s_cat)):
    for j in range(0,len(p_cat)):
      if(p_cat[j][0]==s_cat[i][0] and s_cat[i][1]>1.0):
         radius_ratio.append(p_cat[j][1]/s_cat[i][1])
       
  radius_ratio_ordered=[]
  index=np.argsort(radius_ratio)
  for i in range(0,len(radius_ratio)):
    radius_ratio_ordered.append([radius_ratio[index[i]]])
         
  radius_ratio_ordered=np.array(radius_ratio_ordered)
  return radius_ratio_ordered
  


if __name__ == '__main__':
  result = query('stars.csv', 'planets.csv')