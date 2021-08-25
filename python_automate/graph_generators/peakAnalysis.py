import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("results.txt", 5)

	for group in grouped_results:
		print(group)
	

	harmonic = 0 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.

	index = 2		# 0 = accn, 1 = freq, 2 = snr

	b2s_hist, s2d_hist, b2d_hist = analysis_funcs.extract_diff_hist(grouped_results, harmonic, index)

	xmin = min(b2s_hist + s2d_hist + b2d_hist)
	xmax = max(b2s_hist + s2d_hist + b2d_hist)

	print("xmin: " + str(xmin) + " xmax: " + str(xmax))

	xlow = analysis_funcs.rounddown(xmin,5)
	xhigh = analysis_funcs.roundup(xmax,5)

	ylow = 0
	yhigh = 100

	binEdges = np.linspace(xlow,xhigh,100).tolist()
	b2s_values = np.histogram(b2s_hist, binEdges)
	b2d_values = np.histogram(b2d_hist, binEdges)
	s2d_values = np.histogram(s2d_hist, binEdges)

	print(max(b2s_values[0].tolist()))

	yhigh = max(b2s_values[0].tolist() + b2d_values[0].tolist() + s2d_values[0].tolist()) + 5

	fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False)

	plt.subplot(1,3,1)
	b2s_values, b2s_bins, b2s_patches = plt.hist(b2s_hist, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('% Difference')
	plt.ylabel('Frequency')
	plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(b2s_hist)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(1,3,2)
	plt.hist(b2d_hist, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('% Difference')
	plt.ylabel('Frequency')
	plt.title('BFLOAT vs DOUBLE')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(b2d_hist)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(1,3,3)
	plt.hist(s2d_hist, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('% Difference')
	plt.ylabel('Frequency')
	plt.title('SINGLE vs DOUBLE')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(s2d_hist)) + ' peaks measured')
	plt.grid(True)


	plt.suptitle("Relative difference between peak recovered SNR across extreme synthetic pulsars, 0th (fundamental)harmonic")
	plt.show()


		#print("b2s_diff: " + str(b2s_diff) + "\tb2d_diff: " + str(b2d_diff) + "\ts2d_diff: " + str(s2d_diff))


	#first answer is single a good approximation to double?

	#then tackle whether bfloat is a good approximation to single


		#print(i)
		#print(i["parameters"])
		#print(json.loads(i["peak_list"]))

	#iterate through results list, collect all peaks together in a dictionary of parameters, bfloat peaks, single peaks, double peaks
