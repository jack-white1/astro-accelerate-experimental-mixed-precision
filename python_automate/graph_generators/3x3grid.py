import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("results.txt", 5)

	for group in grouped_results:
		print(group)
	
	graph_colour = 'b'
	harmonic = 0 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.

	index = 0		# 0 = accn, 1 = freq, 2 = snr

	b2s_hist_0, s2d_hist_0, b2d_hist_0 = analysis_funcs.extract_diff_hist(grouped_results, 0, index)
	b2s_hist_1, s2d_hist_1, b2d_hist_1 = analysis_funcs.extract_diff_hist(grouped_results, 1, index)
	b2s_hist_2, s2d_hist_2, b2d_hist_2 = analysis_funcs.extract_diff_hist(grouped_results, 2, index)

	xmin_0 = min(b2s_hist_0 + s2d_hist_0 + b2d_hist_0)
	xmax_0 = max(b2s_hist_0 + s2d_hist_0 + b2d_hist_0)
	xmin_1 = min(b2s_hist_1 + s2d_hist_1 + b2d_hist_1)
	xmax_1 = max(b2s_hist_1 + s2d_hist_1 + b2d_hist_1)
	xmin_2 = min(b2s_hist_2 + s2d_hist_2 + b2d_hist_2)
	xmax_2 = max(b2s_hist_2 + s2d_hist_2 + b2d_hist_2)

	xlow_0 = analysis_funcs.rounddown(xmin_0,5)
	xhigh_0 = analysis_funcs.roundup(xmax_0,5)
	xlow_1 = analysis_funcs.rounddown(xmin_1,5)
	xhigh_1 = analysis_funcs.roundup(xmax_1,5)
	xlow_2 = analysis_funcs.rounddown(xmin_2,5)
	xhigh_2 = analysis_funcs.roundup(xmax_2,5)

	ylow_0 = 0
	yhigh_0 = 100
	ylow_1 = 0
	yhigh_1 = 100
	ylow_2 = 0
	yhigh_2 = 100

	binEdges_0 = np.linspace(xlow_0,xhigh_0,100).tolist()
	b2s_values_0 = np.histogram(b2s_hist_0, binEdges_0)
	b2d_values_0 = np.histogram(b2d_hist_0, binEdges_0)
	s2d_values_0 = np.histogram(s2d_hist_0, binEdges_0)

	binEdges_1 = np.linspace(xlow_1,xhigh_1,100).tolist()
	b2s_values_1 = np.histogram(b2s_hist_1, binEdges_1)
	b2d_values_1 = np.histogram(b2d_hist_1, binEdges_1)
	s2d_values_1 = np.histogram(s2d_hist_1, binEdges_1)

	binEdges_2 = np.linspace(xlow_2,xhigh_2,100).tolist()
	b2s_values_2 = np.histogram(b2s_hist_2, binEdges_2)
	b2d_values_2 = np.histogram(b2d_hist_2, binEdges_2)
	s2d_values_2 = np.histogram(s2d_hist_2, binEdges_2)

	yhigh_0 = max(b2s_values_0[0].tolist() + b2d_values_0[0].tolist() + s2d_values_0[0].tolist()) + 5
	yhigh_1 = max(b2s_values_1[0].tolist() + b2d_values_1[0].tolist() + s2d_values_1[0].tolist()) + 5
	yhigh_2 = max(b2s_values_2[0].tolist() + b2d_values_2[0].tolist() + s2d_values_2[0].tolist()) + 5

	fig, axs = plt.subplots(3, 3, sharey=True, tight_layout=False)

	plt.subplot(3,3,1)
	plt.hist(b2s_hist_0, binEdges_0, density=False, facecolor=graph_colour, alpha=0.75)
	plt.ylabel('Frequency - Fundamental harmonic')
	plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlow_0, xhigh_0)
	plt.ylim(ylow_0, yhigh_0)
	plt.text((xhigh_0+xlow_0)/2,(yhigh_0+ylow_0)/2, str(len(b2s_hist_0)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,2)
	plt.hist(b2d_hist_0, binEdges_0, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('BFLOAT vs DOUBLE')
	plt.xlim(xlow_0, xhigh_0)
	plt.ylim(ylow_0, yhigh_0)
	plt.text((xhigh_0+xlow_0)/2,(yhigh_0+ylow_0)/2, str(len(b2d_hist_0)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,3)
	plt.hist(s2d_hist_0, binEdges_0, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('SINGLE vs DOUBLE')
	plt.xlim(xlow_0, xhigh_0)
	plt.ylim(ylow_0, yhigh_0)
	plt.text((xhigh_0+xlow_0)/2,(yhigh_0+ylow_0)/2, str(len(s2d_hist_0)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,4)
	plt.hist(b2s_hist_1, binEdges_1, density=False, facecolor=graph_colour, alpha=0.75)
	plt.ylabel('Frequency - First harmonic')
	#plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlow_1, xhigh_1)
	plt.ylim(ylow_1, yhigh_1)
	plt.text((xhigh_1+xlow_1)/2,(yhigh_1+ylow_1)/2, str(len(b2s_hist_1)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,5)
	plt.hist(b2d_hist_1, binEdges_1, density=False, facecolor=graph_colour, alpha=0.75)
	#plt.title('BFLOAT vs DOUBLE')
	plt.xlim(xlow_1, xhigh_1)
	plt.ylim(ylow_1, yhigh_1)
	plt.text((xhigh_1+xlow_1)/2,(yhigh_1+ylow_1)/2, str(len(b2d_hist_1)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,6)
	plt.hist(s2d_hist_1, binEdges_1, density=False, facecolor=graph_colour, alpha=0.75)
	#plt.title('SINGLE vs DOUBLE')
	plt.xlim(xlow_1, xhigh_1)
	plt.ylim(ylow_1, yhigh_1)
	plt.text((xhigh_1+xlow_1)/2,(yhigh_1+ylow_1)/2, str(len(s2d_hist_1)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,7)
	plt.hist(b2s_hist_2, binEdges_2, density=False, facecolor=graph_colour, alpha=0.75)
	plt.xlabel('% Difference')
	plt.ylabel('Frequency - Second harmonic')
	#plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlow_2, xhigh_2)
	plt.ylim(ylow_2, yhigh_2)
	plt.text((xhigh_2+xlow_2)/2,(yhigh_2+ylow_2)/2, str(len(b2s_hist_2)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,8)
	plt.hist(b2d_hist_2, binEdges_2, density=False, facecolor=graph_colour, alpha=0.75)
	plt.xlabel('% Difference')
	#plt.title('BFLOAT vs DOUBLE')
	plt.xlim(xlow_2, xhigh_2)
	plt.ylim(ylow_2, yhigh_2)
	plt.text((xhigh_2+xlow_2)/2,(yhigh_2+ylow_2)/2, str(len(b2d_hist_2)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,9)
	plt.hist(s2d_hist_2, binEdges_2, density=False, facecolor=graph_colour, alpha=0.75)
	plt.xlabel('% Difference')
	#plt.title('SINGLE vs DOUBLE')
	plt.xlim(xlow_2, xhigh_2)
	plt.ylim(ylow_2, yhigh_2)
	plt.text((xhigh_2+xlow_2)/2,(yhigh_2+ylow_2)/2, str(len(s2d_hist_2)) + ' peaks measured')
	plt.grid(True)


	plt.suptitle("Relative difference between peak acceleration across extreme synthetic pulsars")
	plt.show()


		#print("b2s_diff: " + str(b2s_diff) + "\tb2d_diff: " + str(b2d_diff) + "\ts2d_diff: " + str(s2d_diff))


	#first answer is single a good approximation to double?

	#then tackle whether bfloat is a good approximation to single


		#print(i)
		#print(i["parameters"])
		#print(json.loads(i["peak_list"]))

	#iterate through results list, collect all peaks together in a dictionary of parameters, bfloat peaks, single peaks, double peaks
