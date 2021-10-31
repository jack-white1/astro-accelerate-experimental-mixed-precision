import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np
from matplotlib.colors import LogNorm
import math
import itertools

def makeRandomFakeToDoList(fakeParameters):
	for parameter_set in fakeParameters:
		with open("fakeToDoList.txt", "a") as f:
			f.write(str(json.dumps(parameter_set))+"\n")

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("uniformresults.txt", 5)

	harmonic = 0 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.

	index = 0		# 0 = accn, 1 = freq, 2 = snr

	accn_b2s_hist_0, accn_s2d_hist_0, accn_b2d_hist_0 = analysis_funcs.extract_thresh_diff_hist_freq_bin_3d(grouped_results, 0, index)
	accn_b2s_hist_1, accn_s2d_hist_1, accn_b2d_hist_1 = analysis_funcs.extract_thresh_diff_hist_freq_bin_3d(grouped_results, 1, index)
	accn_b2s_hist_2, accn_s2d_hist_2, accn_b2d_hist_2 = analysis_funcs.extract_thresh_diff_hist_freq_bin_3d(grouped_results, 2, index)


	index = 1		# 0 = accn, 1 = freq, 2 = snr

	freq_b2s_hist_0, freq_s2d_hist_0, freq_b2d_hist_0 = analysis_funcs.extract_thresh_diff_hist_freq_bin_3d(grouped_results, 0, index)
	freq_b2s_hist_1, freq_s2d_hist_1, freq_b2d_hist_1 = analysis_funcs.extract_thresh_diff_hist_freq_bin_3d(grouped_results, 1, index)
	freq_b2s_hist_2, freq_s2d_hist_2, freq_b2d_hist_2 = analysis_funcs.extract_thresh_diff_hist_freq_bin_3d(grouped_results, 2, index)

	for i in range(len(accn_b2s_hist_0[0])):
		print("Accn bin drift: " + str(accn_b2s_hist_0[0][i]) + ", parameters: " + str(accn_b2s_hist_0[1][i]))

	makeRandomFakeToDoList(accn_b2s_hist_0[1])
	makeRandomFakeToDoList(accn_b2s_hist_1[1])
	makeRandomFakeToDoList(accn_b2s_hist_2[1])
	makeRandomFakeToDoList(freq_b2s_hist_0[1])
	makeRandomFakeToDoList(freq_b2s_hist_1[1])
	makeRandomFakeToDoList(freq_b2s_hist_2[1])


	#print("There are " + str(len(ordered_list)) + " peaks in the list, " + str(len([i for i in ordered_list if i < 22])) + " of which are below 22")

