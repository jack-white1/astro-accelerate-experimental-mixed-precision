import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np
import datetime

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("uniformresults.txt", 10)

	#for group in grouped_results:
	#	print(group)
	

	harmonic = 0 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.

	index = 2		# 0 = accn, 1 = freq, 2 = snr

	b2s_hist = np.asarray(analysis_funcs.extract_diff_hist_perc_diff_b2s(grouped_results, harmonic, index))

	#print(b2s_hist.tolist())

	nbins = 20

	#xmax
	xmax = max(b2s_hist[:,1].tolist())
	#xmin
	xmin = min(b2s_hist[:,1].tolist())
	
	#ymax
	ymax = max(b2s_hist[:,0].tolist())
	#ymin
	ymin = min(b2s_hist[:,0].tolist())

	xbins = np.linspace(xmin, xmax, nbins).tolist()

	xbinnames = []
	for i in range(nbins-1):
		#xbinnames.append(str(int(xbins[i])) + " to " + str(int(xbins[i+1])))
		xbinnames.append("[" + str(int(xbins[i])) + ", " + str(int(xbins[i+1])) + "]")

	print(xbins)

	box_whisker = []
	histogram = []

	for i in range(nbins-1):
		perc_diffs_at_snr = []
		for curr_snr in b2s_hist.tolist():
			if curr_snr[1] > xbins[i] and curr_snr[1] < xbins[i+1]:
				perc_diffs_at_snr.append(curr_snr[0])
		box_whisker.append(perc_diffs_at_snr)
		histogram.append(len(perc_diffs_at_snr))
		print("xbins["+str(i)+"]: " + str(xbins[i]) + ", xbins["+str(i+1)+"]: " + str(xbins[i+1]))


	print(histogram)
	flierprops = dict(marker='x', markerfacecolor='black', markersize=4, markeredgecolor='black')
	fig, axs = plt.subplots(2,1)
	#plt.subplot(2,1,1)
	axs[0].set_title('Percentage difference between single and bfloat16 precision recovered SNR peak height')
	axs[0].boxplot(box_whisker, showmeans=True, meanline=True, flierprops=flierprops)
	xtickNames = plt.setp(axs[0], xticklabels=xbinnames)
	plt.setp(xtickNames, rotation=90, fontsize=8)
	axs[0].set_xlabel("SNR bin")
	axs[0].set_ylabel("Percentage difference")
	axs[0].text(5,2,'Yellow line = median, green line = mean')

	print(xbins[1]-xbins[0])
	axs[1].set_title('Number of peaks in each bin')
	print(len(xbins))
	print(len(histogram))
	axs[1].bar(xbins[0:-1], histogram, xbins[1]-xbins[0])
	axs[1].set_xlim(left = -90, right = 8700)

	#fig.subplots_adjust(wspace=5.0)
	fig.tight_layout(pad=0.5)
	plt.show()

	#xmin = min(b2s_hist + s2d_hist + b2d_hist)
#	xmax = max(b2s_hist + s2d_hist + b2d_hist)

#	print("xmin: " + str(xmin) + " xmax: " + str(xmax))

#	xlow = analysis_funcs.rounddown(xmin,5)
#	xhigh = analysis_funcs.roundup(xmax,5)

#	ylow = 0
#	yhigh = 100

#	binEdges = np.linspace(xlow,xhigh,100).tolist()
#	b2s_values = np.histogram(b2s_hist, binEdges)
#	b2d_values = np.histogram(b2d_hist, binEdges)
#	s2d_values = np.histogram(s2d_hist, binEdges)

#	print(max(b2s_values[0].tolist()))

#	yhigh = max(b2s_values[0].tolist() + b2d_values[0].tolist() + s2d_values[0].tolist()) + 5

#	fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False)

#	plt.subplot(1,3,1)
#	b2s_values, b2s_bins, b2s_patches = plt.hist(b2s_hist, binEdges, density=False, facecolor='g', alpha=0.75)
#	plt.xlabel('% Difference')
#	plt.ylabel('Frequency')
#	plt.title('BFLOAT vs SINGLE')
#	plt.xlim(xlow, xhigh)
#	plt.ylim(ylow, yhigh)
#	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(b2s_hist)) + ' peaks measured')
#	plt.grid(True)

#	plt.subplot(1,3,2)
#	plt.hist(b2d_hist, binEdges, density=False, facecolor='g', alpha=0.75)
#	plt.xlabel('% Difference')
#	plt.ylabel('Frequency')
#	plt.title('BFLOAT vs DOUBLE')
#	plt.xlim(xlow, xhigh)
#	plt.ylim(ylow, yhigh)
#	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(b2d_hist)) + ' peaks measured')
#	plt.grid(True)

#	plt.subplot(1,3,3)
#	plt.hist(s2d_hist, binEdges, density=False, facecolor='g', alpha=0.75)
#	plt.xlabel('% Difference')
#	plt.ylabel('Frequency')
#	plt.title('SINGLE vs DOUBLE')
#	plt.xlim(xlow, xhigh)
#	plt.ylim(ylow, yhigh)
#	plt.text((xhigh+xlow)/2,(yhigh+ylow)/2, str(len(s2d_hist)) + ' peaks measured')
#	plt.grid(True)


#	plt.suptitle("Relative difference between peak recovered SNR across extreme synthetic pulsars, 0th (fundamental)harmonic")
#	plt.show()


		#print("b2s_diff: " + str(b2s_diff) + "\tb2d_diff: " + str(b2d_diff) + "\ts2d_diff: " + str(s2d_diff))


	#first answer is single a good approximation to double?

	#then tackle whether bfloat is a good approximation to single


		#print(i)
		#print(i["parameters"])
		#print(json.loads(i["peak_list"]))

	#iterate through results list, collect all peaks together in a dictionary of parameters, bfloat peaks, single peaks, double peaks