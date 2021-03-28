import matplotlib.pyplot as plt
import numpy as np 

no_list=[]

for i in range(1,10001):
    dice1=np.random.randint(1,7)
    dice2=np.random.randint(1,7)
    no_list.append(dice1+dice2)

plt.hist(no_list, bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5], density=True)
plt.xlabel("Sum of numbers on dice")
plt.ylabel("Probability")
plt.title("Dice Probability Histogram")
plt.show()