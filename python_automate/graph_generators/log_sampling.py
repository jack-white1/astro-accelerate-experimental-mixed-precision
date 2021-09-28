import numpy as np
import matplotlib.pyplot as plt
import math
import random

if __name__ == "__main__":
	parameterBounds = {'seed': [0,1],\
					'period': [1.25, 1000],\
					'width':[4,50],\
					'snrpeak':[0.0125, 0.125],\
					'dm':[5,500],\
					'nbits':[8],\
					'nchans':[1024],\
					'tsamp':[128],\
					'tobs':[600],\
					'fch1':[1550],\
					'foff':[0.292968752],\
					'binary':[float('nan')],\
					'bper':[1.5, 336],\
					'bphase':[0.2],\
					'bpmass':[1.0, 1.5],\
					'bcmass':[0.1, 5.0]}

	fakeParameters = {}
	nsamps = 10000
	base = 1000


	for key in parameterBounds:
		fakeParameters[key] = []
		for i in range(nsamps):
			try:
				if key == "seed":
					fakeParameters[key].append(random.randint(0,2147483647))
				elif key == "dm":
					lb = math.log(parameterBounds[key][0],base)
					ub = math.log(parameterBounds[key][1],base)
					fakeParameters[key].append([int(round(base**elem, 5)) for elem in np.random.uniform(lb,ub,nsamps).tolist()][0])
				else:
					lb = math.log(parameterBounds[key][0],base)
					ub = math.log(parameterBounds[key][1],base)
					fakeParameters[key].append([round(base**elem, 5) for elem in np.random.uniform(lb,ub,nsamps).tolist()][0])
			except:
				fakeParameters[key] = [parameterBounds[key][0]][0]
#				print(key + " is not a variable parameter")

	print(fakeParameters)
	
	nbins = 150

	fig, axs = plt.subplots(3, 2, sharey=True, tight_layout=False)

	plt.subplot(3,3,1)
	plt.hist(fakeParameters['seed'], density=False, bins=nbins)  # density=False would make counts
	plt.ylabel('Num of occurences')
	plt.xlabel('seed')

	plt.subplot(3,3,2)
	plt.hist(fakeParameters['period'], density=False, bins=nbins)  # density=False would make counts
	plt.ylabel('Num of occurences')
	plt.xlabel('period')

	plt.subplot(3,3,3)
	plt.hist(fakeParameters['width'], density=False, bins=nbins)  # density=False would make counts
	plt.ylabel('Num of occurences')
	plt.xlabel('width')

	plt.subplot(3,3,4)
	plt.hist(fakeParameters['snrpeak'], density=False, bins=nbins)  # density=False would make counts
	plt.ylabel('Num of occurences')
	plt.xlabel('snrpeak')

	plt.subplot(3,3,5)
	plt.hist(fakeParameters['dm'], density=False, bins=nbins)  # density=False would make counts
	plt.ylabel('Num of occurences')
	plt.xlabel('dm')

	plt.subplot(3,3,6)
	plt.hist(fakeParameters['bper'], density=False, bins=nbins)  # density=False would make counts
	plt.ylabel('Num of occurences')
	plt.xlabel('bper')

	plt.subplot(3,3,7)
	plt.hist(fakeParameters['bpmass'], density=False, bins=nbins)  # density=False would make counts
	plt.ylabel('Num of occurences')
	plt.xlabel('bpmass')

	plt.subplot(3,3,8)
	plt.hist(fakeParameters['bcmass'], density=False, bins=nbins)  # density=False would make counts
	plt.ylabel('Num of occurences')
	plt.xlabel('bcmass')

	plt.suptitle('Log sampling histograms for SIGPROC fake input parameters, n=' + str(nsamps) + ', base=' + str(base))
	plt.show()

