import numpy as np

def get_features_targets(data):
  u,g,r,i,z=data['u'],data['g'],data['r'],data['i'],data['z']
  features = np.zeros((data.shape[0], 4))
  features[:, 0] = u-g
  features[:, 1] = g-r
  features[:, 2] = r-i
  features[:, 3] = i-z
  targets=data['redshift']
  
  return features, targets

 
     
  


if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
    
  features, targets = get_features_targets(data)
    
  print(features[:2])
  print(targets[:2])
