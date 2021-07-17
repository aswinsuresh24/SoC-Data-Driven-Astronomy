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
 
# load the data and generate the features and targets
data = np.load('sdss_galaxy_colors.npy')
features, targets = get_features_targets(data)
  
# initialize model
dtr=DecisionTreeRegressor()
  
# train the model
dtr.fit(features,targets)

# make predictions using the same features
predictions=dtr.predict(features)

# print out the first 4 predicted redshifts
print(predictions[:4])
