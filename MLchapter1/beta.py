import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import beta
import seaborn


seaborn.set()

params = [0.25,1,10]
x=np.linspace(0,1,100)
f, ax = plt.subplots(len(params),len(params),sharex=True,sharey=True)


for i in range(len(params)):
    for j in range(len(params)):
        a=params[i]
        b=params[j]
        y=beta(a,b).pdf(x)
        ax[i,j].plot(x,y,color='red')
        ax[i,j].set_title('$\\alpha$={},$\\beta$={}'.format(a,b))
        ax[i,j].set_ylim(0,10)
        
ax[0,0].set_xticks([0,0.2,0.4,0.6,0.8,1.0])
ax[0,0].set_yticks([0,2.5,5,7.5,10])
ax[1,0].set_ylabel('$\\alpha$')
ax[2,1].set_xlabel('$\\theta$')
plt.show()
        #ax[i,j].plot(x,y,color='red')
print("hello")
