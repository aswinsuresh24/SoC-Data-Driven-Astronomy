# Calc Stats function:
import numpy as np
def calc_stats(str):
  data=np.loadtxt(str,delimiter=',')
  data_mean=np.mean(data)
  data_median=np.median(data)
  data_mean=np.round(data_mean,decimals=1)
  data_median=np.round(data_median,decimals=1)

  return data_mean,data_median
  
  



if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data.csv')
  print(mean)