import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np

if __name__ == "__main__":
	nPeaks = 5
	grouped_results = analysis_funcs.group_results("results.txt", nPeaks)

	bfloat_hist_data = []
	single_hist_data = []
	double_hist_data = []

	temp_max_group  = {}
	max_peak_height = 0
	for group in grouped_results:
		#print("\n\n\n\n Group:")
		#print(group)
		for peak in range(nPeaks):
			try:
				bfloat_hist_data.append(group["bfloat_peaks"][peak][2])
				single_hist_data.append(group["single_peaks"][peak][2])
				double_hist_data.append(group["double_peaks"][peak][2])
				if group["double_peaks"][peak][2] > max_peak_height:
					temp_max_group = group
					max_peak_height = group["double_peaks"][peak][2]
					print(group)
				if group["single_peaks"][peak][2] > max_peak_height:
					temp_max_group = group
					max_peak_height = group["double_peaks"][peak][2]
					print(group)
				if group["bfloat_peaks"][peak][2] > max_peak_height:
					temp_max_group = group
					max_peak_height = group["double_peaks"][peak][2]
					print(group)
			except:
				pass

	print("Max group:")
	print(temp_max_group)

	fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False)

	xmin = min(bfloat_hist_data + single_hist_data + double_hist_data)
	print("Xmin: " + str(xmin))
	xmax = max(bfloat_hist_data + single_hist_data + double_hist_data)
	print("Xmax: " + str(xmax))

	xlow = analysis_funcs.rounddown(xmin,5)
	xhigh = analysis_funcs.roundup(xmax,5)
	#xhigh = 10000
	ylow = 0

	binEdges = np.linspace(xlow,xhigh,100).tolist()
	bfloat_values = np.histogram(bfloat_hist_data, binEdges)
	single_values = np.histogram(single_hist_data, binEdges)
	double_values = np.histogram(double_hist_data, binEdges)

	yhigh = max(bfloat_values[0].tolist() + single_values[0].tolist() + double_values[0].tolist()) + 5


	plt.subplot(1,3,1)
	plt.hist(bfloat_hist_data, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('SNR Peak Height')
	plt.ylabel('Frequency')
	plt.title('BFLOAT')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(bfloat_hist_data)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(1,3,2)
	plt.hist(single_hist_data, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('SNR Peak Height')
	plt.ylabel('Frequency')
	plt.title('SINGLE')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(single_hist_data)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(1,3,3)
	plt.hist(double_hist_data, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('SNR Peak Height')
	plt.ylabel('Frequency')
	plt.title('DOUBLE')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(double_hist_data)) + ' peaks measured')
	plt.grid(True)

	plt.show()

