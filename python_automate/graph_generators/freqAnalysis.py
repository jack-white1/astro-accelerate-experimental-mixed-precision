import json
import matplotlib.pyplot as plt
import numpy as np

def relative_difference (a,b):
	return 100*(a-b)/(0.5*(a+b))

if __name__ == "__main__":
	rawResultsList = []
	with open("extremePulsarResults.txt", "r") as resultsFile:
		for line in resultsFile:
			rawResultsList.append(json.loads(line))

	results = []

	for i in rawResultsList:
		peak_list = i["peak_list"]
		precision = i["precision"]
		parameters = {"period": i["period"],\
		"width": i["width"],\
		"snrpeak": i["snrpeak"],\
		"dm": i["dm"],\
		"nbits": i["nbits"],\
		"nchans": i["nchans"],\
		"tsamp": i["tsamp"],\
		"tobs": i["tobs"],\
		"fch1": i["fch1"],\
		"foff": i["foff"],\
		"binary": i["binary"],\
		"bper": i["bper"],\
		"bphase": i["bphase"],\
		"bpmass": i["bpmass"],\
		"bcmass": i["bcmass"],\
		}

		results.append({"peak_list": peak_list, "precision":precision, "parameters":parameters})

	grouped_results = []
	for result in results:
		result_group = {}
		if result["precision"] == "bfloat":
			result_group["bfloat_peaks"] = json.loads(result["peak_list"])
			result_group["parameters"] = result["parameters"]
			for candidate in results:
				if candidate["parameters"] == result["parameters"]:
					if candidate["precision"] == "single":
						result_group["single_peaks"] = json.loads(candidate["peak_list"])
					if candidate["precision"] == "double":
						result_group["double_peaks"] = json.loads(candidate["peak_list"])
			results.remove(result)
			grouped_results.append(result_group)

	print(len(grouped_results))
	b2s_hist = []
	s2d_hist = []
	b2d_hist = []

	for group in grouped_results:
		bfloat_peak_freq = group["bfloat_peaks"][0][1]
		single_peak_freq = group["single_peaks"][0][1]
		double_peak_freq = group["double_peaks"][0][1]

		b = bfloat_peak_freq
		s = single_peak_freq
		d = double_peak_freq

		b2s_diff = relative_difference(b,s)
		s2d_diff = relative_difference(s,d)
		b2d_diff = relative_difference(b,d)

		#print(str(b2s_diff) +"\t"+ str(s2d_diff) +"\t"+ str(b2d_diff))

		b2s_hist.append(b2s_diff)
		s2d_hist.append(s2d_diff)
		b2d_hist.append(b2d_diff)

	xmin = min(b2s_hist + s2d_hist + b2d_hist)
	xmax = max(b2s_hist + s2d_hist + b2d_hist)
	print("xmin: " + str(xmin) + " xmax: " + str(xmax))

	xlow = -50
	xhigh = 50

	ylow = 0
	yhigh = 150

	binEdges = np.linspace(xlow,xhigh,100).tolist()

	fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False)

	plt.subplot(1,3,1)
	plt.hist(b2s_hist, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('% Difference')
	plt.ylabel('Num of occurences')
	plt.title('BFLOAT vs SINGLE')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.grid(True)

	plt.subplot(1,3,2)
	plt.hist(b2d_hist, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('% Difference')
	plt.ylabel('Num of occurences')
	plt.title('BFLOAT vs DOUBLE')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.grid(True)

	plt.subplot(1,3,3)
	plt.hist(s2d_hist, binEdges, density=False, facecolor='g', alpha=0.75)
	plt.xlabel('% Difference')
	plt.ylabel('Num of occurences')
	plt.title('SINGLE vs DOUBLE')
	plt.xlim(xlow, xhigh)
	plt.ylim(ylow, yhigh)
	plt.grid(True)


	plt.suptitle("Relative difference between peak freq across 128 extreme synthetic pulsars")
	plt.show()

		#print("b2s_diff: " + str(b2s_diff) + "\tb2d_diff: " + str(b2d_diff) + "\ts2d_diff: " + str(s2d_diff))


	#first answer is single a good approximation to double?

	#then tackle whether bfloat is a good approximation to single


		#print(i)
		#print(i["parameters"])
		#print(json.loads(i["peak_list"]))

	#iterate through results list, collect all peaks together in a dictionary of parameters, bfloat peaks, single peaks, double peaks
