import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("/home/jack/Documents/aa_mixed/astro-accelerate-experimental-mixed-precision/python_automate/results.txt", 5)

	harmonic = 0 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.
	index = 2		# 0 = accn, 1 = freq, 2 = snr
	b2s_hist, s2d_hist, b2d_hist = analysis_funcs.extract_diff_hist_save_params(grouped_results, harmonic, index)
	b2s_hist = sorted(b2s_hist, key = lambda x: x[0], reverse=True)[0:100]
	s2d_hist = sorted(s2d_hist, key = lambda x: x[0], reverse=True)[0:100]
	b2d_hist = sorted(b2d_hist, key = lambda x: x[0], reverse=True)[0:100]

	period_hist = []
	width_hist = []
	snrpeak_hist = []
	dm_hist = []
	bper_hist = []
	bpmass_hist = []
	bcmass_hist = []

	
	for element in (b2s_hist + s2d_hist + b2d_hist):
		period_hist.append(element[1]["period"])
		width_hist.append(element[1]["width"])
		snrpeak_hist.append(element[1]["snrpeak"])
		dm_hist.append(element[1]["dm"])
		bper_hist.append(element[1]["bper"])
		bpmass_hist.append(element[1]["bpmass"])
		bcmass_hist.append(element[1]["bcmass"])

	fig, axs = plt.subplots(3, 3, sharey=True, tight_layout=True)

	graph_colour = 'b'

	plt.subplot(3,3,1)
	plt.hist(period_hist, 20, density=False, facecolor=graph_colour, alpha=0.75)
	plt.ylabel('Num of occurences')
	plt.title('PERIOD')
	plt.xlabel('Parameter value')
	plt.grid(True)

	plt.subplot(3,3,2)
	plt.hist(width_hist, 20, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('WIDTH')
	plt.xlabel('Parameter value')
	plt.ylabel('Num of occurences')
	plt.grid(True)

	plt.subplot(3,3,3)
	plt.hist(snrpeak_hist, 20, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('SNRPEAK')
	plt.xlabel('Parameter value')
	plt.ylabel('Num of occurences')
	plt.grid(True)

	plt.subplot(3,3,4)
	plt.hist(dm_hist, 20, density=False, facecolor=graph_colour, alpha=0.75)
	plt.ylabel('Num of occurences')
	plt.xlabel('Parameter value')
	plt.title('DM')
	plt.grid(True)

	plt.subplot(3,3,5)
	plt.hist(bper_hist, 20, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('BPER')
	plt.xlabel('Parameter value')
	plt.ylabel('Num of occurences')
	plt.grid(True)

	plt.subplot(3,3,6)
	plt.hist(bpmass_hist, 20, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('BPMASS')
	plt.xlabel('Parameter value')
	plt.ylabel('Num of occurences')
	plt.grid(True)

	plt.subplot(3,3,7)
	plt.hist(bcmass_hist, 20, density=False, facecolor=graph_colour, alpha=0.75)
	plt.xlabel('Parameter value')
	plt.ylabel('Num of occurences')
	plt.title('BCMASS')
	plt.grid(True)


	plt.suptitle("Histograms showing frequency of parameter values in 100 worst recreated peaks in b/d, b/s, s/d")
	plt.show()