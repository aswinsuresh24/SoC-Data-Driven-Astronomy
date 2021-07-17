import numpy as np
from sklearn.tree import DecisionTreeRegressor

def get_features_targets(data):
  u,g,r,i,z=data['u'],data['g'],data['r'],data['i'],data['z']
  features = np.zeros((data.shape[0], 4))
  features[:, 0] = u-g
  features[:, 1] = g-r
  features[:, 2] = r-i
  features[:, 3] = i-z
  targets=data['redshift']
  
  return features, targets

def median_diff(predicted, actual):
  med_diff=[]
  for i in range(0,len(predicted)):
    med_diff.append(np.abs(predicted[i]-actual[i]))
    
  median_difference=np.median(med_diff)
  return median_difference


def split_data(features,targets):
  split=features.shape[0]//2
  train_features = features[:split]
  test_features = features[split:]
  
  split=targets.shape[0]//2
  train_targets = targets[:split]
  test_targets = targets[split:]
  
  return train_features,test_features,train_targets,test_targets

def validate_model(model, features, targets):
  # split the data into training and testing features and predictions
    train_features,test_features,train_targets,test_targets=split_data(features,targets)
    
  # train the model
    model.fit(train_features,train_targets)

  # get the predicted_redshifts
    predictions=model.predict(test_features)
  
  # use median_diff function to calculate the accuracy
    return median_diff(test_targets, predictions)


if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model
  dtr = DecisionTreeRegressor()

  # validate the model and print the med_diff
  diff = validate_model(dtr, features, targets)
  print('Median difference: {:f}'.format(diff))