import analysis_funcs
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == "__main__":
	nPeaks=1
	grouped_results = analysis_funcs.group_results("results.txt", nPeaks, datetime.datetime(2021,9,16,23), datetime.datetime(2021,9,17,7))
	#print(grouped_results)
	#grouped_results = analysis_funcs.group_results("results.txt", 3, datetime.datetime(2021,9,8,12), datetime.datetime(2021,9,8,20))
	bphase_data = []
	
	bfloat_harm_sum_data = []
	single_harm_sum_data = []
	double_harm_sum_data = []

	bfloat_accn_data = []
	single_accn_data = []
	double_accn_data = []
	prestoc_accn_data = []
	prestos_accn_data = []

	bfloat_snr_data = []
	single_snr_data = []
	double_snr_data = []
	prestoc_snr_data = []
	prestos_snr_data = []

	bfloat_freq_data = []
	single_freq_data = []
	double_freq_data = []
	prestoc_freq_data = []
	prestos_freq_data = []



	parameters = ''

	for group in grouped_results:
		print(group)
		bfloat_harm_sum = 0
		single_harm_sum = 0
		double_harm_sum = 0

		for harmonic in range(nPeaks):
			bfloat_harm_sum += group["bfloat_peaks"][harmonic][2]
			single_harm_sum += group["single_peaks"][harmonic][2]
			try:
				double_harm_sum += group["double_peaks"][harmonic][2]
			except:
				print("No double data")
				print(group)

		harmonic = 0 	# 0 = fundamental, 1 = first harmonic, 2 = second harmonic etc

		bfloat_harm_sum_data.append(bfloat_harm_sum)
		single_harm_sum_data.append(single_harm_sum)
		double_harm_sum_data.append(double_harm_sum)

		bfloat_accn_data.append(group["bfloat_peaks"][harmonic][0])
		single_accn_data.append(group["single_peaks"][harmonic][0])
		prestos_accn_data.append(group["PRESTOsummed_peaks"][harmonic][0])
		prestoc_accn_data.append(group["PRESTOcoherent_peaks"][harmonic][0])


		bfloat_snr_data.append(group["bfloat_peaks"][harmonic][2])
		single_snr_data.append(group["single_peaks"][harmonic][2])
		prestos_snr_data.append(group["PRESTOsummed_peaks"][harmonic][2])
		prestoc_snr_data.append(group["PRESTOcoherent_peaks"][harmonic][2])
		try:
			double_snr_data.append(group["double_peaks"][harmonic][2])
			double_accn_data.append(group["double_peaks"][harmonic][0])
		except:
			print("no double data at")
			print(group)

		bfloat_freq_data.append(group["bfloat_peaks"][harmonic][1])
		single_freq_data.append(group["single_peaks"][harmonic][1])
		prestos_freq_data.append(group["PRESTOsummed_peaks"][harmonic][1])
		prestoc_freq_data.append(group["PRESTOcoherent_peaks"][harmonic][1])
		try:
			double_freq_data.append(group["double_peaks"][harmonic][1])
		except:
			print("no double data at")
			print(group)

		parameters = group["parameters"]

		bphase_data.append(group["parameters"]["bphase"])

	print(bphase_data)
	print(single_snr_data)

	textstr = ''
	for key in parameters.keys():
		textstr += key + ": " + str(parameters[key]) + "\n"


	fig = plt.figure()
	ax = Axes3D(fig)

#	ax.scatter(bphase_data, bfloat_snr_data, bfloat_freq_data, marker='.', c='r')
#	ax.scatter(bphase_data, single_snr_data, single_freq_data, marker='x', c='g')
#	ax.scatter(bphase_data, double_snr_data, double_freq_data, marker='o', facecolor='none',edgecolor='b')
#	ax.scatter(bphase_data, prestoc_snr_data, prestoc_freq_data, marker='^', facecolor='k',edgecolor='none')
#	ax.scatter(bphase_data, prestos_snr_data, prestos_freq_data, marker='2', facecolor='m',edgecolor='none')
#	ax.set_xlabel('bphase')
#	ax.set_ylabel('response')
#	ax.set_zlabel('frequency')
#
#	plt.show()

	ax.scatter(bphase_data, bfloat_snr_data, bfloat_accn_data, marker='.', c='r')
	ax.scatter(bphase_data, single_snr_data, single_accn_data, marker='x', c='g')
	ax.scatter(bphase_data, double_snr_data, double_accn_data, marker='o', facecolor='none',edgecolor='b')
	ax.scatter(bphase_data, prestoc_snr_data, prestoc_accn_data, marker='^', facecolor='k',edgecolor='none')
	ax.scatter(bphase_data, prestos_snr_data, prestos_accn_data, marker='2', facecolor='m',edgecolor='none')
	ax.set_xlabel('bphase')
	ax.set_ylabel('response')
	ax.set_zlabel('acceleration')

	plt.show()
