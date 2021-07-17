#Functions
import numpy as np
import time
                 
def angular_dist(l1,l2):
  a=np.sin(np.abs(l1[1]-l2[1])/2)**2
  b=np.cos(l1[1])*np.cos(l2[1])*np.sin(np.abs(l1[0]-l2[0])/2)**2
  d=2*np.arcsin(np.sqrt(a+b))
  d=np.degrees(d)
  return d

def find_closest(list1,list2):
  mindist=angular_dist(list1[0],list2)
  index=0
  for i in range(1,len(list1)):
    d=angular_dist(list1[i],list2)
    if d<mindist:
      mindist=d
      index=i
      
  return index,mindist


def crossmatch(list1,list2,n):
  start=time.perf_counter()
  list1=np.radians(list1)
  list2=np.radians(list2)
   
  matches=[]
  match_index=[]
  no_matches=[]
  
  for i in range(0,len(list1)):
    dist=find_closest(list2,list1[i])
    if dist[1]<n:
      matches.append((i,dist[0],dist[1]))
      match_index.append(i)
      
  end=time.perf_counter()-start    
      
  for i in range(0,len(list1)):
    if not(i in match_index):
      no_matches.append(i)
  no_matches.sort()
  
  return matches,no_matches,end
      
    
  
    
  
  


if __name__ == '__main__':
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
