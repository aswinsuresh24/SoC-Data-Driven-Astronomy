import numpy as np

def median_diff(predicted, actual):
  med_diff=[]
  for i in range(0,len(predicted)):
    med_diff.append(np.abs(predicted[i]-actual[i]))
    
  median_difference=np.median(med_diff)
  return median_difference


if __name__ == "__main__":
  # load testing data
  targets = np.load('targets.npy')
  predictions = np.load('predictions.npy')

  # call function to measure the accuracy of the predictions
  diff = median_diff(predictions, targets)

  # print the median difference
  print("Median difference: {:0.3f}".format(diff))