import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  t=[]
  # the time to generate the random array should not be included
 
  for i in range(0,ntrials):
    data = np.random.rand(size)
    start=time.perf_counter()
    res = func(data)
    end=time.perf_counter()-start
    t.append(end)
    
  t=np.array(t)
  t_avg=np.mean(t)
  # return the average run time
  return t_avg

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))