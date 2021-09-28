import analysis_funcs
import datetime
import matplotlib.pyplot as plt


if __name__ == "__main__":
	nPeaks=3
	grouped_results = analysis_funcs.group_results("results.txt", nPeaks, datetime.datetime(2021,9,14,23), datetime.datetime(2021,9,15,6))
	#print(grouped_results)
	#grouped_results = analysis_funcs.group_results("results.txt", 3, datetime.datetime(2021,9,8,12), datetime.datetime(2021,9,8,20))
	period_data = []
	
	bfloat_harm_sum_data = []
	single_harm_sum_data = []
	double_harm_sum_data = []

	bfloat_accn_data = []
	single_accn_data = []
	double_accn_data = []
	
	bfloat_snr_data = []
	single_snr_data = []
	double_snr_data = []


	parameters = ''

	for group in grouped_results:
		print(group)
		bfloat_harm_sum = 0
		single_harm_sum = 0
		double_harm_sum = 0

		for harmonic in range(nPeaks):
			bfloat_harm_sum += group["bfloat_peaks"][harmonic][2]
			single_harm_sum += group["single_peaks"][harmonic][2]


		harmonic = 2 	# 0 = fundamental, 1 = first harmonic, 2 = second harmonic etc

		bfloat_harm_sum_data.append(bfloat_harm_sum)
		single_harm_sum_data.append(single_harm_sum)

		bfloat_accn_data.append(group["bfloat_peaks"][harmonic][0])
		single_accn_data.append(group["single_peaks"][harmonic][0])

		bfloat_snr_data.append(group["bfloat_peaks"][harmonic][2])
		single_snr_data.append(group["single_peaks"][harmonic][2])

		parameters = group["parameters"]

		period_data.append(group["parameters"]["period"])

	print(period_data)
	print(single_snr_data)

	textstr = ''
	for key in parameters.keys():
		textstr += key + ": " + str(parameters[key]) + "\n"


#	plt.scatter(period_data, bfloat_accn_data, marker='.', c='r')
#	plt.scatter(period_data, single_accn_data, marker='x', c='g')
#	plt.scatter(period_data, double_accn_data, marker='o', facecolor='none',edgecolor='b')
#	plt.xlabel('period')
#	plt.ylabel('Acceleration of fundamental peak')
#	plt.title('How period affects acceleration of fundamental peak, tobs=50')
#	plt.legend(['bfloat','single','double'])

#	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#	plt.text(0, -0.005, textstr, fontsize=8,verticalalignment='top',bbox=props)

#	plt.show()

	plt.scatter(period_data, bfloat_snr_data, marker='.', c='r')
	plt.scatter(period_data, single_snr_data, marker='x', c='g')
	plt.xlabel('period')
	plt.ylabel('pow of second harmonic peak')
	plt.title('How period affects pow of second harmonic peak')
	plt.legend(['bfloat','single','double'])

	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

	plt.text(22.8995, 3250, textstr, fontsize=8,verticalalignment='top',bbox=props)

	plt.show()

#	plt.scatter(period_data, bfloat_harm_sum_data, marker='.', c='r')
#	plt.scatter(period_data, single_harm_sum_data, marker='x', c='g')
#	plt.scatter(period_data, double_harm_sum_data, marker='o', facecolor='none',edgecolor='b')
#	plt.xlabel('period')
#	plt.ylabel('Sum of 32 harmonics')
#	plt.title('How period affects snr of 32 summed harmonics')
#	plt.legend(['bfloat','single','double'])

#	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
#	plt.text(0.75, 80000, textstr, fontsize=8,verticalalignment='top',bbox=props)

#	plt.show()
