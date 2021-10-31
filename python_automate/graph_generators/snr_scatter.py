import json
import matplotlib.pyplot as plt
import numpy as np
import analysis_funcs
import numpy as np

if __name__ == "__main__":
	grouped_results = analysis_funcs.group_results("uniformresults.txt", 5)

	graph_colour_0 = 'r'
	graph_colour_1 = 'g'
	graph_colour_2 = 'b'

	harmonic = 2 	# 0 = fundamental, 1 = 1st harmonic, 2 = 2nd harmonic etc.

	index = 2		# 0 = accn, 1 = freq, 2 = snr

	b2s_hist_0, s2d_hist_0, b2d_hist_0 = analysis_funcs.extract_diff_hist_save_params(grouped_results, 0, index)
	b2s_hist_1, s2d_hist_1, b2d_hist_1 = analysis_funcs.extract_diff_hist_save_params(grouped_results, 1, index)
	b2s_hist_2, s2d_hist_2, b2d_hist_2 = analysis_funcs.extract_diff_hist_save_params(grouped_results, 2, index)

	x_a = []
	y_a = []
	x_b = []
	y_b = []
	x_c = []
	y_c = []

	for datapoint in b2d_hist_0:
		xpoint = datapoint['single_peak']
		ypoint = abs(datapoint['diff'])
		x_a.append(xpoint)
		y_a.append(ypoint)

		if xpoint > 0:
			if ypoint > 3:
				#print("OUTLIER:")
				print(int(datapoint['parameters']['seed']))
				#print("\n")

	for datapoint in b2d_hist_1:
		xpoint = datapoint['single_peak']
		ypoint = abs(datapoint['diff'])
		x_b.append(xpoint)
		y_b.append(ypoint)

		if xpoint > 0:
			if ypoint > 3:
				#print("OUTLIER:")
				print(int(datapoint['parameters']['seed']))
				#print("\n")

	for datapoint in b2d_hist_2:
		xpoint = datapoint['single_peak']
		ypoint = abs(datapoint['diff'])
		x_c.append(xpoint)
		y_c.append(ypoint)

		if xpoint > 0:
			if ypoint > 3:
				#print("OUTLIER:")
				print(int(datapoint['parameters']['seed']))
				#print("\n")


	xtickrotation = 15
	fig, ax = plt.subplots()
	ax.scatter(x_a,y_a,c='r',label = "Fundamental")
	ax.scatter(x_b,y_b,c='g',label = "First harmonic")
	ax.scatter(x_c,y_c,c='b',label = "Second harmonic")
	ax.legend()
	plt.xscale('log')
	plt.ylabel('Magnitude of relative difference %')
	plt.xlabel('Pow of single precision peak')
	plt.grid(True)
	plt.suptitle("How relative peak height difference varies with single precision peak pow, BFLOAT vs SINGLE")
	plt.show()


	#mean
	#stdev