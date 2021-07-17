# Mean datasets function:
import numpy as np
def mean_datasets(str):
  l=len(str)
  data=np.loadtxt(str[0],delimiter=',')
  for i in range(1,l):
    data+=np.loadtxt(str[i],delimiter=',')
  data=data/l
  data=np.round(data,decimals=1)
  return data
  


if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
