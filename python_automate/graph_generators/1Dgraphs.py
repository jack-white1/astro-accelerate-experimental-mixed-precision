import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("results.txt", 5)

	#for group in grouped_results:
	#	print(group)
	
	graph_colour = 'b'
	harmonic = 0 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.

	index = 2		# 0 = accn, 1 = freq, 2 = snr

	b2s_hist_period, s2d_hist_period, b2d_hist_period = analysis_funcs.extract_1D_hist(grouped_results, harmonic, index, 'period')
	b2s_hist_width, s2d_hist_width, b2d_hist_width = analysis_funcs.extract_1D_hist(grouped_results, harmonic, index, 'width')
	b2s_hist_snrpeak, s2d_hist_snrpeak, b2d_hist_snrpeak = analysis_funcs.extract_1D_hist(grouped_results, harmonic, index, 'snrpeak')
	b2s_hist_dm, s2d_hist_dm, b2d_hist_dm = analysis_funcs.extract_1D_hist(grouped_results, harmonic, index, 'dm')
	b2s_hist_bper, s2d_hist_bper, b2d_hist_bper = analysis_funcs.extract_1D_hist(grouped_results, harmonic, index, 'bper')
	b2s_hist_bpmass, s2d_hist_bpmass, b2d_hist_bpmass = analysis_funcs.extract_1D_hist(grouped_results, harmonic, index, 'bpmass')
	b2s_hist_bcmass, s2d_hist_bcmass, b2d_hist_bcmass = analysis_funcs.extract_1D_hist(grouped_results, harmonic, index, 'bcmass')

	xmin_period = min(b2s_hist_period + s2d_hist_period + b2d_hist_period)
	xmax_period = max(b2s_hist_period + s2d_hist_period + b2d_hist_period)
	xmin_width = min(b2s_hist_width + s2d_hist_width + b2d_hist_width)
	xmax_width = max(b2s_hist_width + s2d_hist_width + b2d_hist_width)
	xmin_snrpeak = min(b2s_hist_snrpeak + s2d_hist_snrpeak + b2d_hist_snrpeak)
	xmax_snrpeak = max(b2s_hist_snrpeak + s2d_hist_snrpeak + b2d_hist_snrpeak)
	xmin_dm = min(b2s_hist_dm + s2d_hist_dm + b2d_hist_dm)
	xmax_dm = max(b2s_hist_dm + s2d_hist_dm + b2d_hist_dm)
	xmin_bper = min(b2s_hist_bper + s2d_hist_bper + b2d_hist_bper)
	xmax_bper = max(b2s_hist_bper + s2d_hist_bper + b2d_hist_bper)
	xmin_bpmass = min(b2s_hist_bpmass + s2d_hist_bpmass + b2d_hist_bpmass)
	xmax_bpmass = max(b2s_hist_bpmass + s2d_hist_bpmass + b2d_hist_bpmass)
	xmin_bcmass = min(b2s_hist_bcmass + s2d_hist_bcmass + b2d_hist_bcmass)
	xmax_bcmass = max(b2s_hist_bcmass + s2d_hist_bcmass + b2d_hist_bcmass)

	xlow_period = analysis_funcs.rounddown(xmin_period,5)
	xhigh_period = analysis_funcs.roundup(xmax_period,5)
	xlow_width = analysis_funcs.rounddown(xmin_width,5)
	xhigh_width = analysis_funcs.roundup(xmax_width,5)
	xlow_snrpeak = analysis_funcs.rounddown(xmin_snrpeak,5)
	xhigh_snrpeak = analysis_funcs.roundup(xmax_snrpeak,5)
	xlow_dm = analysis_funcs.rounddown(xmin_dm,5)
	xhigh_dm = analysis_funcs.roundup(xmax_dm,5)
	xlow_bper = analysis_funcs.rounddown(xmin_bper,5)
	xhigh_bper = analysis_funcs.roundup(xmax_bper,5)
	xlow_bpmass = analysis_funcs.rounddown(xmin_bpmass,5)
	xhigh_bpmass = analysis_funcs.roundup(xmax_bpmass,5)
	xlow_bcmass = analysis_funcs.rounddown(xmin_bcmass,5)
	xhigh_bcmass = analysis_funcs.roundup(xmax_bcmass,5)

#	xlow_period = -0.5
#	xhigh_period = 0.5
#	xlow_width = -0.5
#	xhigh_width = 0.5
#	xlow_snrpeak = -0.5
#	xhigh_snrpeak = 0.5
#	xlow_dm = -0.5
#	xhigh_dm = 0.5
#	xlow_bper = -50
#	xhigh_bper = 5
#	xlow_bpmass = -25
#	xhigh_bpmass = 5
#	xlow_bcmass = -45
#	xhigh_bcmass = 5

	ylow_period = 0
	yhigh_period = 100
	ylow_width = 0
	yhigh_width = 100
	ylow_snrpeak = 0
	yhigh_snrpeak = 100
	ylow_dm = 0
	yhigh_dm = 100
	ylow_bper = 0
	yhigh_bper = 100
	ylow_bpmass = 0
	yhigh_bpmass = 100
	ylow_bcmass = 0
	yhigh_bcmass = 100


	binEdges_period = np.linspace(xlow_period,xhigh_period,100).tolist()
	binEdges_width = np.linspace(xlow_width,xhigh_width,100).tolist()
	binEdges_snrpeak = np.linspace(xlow_snrpeak,xhigh_snrpeak,100).tolist()
	binEdges_dm = np.linspace(xlow_dm,xhigh_dm,100).tolist()
	binEdges_bper = np.linspace(xlow_bper,xhigh_bper,100).tolist()
	binEdges_bpmass = np.linspace(xlow_bpmass,xhigh_bpmass,100).tolist()
	binEdges_bcmass = np.linspace(xlow_bcmass,xhigh_bcmass,100).tolist()

	b2s_values_period = np.histogram(b2s_hist_period, binEdges_period)
	b2d_values_period = np.histogram(b2d_hist_period, binEdges_period)
	s2d_values_period = np.histogram(s2d_hist_period, binEdges_period)

	b2s_values_width = np.histogram(b2s_hist_width, binEdges_width)
	b2d_values_width = np.histogram(b2d_hist_width, binEdges_width)
	s2d_values_width = np.histogram(s2d_hist_width, binEdges_width)

	b2s_values_snrpeak = np.histogram(b2s_hist_snrpeak, binEdges_snrpeak)
	b2d_values_snrpeak = np.histogram(b2d_hist_snrpeak, binEdges_snrpeak)
	s2d_values_snrpeak = np.histogram(s2d_hist_snrpeak, binEdges_snrpeak)

	b2s_values_dm = np.histogram(b2s_hist_dm, binEdges_dm)
	b2d_values_dm = np.histogram(b2d_hist_dm, binEdges_dm)
	s2d_values_dm = np.histogram(s2d_hist_dm, binEdges_dm)

	b2s_values_bper = np.histogram(b2s_hist_bper, binEdges_bper)
	b2d_values_bper = np.histogram(b2d_hist_bper, binEdges_bper)
	s2d_values_bper = np.histogram(s2d_hist_bper, binEdges_bper)

	b2s_values_bpmass = np.histogram(b2s_hist_bpmass, binEdges_bpmass)
	b2d_values_bpmass = np.histogram(b2d_hist_bpmass, binEdges_bpmass)
	s2d_values_bpmass = np.histogram(s2d_hist_bpmass, binEdges_bpmass)

	b2s_values_bcmass = np.histogram(b2s_hist_bcmass, binEdges_bcmass)
	b2d_values_bcmass = np.histogram(b2d_hist_bcmass, binEdges_bcmass)
	s2d_values_bcmass = np.histogram(s2d_hist_bcmass, binEdges_bcmass)

	yhigh_period = max(b2s_values_period[0].tolist() + b2d_values_period[0].tolist() + s2d_values_period[0].tolist()) + 5
	yhigh_width = max(b2s_values_width[0].tolist() + b2d_values_width[0].tolist() + s2d_values_width[0].tolist()) + 5
	yhigh_snrpeak = max(b2s_values_snrpeak[0].tolist() + b2d_values_snrpeak[0].tolist() + s2d_values_snrpeak[0].tolist()) + 5
	yhigh_dm = max(b2s_values_dm[0].tolist() + b2d_values_dm[0].tolist() + s2d_values_dm[0].tolist()) + 5
	yhigh_bper = max(b2s_values_bper[0].tolist() + b2d_values_bper[0].tolist() + s2d_values_bper[0].tolist()) + 5
	yhigh_bpmass = max(b2s_values_bpmass[0].tolist() + b2d_values_bpmass[0].tolist() + s2d_values_bpmass[0].tolist()) + 5
	yhigh_bcmass = max(b2s_values_bcmass[0].tolist() + b2d_values_bcmass[0].tolist() + s2d_values_bcmass[0].tolist()) + 5

	yhigh_period = 300
	yhigh_width = 300
	yhigh_snrpeak = 300
	yhigh_dm = 300
	yhigh_bper = 300
	yhigh_bpmass = 300
	yhigh_bcmass = 300

	print(b2s_hist_period + s2d_hist_period + b2d_hist_period)


	fig, axs = plt.subplots(3, 3, sharey=True, tight_layout=True)

	plt.subplot(3,3,1)
	plt.hist(b2s_hist_period + s2d_hist_period + b2d_hist_period, binEdges_period, density=False, facecolor=graph_colour, alpha=0.75)
	plt.ylabel('Num of occurences')
	plt.title('PERIOD')
	plt.xlabel('% Difference')
	plt.xlim(xlow_period, xhigh_period)
	plt.ylim(ylow_period, yhigh_period)
	plt.text((xhigh_period+xlow_period)/2,(yhigh_period+ylow_period)/2, str(len(b2s_hist_period + s2d_hist_period + b2d_hist_period)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,2)
	plt.hist(b2s_hist_width + s2d_hist_width + b2d_hist_width, binEdges_width, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('WIDTH')
	plt.xlabel('% Difference')
	plt.ylabel('Num of occurences')
	plt.xlim(xlow_width, xhigh_width)
	plt.ylim(ylow_width, yhigh_width)
	plt.text((xhigh_width+xlow_width)/2,(yhigh_width+ylow_width)/2, str(len(b2s_hist_width + s2d_hist_width + b2d_hist_width)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,3)
	plt.hist(b2s_hist_snrpeak + s2d_hist_snrpeak + b2d_hist_snrpeak, binEdges_snrpeak, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('SNRPEAK')
	plt.xlabel('% Difference')
	plt.ylabel('Num of occurences')
	plt.xlim(xlow_snrpeak, xhigh_snrpeak)
	plt.ylim(ylow_snrpeak, yhigh_snrpeak)
	plt.text((xhigh_snrpeak+xlow_snrpeak)/2,(yhigh_snrpeak+ylow_snrpeak)/2, str(len(b2s_hist_snrpeak + s2d_hist_snrpeak + b2d_hist_snrpeak)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,4)
	plt.hist(b2s_hist_dm + s2d_hist_dm + b2d_hist_dm, binEdges_dm, density=False, facecolor=graph_colour, alpha=0.75)
	plt.ylabel('Num of occurences')
	plt.xlabel('% Difference')
	plt.title('DM')
	plt.xlim(xlow_dm, xhigh_dm)
	plt.ylim(ylow_dm, yhigh_dm)
	plt.text((xhigh_dm+xlow_dm)/2,(yhigh_dm+ylow_dm)/2, str(len(b2s_hist_dm + s2d_hist_dm + b2d_hist_dm)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,5)
	plt.hist(b2s_hist_bper + s2d_hist_bper + b2d_hist_bper, binEdges_bper, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('BPER')
	plt.xlabel('% Difference')
	plt.ylabel('Num of occurences')
	plt.xlim(xlow_bper, xhigh_bper)
	plt.ylim(ylow_bper, yhigh_bper)
	plt.text((xhigh_bper+xlow_bper)/2,(yhigh_bper+ylow_bper)/2, str(len(b2s_hist_bper + s2d_hist_bper + b2d_hist_bper)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,6)
	plt.hist(b2s_hist_bpmass + s2d_hist_bpmass + b2d_hist_bpmass, binEdges_bpmass, density=False, facecolor=graph_colour, alpha=0.75)
	plt.title('BPMASS')
	plt.xlabel('% Difference')
	plt.ylabel('Num of occurences')
	plt.xlim(xlow_bpmass, xhigh_bpmass)
	plt.ylim(ylow_bpmass, yhigh_bpmass)
	plt.text((xhigh_bpmass+xlow_bpmass)/2,(yhigh_bpmass+ylow_bpmass)/2, str(len(b2s_hist_bpmass + s2d_hist_bpmass + b2d_hist_bpmass)) + ' peaks measured')
	plt.grid(True)

	plt.subplot(3,3,7)
	plt.hist(b2s_hist_bcmass + s2d_hist_bcmass + b2d_hist_bcmass, binEdges_bcmass, density=False, facecolor=graph_colour, alpha=0.75)
	plt.xlabel('% Difference')
	plt.ylabel('Num of occurences')
	plt.title('BCMASS')
	plt.xlim(xlow_bcmass, xhigh_bcmass)
	plt.ylim(ylow_bcmass, yhigh_bcmass)
	plt.text((xhigh_bcmass+xlow_bcmass)/2,(yhigh_bcmass+ylow_bcmass)/2, str(len(b2s_hist_bcmass + s2d_hist_bcmass + b2d_hist_bcmass)) + ' peaks measured')
	plt.grid(True)


	plt.suptitle("Relative difference between peak recovered SNR across fake file parameters (75 datapoints per axis)")
	plt.show()


		#print("b2s_diff: " + str(b2s_diff) + "\tb2d_diff: " + str(b2d_diff) + "\ts2d_diff: " + str(s2d_diff))


	#first answer is single a good approximation to double?

	#then tackle whether bfloat is a good approximation to single


		#print(i)
		#print(i["parameters"])
		#print(json.loads(i["peak_list"]))

	#iterate through results list, collect all peaks together in a dictionary of parameters, bfloat peaks, single peaks, double peaks
