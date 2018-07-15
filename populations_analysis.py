import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('populations.txt')
year, hares, lynxes, carrots = data.T
print(data)
means = np.mean(data,axis=0)[1:]
stdev = np.std(data,axis=0)[1:]
#mean and stdev
print(means)
print(stdev)
#find max species each year
popu = data[:,1:]
species = np.array(['H','L','C'])
maxspecies = species[np.argmax(popu,axis=1)]
print(np.c_[year,maxspecies])
print(year[np.any(popu > 50000,axis=1)])
popu = data[:,1:]
year[np.argsort(popu,axis=0)[:2,:]]
hare_grad = np.gradient(hares, 1.0)
print("diff(Hares) vs. Lynxes correlation", np.around(np.corrcoef(hare_grad, lynxes)[0,1],decimals=2))
plt.plot(year, hare_grad, year, -lynxes)
