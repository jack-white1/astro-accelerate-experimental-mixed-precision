import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("uniformresults.txt", 5)

	i = 0
	for group in grouped_results:
		if group["bfloat_peaks"][1][0] != group["single_peaks"][1][0]: #[harmonic][acc = 0 ,freq = 1,snr = 2, freq_bin = 3]
			print(group["bfloat_peaks"])
			print(group["single_peaks"])
			print("\n")
	
	graph_colour_0 = 'r'
	graph_colour_1 = 'g'
	graph_colour_2 = 'b'


	harmonic = 0 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.

	index = 0		# 0 = accn, 1 = freq, 2 = snr

	accn_b2s_hist_0, accn_s2d_hist_0, accn_b2d_hist_0 = analysis_funcs.extract_diff_hist_freq_bin(grouped_results, 0, index)
	accn_b2s_hist_1, accn_s2d_hist_1, accn_b2d_hist_1 = analysis_funcs.extract_diff_hist_freq_bin(grouped_results, 1, index)
	accn_b2s_hist_2, accn_s2d_hist_2, accn_b2d_hist_2 = analysis_funcs.extract_diff_hist_freq_bin(grouped_results, 2, index)


	index = 1		# 0 = accn, 1 = freq, 2 = snr

	freq_b2s_hist_0, freq_s2d_hist_0, freq_b2d_hist_0 = analysis_funcs.extract_diff_hist_freq_bin(grouped_results, 0, index)
	freq_b2s_hist_1, freq_s2d_hist_1, freq_b2d_hist_1 = analysis_funcs.extract_diff_hist_freq_bin(grouped_results, 1, index)
	freq_b2s_hist_2, freq_s2d_hist_2, freq_b2d_hist_2 = analysis_funcs.extract_diff_hist_freq_bin(grouped_results, 2, index)


	print(accn_b2s_hist_0)

	accn_b2s_0_mean = np.mean(accn_b2s_hist_0)
	accn_b2s_0_stdev = np.std(accn_b2s_hist_0)

	accn_b2s_1_mean = np.mean(accn_b2s_hist_1)
	accn_b2s_1_stdev = np.std(accn_b2s_hist_1)

	accn_b2s_2_mean = np.mean(accn_b2s_hist_2)
	accn_b2s_2_stdev = np.std(accn_b2s_hist_2)


	freq_b2s_0_mean = np.mean(freq_b2s_hist_0)
	freq_b2s_0_stdev = np.std(freq_b2s_hist_0)

	freq_b2s_1_mean = np.mean(freq_b2s_hist_1)
	freq_b2s_1_stdev = np.std(freq_b2s_hist_1)

	freq_b2s_2_mean = np.mean(freq_b2s_hist_2)
	freq_b2s_2_stdev = np.std(freq_b2s_hist_2)


	xmin_a = min(accn_b2s_hist_0)
	xmax_a = max(accn_b2s_hist_0)

	xmax_b = max(accn_b2s_hist_1)
	xmin_b = min(accn_b2s_hist_1)

	xmin_c = min(accn_b2s_hist_2)
	xmax_c = max(accn_b2s_hist_2)

	xmin_d = min(freq_b2s_hist_0)
	xmax_d = max(freq_b2s_hist_0)

	xmax_e = max(freq_b2s_hist_1)
	xmin_e = min(freq_b2s_hist_1)

	xmin_f = min(freq_b2s_hist_2)
	xmax_f = max(freq_b2s_hist_2)


	#print(str(xmin_0) + " " + str(xmin_1) + " " + str(xmin_2) + " " +  str(xmax_0) + " " +  str(xmax_1) + " " +  str(xmax_2))
	#print(s2d_hist_0)

	#xlo_0 = analysis_funcs.rounddown(xmin_0,5)
	#xhi_0 = analysis_funcs.roundup(xmax_0,5)
	#xlo_1 = analysis_funcs.rounddown(xmin_1,5)
	#xhi_1 = analysis_funcs.roundup(xmax_1,5)
	#xlo_2 = analysis_funcs.rounddown(xmin_2,5)
	#xhi_2 = analysis_funcs.roundup(xmax_2,5)

	xlo_a = xmin_a
	xhi_a = xmax_a
	xlo_b = xmin_b
	xhi_b = xmax_b
	xlo_c = xmin_c
	xhi_c = xmax_c
	xlo_d = xmin_d
	xhi_d = xmax_d
	xlo_e = xmin_e
	xhi_e = xmax_e
	xlo_f = xmin_f
	xhi_f = xmax_f

	xlo_a = accn_b2s_0_mean - 3*accn_b2s_0_stdev
	xhi_a = accn_b2s_0_mean + 3*accn_b2s_0_stdev
	xlo_b = accn_b2s_1_mean - 3*accn_b2s_1_stdev
	xhi_b = accn_b2s_1_mean + 3*accn_b2s_1_stdev
	xlo_c = accn_b2s_2_mean - 3*accn_b2s_2_stdev
	xhi_c = accn_b2s_2_mean + 3*accn_b2s_2_stdev

	xlo_d = freq_b2s_0_mean - 3*freq_b2s_0_stdev
	xhi_d = freq_b2s_0_mean + 3*freq_b2s_0_stdev
	xlo_e = freq_b2s_1_mean - 3*freq_b2s_1_stdev
	xhi_e = freq_b2s_1_mean + 3*freq_b2s_1_stdev
	xlo_f = freq_b2s_2_mean - 3*freq_b2s_2_stdev
	xhi_f = freq_b2s_2_mean + 3*freq_b2s_2_stdev


	ylo_a = 0
	ylo_b = 0
	ylo_c = 0
	ylo_d = 0
	ylo_e = 0
	ylo_f = 0
	ylo_g = 0
	ylo_h = 0
	ylo_i = 0

	nbins = 100

	binEdges_a = np.linspace(xlo_a,xhi_a,nbins).tolist()
	accn_b2s_values_0 = np.histogram(accn_b2s_hist_0, binEdges_a)

	binEdges_b = np.linspace(xlo_b,xhi_b,nbins).tolist()
	accn_b2s_values_1 = np.histogram(accn_b2s_hist_1, binEdges_b)

	binEdges_c = np.linspace(xlo_c,xhi_c,nbins).tolist()
	accn_b2s_values_2 = np.histogram(accn_b2s_hist_2, binEdges_c)


	binEdges_d = np.linspace(xlo_d,xhi_d,nbins).tolist()
	freq_b2s_values_0 = np.histogram(freq_b2s_hist_0, binEdges_a)

	binEdges_e = np.linspace(xlo_e,xhi_e,nbins).tolist()
	freq_b2s_values_1 = np.histogram(freq_b2s_hist_1, binEdges_b)

	binEdges_f = np.linspace(xlo_f,xhi_f,nbins).tolist()
	freq_b2s_values_2 = np.histogram(freq_b2s_hist_2, binEdges_c)



	yhi_a = max(accn_b2s_values_0[0].tolist())*1.1
	yhi_b = max(accn_b2s_values_1[0].tolist())*1.1
	yhi_c = max(accn_b2s_values_2[0].tolist())*1.1

	yhi_d = max(freq_b2s_values_0[0].tolist())*1.1
	yhi_e = max(freq_b2s_values_1[0].tolist())*1.1
	yhi_f = max(freq_b2s_values_2[0].tolist())*1.1


	#print(str(xlo_d) + " " + str(xhi_d) +  " " + str(ylo_d) +  " " + str(yhi_d))
	#print(b2s_values_0)

	fig, axs = plt.subplots(3, 2, sharey=True, tight_layout=False)

	xtickrotation = 15

	plt.subplot(3,2,1)
	plt.hist(accn_b2s_hist_0, binEdges_a, density=False, facecolor=graph_colour_0, alpha=0.75)
	plt.ylabel('Fundamental\nNumber of occurences')
	plt.title('Acceleration')
	plt.xlim(xlo_a, xhi_a)
	plt.ylim(ylo_a, yhi_a)
	measured_str = str(len(accn_b2s_hist_0)) + ' peaks measured'
	plotted_str = "\n" + str(sum(accn_b2s_values_0[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(accn_b2s_0_mean,4))
	stdev_str = "\nStdev: " + str(round(accn_b2s_0_stdev,4))
	max_str = "\nMax:" + str(round(max(accn_b2s_hist_0),4))
	min_str = "\nMin:" + str(round(min(accn_b2s_hist_0),4))
	plt.text(xlo_a + 0.025*abs(xhi_a-xlo_a),yhi_a*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.grid(True)

	plt.subplot(3,2,2)
	plt.hist(freq_b2s_hist_0, binEdges_b, density=False, facecolor=graph_colour_0, alpha=0.75)
	plt.title('Frequency')
	plt.xlim(xlo_b, xhi_b)
	plt.ylim(ylo_b, yhi_b)
	measured_str = str(len(freq_b2s_hist_0)) + ' peaks measured'
	plotted_str = "\n" + str(sum(freq_b2s_values_0[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(freq_b2s_0_mean,4))
	stdev_str = "\nStdev: " + str(round(freq_b2s_0_stdev,4))
	max_str = "\nMax:" + str(round(max(freq_b2s_hist_0),4))
	min_str = "\nMin:" + str(round(min(freq_b2s_hist_0),4))
	plt.text(xlo_b + 0.025*abs(xhi_b-xlo_b),yhi_c*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.xticks(rotation=xtickrotation, ha="right")
	plt.grid(True)

	plt.subplot(3,2,3)
	plt.hist(accn_b2s_hist_1, binEdges_c, density=False, facecolor=graph_colour_1, alpha=0.75)
	plt.ylabel('First harmonic\nNumber of occurences ')
	#plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlo_c, xhi_c)
	plt.ylim(ylo_c, yhi_c)
	measured_str = str(len(accn_b2s_hist_1)) + ' peaks measured'
	plotted_str = "\n" + str(sum(accn_b2s_values_1[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(accn_b2s_1_mean,4))
	stdev_str = "\nStdev: " + str(round(accn_b2s_1_stdev,4))
	max_str = "\nMax:" + str(round(max(accn_b2s_hist_1),4))
	min_str = "\nMin:" + str(round(min(accn_b2s_hist_1),4))
	plt.text(xlo_c + 0.025*abs(xhi_c-xlo_c),yhi_c*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.grid(True)

	plt.subplot(3,2,4)
	plt.hist(freq_b2s_hist_1, binEdges_d, density=False, facecolor=graph_colour_1, alpha=0.75)
	plt.xlim(xlo_d, xhi_d)
	plt.ylim(ylo_d, yhi_d)
	measured_str = str(len(freq_b2s_hist_1)) + ' peaks measured'
	plotted_str = "\n" + str(sum(freq_b2s_values_1[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(freq_b2s_1_mean,4))
	stdev_str = "\nStdev: " + str(round(freq_b2s_1_stdev,4))
	max_str = "\nMax:" + str(round(max(freq_b2s_hist_1),4))
	min_str = "\nMin:" + str(round(min(freq_b2s_hist_1),4))
	plt.text(xlo_d + 0.025*abs(xhi_d-xlo_d),yhi_d*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.xticks(rotation=xtickrotation, ha="right")
	plt.grid(True)

	plt.subplot(3,2,5)
	plt.hist(accn_b2s_hist_2, binEdges_e, density=False, facecolor=graph_colour_2, alpha=0.75)
	plt.xlabel('Acceleration bin drift')
	plt.ylabel('Second harmonic\nNumber of occurences')
	plt.xlim(xlo_e, xhi_e)
	plt.ylim(ylo_e, yhi_e)
	measured_str = str(len(accn_b2s_hist_2)) + ' peaks measured'
	plotted_str = "\n" + str(sum(accn_b2s_values_2[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(accn_b2s_2_mean,4))
	stdev_str = "\nStdev: " + str(round(accn_b2s_2_stdev,4))
	max_str = "\nMax:" + str(round(max(accn_b2s_hist_2),4))
	min_str = "\nMin:" + str(round(min(accn_b2s_hist_2),4))
	plt.text(xlo_e + 0.025*abs(xhi_e-xlo_e),yhi_e*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.grid(True)

	plt.subplot(3,2,6)
	plt.hist(freq_b2s_hist_2, binEdges_f, density=False, facecolor=graph_colour_2, alpha=0.75)
	plt.xlabel('Frequency bin drift')
	plt.xlim(xlo_f, xhi_f)
	plt.ylim(ylo_f, yhi_f)
	measured_str = str(len(freq_b2s_hist_2)) + ' peaks measured'
	plotted_str = "\n" + str(sum(freq_b2s_values_2[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(freq_b2s_2_mean,4))
	stdev_str = "\nStdev: " + str(round(freq_b2s_2_stdev,4))
	max_str = "\nMax:" + str(round(max(freq_b2s_hist_2),4))
	min_str = "\nMin:" + str(round(min(freq_b2s_hist_2),4))
	plt.text(xlo_f + 0.025*abs(xhi_f-xlo_f),yhi_f*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.xticks(rotation=xtickrotation, ha="right")
	plt.grid(True)


	plt.suptitle("Acceleration, frequency bin drift in synthetic pulsars (log sampled input parameters)")
	plt.show()


	#mean
	#stdev