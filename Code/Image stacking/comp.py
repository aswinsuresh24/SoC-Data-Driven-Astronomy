# List_stats function
import numpy as np

def list_stats(list):
  list.sort()
  list=np.array(list)
  l=len(list)
  if l==1:
    return list[0],list[0]
  else:
    mean=np.mean(list)
    mean=round(mean,2)
    if l%2==0:
      mid=l//2
      median=(list[mid-1]+list[mid])/2
      median=round(median,2)
      return round(median,2),round(mean,2)
    else:
      mid=l//2
      median=list[mid]
      median=round(median,2)
      return round(median,2),round(mean,2)

      
      
      
  
   
if __name__ == '__main__':
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  m = list_stats([1.5])
  print(m)