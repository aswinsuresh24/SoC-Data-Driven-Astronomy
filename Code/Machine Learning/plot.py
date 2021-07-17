import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors.npy')
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')
    
    # Define our colour indexes u-g and r-i
    u,g,r,i=data['u'],data['g'],data['r'],data['i']
    features = np.zeros((data.shape[0], 2))
    features[:, 0] = u-g
    features[:, 1] = r-i
    ug=np.array(features[:, 0])
    ri=np.array(features[:, 1])
    # Make a redshift array
    redshift=data['redshift']
    # Create the plot with plt.scatter and plt.colorbar
    plot=plt.scatter(ug,ri,s=0.1,c=redshift,cmap=cmap,lw=0.1)
    plt.colorbar(plot)
    # Define axis labels and plot title
    plt.xlabel('Colour index u-g')
    plt.ylabel('Colour index r-i')
    plt.title('Redshift (colour) u-g versus r-i')
    # Set any axis limits
    plt.xlim(-0.5,2.5)
    plt.ylim(-0.5,1.0)

    plt.show()