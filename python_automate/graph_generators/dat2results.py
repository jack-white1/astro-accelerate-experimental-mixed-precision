import json
import math
import os
import csv
import analysis_funcs

if __name__ == "__main__":
	directory = "/home/jack/hdd/dat/"
	datFileList = os.listdir(directory)
	for filename in datFileList:
		#print(filename)
		#print(filename[-9:])
		if filename[-9:] == "peaks.dat":
			aaOutputDatFileName = directory + filename
			#print(aaOutputDatFileName)
			parameters = analysis_funcs.params_from_filename(filename)

			peaks = []
			with open(aaOutputDatFileName, newline='') as csvfile:
				datreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
				for row in datreader:
					peaks.append([float(row[0]),float(row[3]),float(row[5])]) #acceleration, frequency, pow=4/snr=5
					#print("pow: " + row[4] + ", snr: " + row[5])


		#print(data)
		#data = data.sort(key = lambda x: x[2])
		#print(sorted(data, key = lambda x: x[2]))
		#data = np.asarray(sorted(data, key = lambda x: x[2]))
			peaks = sorted(peaks, key = lambda x: x[2], reverse=True)
		#print(peaks[0:100])
			#print("peaks: ", peaks)
			max_freq = sorted(peaks, key = lambda x: x[1], reverse=True)[0][1]
			#print("max_freq: " + str(max_freq))

		#max_result = data[np.argmax(data[:,2]),:].tolist()

			max_result = peaks[0]
			#print("peak at " + str(max_result))

			period = parameters['period']*0.001		# convert to ms
			fundamental_freq = 1/period				# Hz
			#print("fundamental_freq at : " + str(fundamental_freq) + " Hz" )

			maxBands = 100
			nBands = min(math.floor(max_freq/fundamental_freq),maxBands)

			bandBoundaries = []

			#print("nBands = " + str(nBands))
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
			#print("results: "+str(results))
			with open("results.txt", "a") as f:
				f.write(json.dumps(results)+"\n")


#	directory = "/home/jack/hdd/presto/"
#	datFileList = os.listdir(directory)
#	for filename in datFileList:
#		print(filename)
#		print(filename[-16:])
#		if filename[-16:] == "PRESTO_peaks.dat":
#			aaOutputDatFileName = directory + filename
#			print(aaOutputDatFileName)
#			parameters = analysis_funcs.params_from_filename(filename)
#			print(parameters)
#
#			peaks = []
#			with open(aaOutputDatFileName, newline='') as csvfile:
#				datreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
#				presto_fundamental = []
#				i = 0
#				for row in datreader:
#					if i == 3:
#						print(row[0].split())
#						presto_fundamental = row[0].split()
#					i+=1
#				accn = presto_fundamental[9].split('(')[0]
#				freq = presto_fundamental[6].split('(')[0]
#				response = presto_fundamental[2] # 1 = sigma, 2 = summed power, 3 = coherent power
#			peaks.append([float(accn),float(freq),float(response)])
#			precision = parameters["precision"]+"summed"
#			print("PRECISION" + precision)
#
#			results = {"peak_list":json.dumps(peaks),'precision':precision,"filFilePath": '.'.join(filename.split(".")[0:-2]) + ".fil","aaOutputDatFileName":aaOutputDatFileName}
#			results.update(parameters)
			results["precision"] = precision
			print("results: "+str(results))
			with open("results.txt", "a") as f:
				f.write(json.dumps(results)+"\n")

	directory = "/home/jack/hdd/presto/"
	datFileList = os.listdir(directory)
	for filename in datFileList:
		print(filename)
		print(filename[-16:])
		if filename[-16:] == "PRESTO_peaks.dat":
			aaOutputDatFileName = directory + filename
			print(aaOutputDatFileName)
			parameters = analysis_funcs.params_from_filename(filename)
			print(parameters)

			peaks = []
			with open(aaOutputDatFileName, newline='') as csvfile:
				datreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
				presto_fundamental = []
				i = 0
				for row in datreader:
					if i == 3:
						print(row[0].split())
						presto_fundamental = row[0].split()
					i+=1
				accn = presto_fundamental[9].split('(')[0]
				freq = presto_fundamental[6].split('(')[0]
				response = presto_fundamental[3] # 1 = sigma, 2 = summed power, 3 = coherent power
			peaks.append([float(accn),float(freq),float(response)])
			precision = parameters["precision"]+"coherent"
			print("PRECISION" + precision)

			results = {"peak_list":json.dumps(peaks),'precision':precision,"filFilePath": '.'.join(filename.split(".")[0:-2]) + ".fil","aaOutputDatFileName":aaOutputDatFileName}
			results.update(parameters)
			results["precision"] = precision
			print("results: "+str(results))
			with open("results.txt", "a") as f:
				f.write(json.dumps(results)+"\n")

		directory = "/home/jack/hdd/presto/"
	datFileList = os.listdir(directory)
	for filename in datFileList:
		print(filename)
		print(filename[-16:])
		if filename[-16:] == "PRESTO_peaks.dat":
			aaOutputDatFileName = directory + filename
			print(aaOutputDatFileName)
			parameters = analysis_funcs.params_from_filename(filename)
			print(parameters)

			peaks = []
			with open(aaOutputDatFileName, newline='') as csvfile:
				datreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
				presto_fundamental = []
				i = 0
				for row in datreader:
					if i == 3:
						print(row[0].split())
						presto_fundamental = row[0].split()
					i+=1
				accn = presto_fundamental[9].split('(')[0]
				freq = presto_fundamental[6].split('(')[0]
				response = presto_fundamental[1] # 1 = sigma, 2 = summed power, 3 = coherent power
			peaks.append([float(accn),float(freq),float(response)])
			precision = parameters["precision"]+"sigma"
			print("PRECISION" + precision)

			results = {"peak_list":json.dumps(peaks),'precision':precision,"filFilePath": '.'.join(filename.split(".")[0:-2]) + ".fil","aaOutputDatFileName":aaOutputDatFileName}
			results.update(parameters)
			results["precision"] = precision
			print("results: "+str(results))
			with open("results.txt", "a") as f:
				f.write(json.dumps(results)+"\n")