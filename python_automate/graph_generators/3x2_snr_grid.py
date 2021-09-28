import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("uniformresults.txt", 5)

	i = 0
	for group in grouped_results:
		print(i)
		print("\n")
	
	graph_colour_0 = 'r'
	graph_colour_1 = 'g'
	graph_colour_2 = 'b'
	harmonic = 0 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.

	index = 2		# 0 = accn, 1 = freq, 2 = snr

	b2s_hist_0, s2d_hist_0, b2d_hist_0 = analysis_funcs.extract_diff_hist(grouped_results, 0, index)
	b2s_hist_1, s2d_hist_1, b2d_hist_1 = analysis_funcs.extract_diff_hist(grouped_results, 1, index)
	b2s_hist_2, s2d_hist_2, b2d_hist_2 = analysis_funcs.extract_diff_hist(grouped_results, 2, index)

	print(b2s_hist_0)

	b2s_0_mean = np.mean(b2s_hist_0)
	b2s_0_stdev = np.std(b2s_hist_0)
	b2d_0_mean = np.mean(b2d_hist_0)
	b2d_0_stdev = np.std(b2d_hist_0)
	s2d_0_mean = np.mean(s2d_hist_0)
	s2d_0_stdev = np.std(s2d_hist_0)
	b2s_1_mean = np.mean(b2s_hist_1)
	b2s_1_stdev = np.std(b2s_hist_1)
	b2d_1_mean = np.mean(b2d_hist_1)
	b2d_1_stdev = np.std(b2d_hist_1)
	s2d_1_mean = np.mean(s2d_hist_1)
	s2d_1_stdev = np.std(s2d_hist_1)
	b2s_2_mean = np.mean(b2s_hist_2)
	b2s_2_stdev = np.std(b2s_hist_2)
	b2d_2_mean = np.mean(b2d_hist_2)
	b2d_2_stdev = np.std(b2d_hist_2)
	s2d_2_mean = np.mean(s2d_hist_2)
	s2d_2_stdev = np.std(s2d_hist_2)
	

	xmin_a = min(b2s_hist_0)
	xmax_a = max(b2s_hist_0)
	xmin_b = min(b2d_hist_0)
	xmax_b = max(b2d_hist_0)
	xmin_c = min(s2d_hist_0)
	xmax_c = max(s2d_hist_0)
	xmax_d = max(b2s_hist_1)
	xmin_d = min(b2s_hist_1)
	xmin_e = min(b2d_hist_1)
	xmax_e = max(b2d_hist_1)
	xmin_f = min(s2d_hist_1)
	xmax_f = max(s2d_hist_1)
	xmin_g = min(b2s_hist_2)
	xmax_g = max(b2s_hist_2)
	xmin_h = min(b2d_hist_2)
	xmax_h = max(b2d_hist_2)
	xmin_i = min(s2d_hist_2)
	xmax_i = max(s2d_hist_2)

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
	xlo_g = xmin_g
	xhi_g = xmax_g
	xlo_h = xmin_h
	xhi_h = xmax_h
	xlo_i = xmin_i
	xhi_i = xmax_i

	xlo_a = b2s_0_mean - 3*b2s_0_stdev
	xhi_a = b2s_0_mean + 3*b2s_0_stdev
	xlo_b = b2d_0_mean - 3*b2d_0_stdev
	xhi_b = b2d_0_mean + 3*b2d_0_stdev
	xlo_c = s2d_0_mean - 3*s2d_0_stdev
	xhi_c = s2d_0_mean + 3*s2d_0_stdev
	xlo_d = b2s_1_mean - 3*b2s_1_stdev
	xhi_d = b2s_1_mean + 3*b2s_1_stdev
	xlo_e = b2d_1_mean - 3*b2d_1_stdev
	xhi_e = b2d_1_mean + 3*b2d_1_stdev
	xlo_f = s2d_1_mean - 3*s2d_1_stdev
	xhi_f = s2d_1_mean + 3*s2d_1_stdev
	xlo_g = b2s_2_mean - 3*b2s_2_stdev
	xhi_g = b2s_2_mean + 3*b2s_2_stdev
	xlo_h = b2d_2_mean - 3*b2d_2_stdev
	xhi_h = b2d_2_mean + 3*b2d_2_stdev
	xlo_i = s2d_2_mean - 3*s2d_2_stdev
	xhi_i = s2d_2_mean + 3*s2d_2_stdev


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
	b2s_values_0 = np.histogram(b2s_hist_0, binEdges_a)

	binEdges_b = np.linspace(xlo_b,xhi_b,nbins).tolist()
	b2d_values_0 = np.histogram(b2d_hist_0, binEdges_b)

	binEdges_c = np.linspace(xlo_c,xhi_c,nbins).tolist()
	s2d_values_0 = np.histogram(s2d_hist_0, binEdges_c)

	binEdges_d = np.linspace(xlo_d,xhi_d,nbins).tolist()
	b2s_values_1 = np.histogram(b2s_hist_1, binEdges_d)

	binEdges_e = np.linspace(xlo_e,xhi_e,nbins).tolist()
	b2d_values_1 = np.histogram(b2d_hist_1, binEdges_e)

	binEdges_f = np.linspace(xlo_f,xhi_f,nbins).tolist()
	s2d_values_1 = np.histogram(s2d_hist_1, binEdges_f)

	binEdges_g = np.linspace(xlo_g,xhi_g,nbins).tolist()
	b2s_values_2 = np.histogram(b2s_hist_2, binEdges_g)

	binEdges_h = np.linspace(xlo_h,xhi_h,nbins).tolist()
	b2d_values_2 = np.histogram(b2d_hist_2, binEdges_h)

	binEdges_i = np.linspace(xlo_i,xhi_i,nbins).tolist()
	s2d_values_2 = np.histogram(s2d_hist_2, binEdges_i)

	yhi_a = max(b2s_values_0[0].tolist())*1.1
	yhi_b = max(b2d_values_0[0].tolist())*1.1
	yhi_c = max(s2d_values_0[0].tolist())*1.1
	yhi_d = max(b2s_values_1[0].tolist())*1.1
	yhi_e = max(b2d_values_1[0].tolist())*1.1
	yhi_f = max(s2d_values_1[0].tolist())*1.1
	yhi_g = max(b2s_values_2[0].tolist())*1.1
	yhi_h = max(b2d_values_2[0].tolist())*1.1
	yhi_i = max(s2d_values_2[0].tolist())*1.1

	#print(str(xlo_d) + " " + str(xhi_d) +  " " + str(ylo_d) +  " " + str(yhi_d))
	#print(b2s_values_0)

	fig, axs = plt.subplots(3, 2, sharey=True, tight_layout=False)

	xtickrotation = 15

	plt.subplot(3,2,1)
	plt.hist(b2s_hist_0, binEdges_a, density=False, facecolor=graph_colour_0, alpha=0.75)
	plt.ylabel('Number of peaks - Fundamental')
	plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlo_a, xhi_a)
	plt.ylim(ylo_a, yhi_a)
	measured_str = str(len(b2s_hist_0)) + ' peaks measured'
	plotted_str = "\n" + str(sum(b2s_values_0[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(b2s_0_mean,4))
	stdev_str = "\nStdev: " + str(round(b2s_0_stdev,4))
	max_str = "\nMax:" + str(round(max(b2s_hist_0),4))
	min_str = "\nMin:" + str(round(min(b2s_hist_0),4))
	plt.text(xlo_a + 0.025*abs(xhi_a-xlo_a),yhi_a*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.grid(True)

#	plt.subplot(3,3,2)
#	plt.hist(b2d_hist_0, binEdges_b, density=False, facecolor=graph_colour_0, alpha=0.75)
#	plt.title('BFLOAT vs DOUBLE')
#	plt.xlim(xlo_b, xhi_b)
#	plt.ylim(ylo_b, yhi_b)
#	measured_str = str(len(b2d_hist_0)) + ' peaks measured'
#	plotted_str = "\n" + str(sum(b2d_values_0[0])) + ' peaks plotted, ±3σ'
#	mean_str = "\nMean: " + "{:e}".format(round(b2d_0_mean,4))
#	stdev_str = "\nStdev: " + str(round(b2d_0_stdev,4))
#	max_str = "\nMax:" + str(round(max(b2d_hist_0),4))
#	min_str = "\nMin:" + str(round(min(b2d_hist_0),4))
#	plt.text(xlo_b + 0.025*abs(xhi_b-xlo_b),yhi_b*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
#	plt.grid(True)
#
	plt.subplot(3,2,2)
	plt.hist(s2d_hist_0, binEdges_c, density=False, facecolor=graph_colour_0, alpha=0.75)
	plt.title('SINGLE vs DOUBLE')
	plt.xlim(xlo_c, xhi_c)
	plt.ylim(ylo_c, yhi_c)
	measured_str = str(len(s2d_hist_0)) + ' peaks measured'
	plotted_str = "\n" + str(sum(s2d_values_0[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(s2d_0_mean,4))
	stdev_str = "\nStdev: " + str(round(s2d_0_stdev,4))
	max_str = "\nMax:" + str(round(max(s2d_hist_0),4))
	min_str = "\nMin:" + str(round(min(s2d_hist_0),4))
	plt.text(xlo_c + 0.025*abs(xhi_c-xlo_c),yhi_c*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.xticks(rotation=xtickrotation, ha="right")
	plt.grid(True)

	plt.subplot(3,2,3)
	plt.hist(b2s_hist_1, binEdges_d, density=False, facecolor=graph_colour_1, alpha=0.75)
	plt.ylabel('Number of peaks - First harmonic')
	#plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlo_d, xhi_d)
	plt.ylim(ylo_d, yhi_d)
	measured_str = str(len(b2s_hist_1)) + ' peaks measured'
	plotted_str = "\n" + str(sum(b2s_values_1[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(b2s_1_mean,4))
	stdev_str = "\nStdev: " + str(round(b2s_1_stdev,4))
	max_str = "\nMax:" + str(round(max(b2s_hist_1),4))
	min_str = "\nMin:" + str(round(min(b2s_hist_1),4))
	plt.text(xlo_d + 0.025*abs(xhi_d-xlo_d),yhi_d*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.grid(True)

#	plt.subplot(3,3,5)
#	plt.hist(b2d_hist_1, binEdges_e, density=False, facecolor=graph_colour_1, alpha=0.75)
#	#plt.title('BFLOAT vs DOUBLE')
#	plt.xlim(xlo_e, xhi_e)
#	plt.ylim(ylo_e, yhi_e)
#	measured_str = str(len(b2d_hist_1)) + ' peaks measured'
#	plotted_str = "\n" + str(sum(b2d_values_1[0])) + ' peaks plotted, ±3σ'
#	mean_str = "\nMean: " + "{:e}".format(round(b2d_1_mean,4))
#	stdev_str = "\nStdev: " + str(round(b2d_1_stdev,4))
#	max_str = "\nMax:" + str(round(max(b2d_hist_1),4))
#	min_str = "\nMin:" + str(round(min(b2d_hist_1),4))
#	plt.text(xlo_e + 0.025*abs(xhi_e-xlo_e),yhi_e*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
#	plt.grid(True)

	plt.subplot(3,2,4)
	plt.hist(s2d_hist_1, binEdges_f, density=False, facecolor=graph_colour_1, alpha=0.75)
	#plt.title('SINGLE vs DOUBLE')
	plt.xlim(xlo_f, xhi_f)
	plt.ylim(ylo_f, yhi_f)
	measured_str = str(len(s2d_hist_1)) + ' peaks measured'
	plotted_str = "\n" + str(sum(s2d_values_1[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(s2d_1_mean,4))
	stdev_str = "\nStdev: " + str(round(s2d_1_stdev,4))
	max_str = "\nMax:" + str(round(max(s2d_hist_1),4))
	min_str = "\nMin:" + str(round(min(s2d_hist_1),4))
	plt.text(xlo_f + 0.025*abs(xhi_f-xlo_f),yhi_f*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.xticks(rotation=xtickrotation, ha="right")
	plt.grid(True)

	plt.subplot(3,2,5)
	plt.hist(b2s_hist_2, binEdges_g, density=False, facecolor=graph_colour_2, alpha=0.75)
	plt.xlabel('Relative difference between peak SNR - %')
	plt.ylabel('Number of peaks - Second harmonic')
	#plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlo_g, xhi_g)
	plt.ylim(ylo_g, yhi_g)
	measured_str = str(len(b2s_hist_2)) + ' peaks measured'
	plotted_str = "\n" + str(sum(b2s_values_2[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(b2s_2_mean,4))
	stdev_str = "\nStdev: " + str(round(b2s_2_stdev,4))
	max_str = "\nMax:" + str(round(max(b2s_hist_2),4))
	min_str = "\nMin:" + str(round(min(b2s_hist_2),4))
	plt.text(xlo_g + 0.025*abs(xhi_g-xlo_g),yhi_g*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.grid(True)

#	plt.subplot(3,3,8)
#	plt.hist(b2d_hist_2, binEdges_h, density=False, facecolor=graph_colour_2, alpha=0.75)
#	plt.xlabel('% Difference')
#	#plt.title('BFLOAT vs DOUBLE')
#	plt.xlim(xlo_h, xhi_h)
#	plt.ylim(ylo_h, yhi_h)
#	measured_str = str(len(b2d_hist_2)) + ' peaks measured'
#	plotted_str = "\n" + str(sum(b2d_values_1[0])) + ' peaks plotted, ±3σ'
#	mean_str = "\nMean: " + "{:e}".format(round(b2d_1_mean,4))
#	stdev_str = "\nStdev: " + str(round(b2d_1_stdev,4))
#	max_str = "\nMax:" + str(round(max(b2d_hist_1),4))
#	min_str = "\nMin:" + str(round(min(b2d_hist_1),4))
#	plt.text(xlo_h + 0.025*abs(xhi_h-xlo_h),yhi_h*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
#	plt.grid(True)
#
	plt.subplot(3,2,6)
	plt.hist(s2d_hist_2, binEdges_i, density=False, facecolor=graph_colour_2, alpha=0.75)
	plt.xlabel('Relative difference between peak SNR - %')
	#plt.title('SINGLE vs DOUBLE')
	plt.xlim(xlo_i, xhi_i)
	plt.ylim(ylo_i, yhi_i)
	measured_str = str(len(s2d_hist_2)) + ' peaks measured'
	plotted_str = "\n" + str(sum(s2d_values_2[0])) + ' peaks plotted, μ±3σ'
	mean_str = "\nMean: " + "{:e}".format(round(s2d_2_mean,4))
	stdev_str = "\nStdev: " + str(round(s2d_2_stdev,4))
	max_str = "\nMax:" + str(round(max(s2d_hist_2),4))
	min_str = "\nMin:" + str(round(min(s2d_hist_2),4))
	plt.text(xlo_i + 0.025*abs(xhi_i-xlo_i),yhi_i*0.55, measured_str + plotted_str + mean_str + stdev_str + max_str + min_str)
	plt.xticks(rotation=xtickrotation, ha="right")
	plt.grid(True)


	plt.suptitle("Relative difference between peak SNR in synthetic pulsars (log sampled input parameters)")
	plt.show()


	#mean
	#stdev