import json
import math
import os
import csv
import analysis_funcs

if __name__ == "__main__":
	directory = "/home/jack/hdd/dat/"
	datFileList = os.listdir(directory)
	for filename in datFileList:
		aaOutputDatFileName = directory + filename
		print(aaOutputDatFileName)
		parameters = analysis_funcs.params_from_filename(filename)

		peaks = []
		with open(aaOutputDatFileName, newline='') as csvfile:
			datreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
			for row in datreader:
				peaks.append([float(row[0]),float(row[3]),float(row[5])]) #acceleration, frequency, snr


	#print(data)
	#data = data.sort(key = lambda x: x[2])
	#print(sorted(data, key = lambda x: x[2]))
	#data = np.asarray(sorted(data, key = lambda x: x[2]))
		peaks = sorted(peaks, key = lambda x: x[2], reverse=True)
	#print(peaks[0:100])
		#print("peaks: ", peaks)
		max_freq = sorted(peaks, key = lambda x: x[1], reverse=True)[0][1]
		print("max_freq: " + str(max_freq))

	#max_result = data[np.argmax(data[:,2]),:].tolist()

		max_result = peaks[0]
		print("peak at " + str(max_result))

		period = parameters['period']*0.001		# convert to ms
		fundamental_freq = 1/period				# Hz
		print("fundamental_freq at : " + str(fundamental_freq) + " Hz" )

		maxBands = 100
		nBands = min(math.floor(max_freq/fundamental_freq),maxBands)

		bandBoundaries = []

		print("nBands = " + str(nBands))
		for i in range(nBands):
			bandBoundaries.append([fundamental_freq*(i+0.5), fundamental_freq*(i+1.5)])
		harmonics = []
	
		for band in range(nBands):
			#print("Harmonic band "+str(band)+" from "+ str(bandBoundaries[band][0]) +" Hz to "+ str(bandBoundaries[band][1]) +" Hz")
			candidate_peak = [0,0,0]
			for peak in peaks:
				if ((peak[1] > bandBoundaries[band][0]) and (peak[1] < bandBoundaries[band][1]) and peak[2] > candidate_peak[2]):
					candidate_peak = peak
			if candidate_peak != [0,0,0]:
				harmonics.append(candidate_peak)

		#print("Harmonics:")
		i = 0
		for harmonic in harmonics:
			#print("Max peak in band "+str(i)+", [acc,f,pow] = " +str(harmonic) + " which is " + str(harmonic[1]/fundamental_freq) + "x the fundamental freq")
			i+=1

		results = {"peak_list":json.dumps(harmonics),'precision':parameters["precision"],"filFilePath": '.'.join(filename.split(".")[0:-2]) + ".fil","aaOutputDatFileName":aaOutputDatFileName}
		results.update(parameters)
		print("results: "+str(results))
		with open("results.txt", "a") as f:
			f.write(json.dumps(results)+"\n")