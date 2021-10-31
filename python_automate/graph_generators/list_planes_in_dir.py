import json
import math
import os
import csv
import analysis_funcs

if __name__ == "__main__":
	directory = "/home/jack/hdd/noise/"
	datFileList = os.listdir(directory)
	for filename in datFileList:
		if filename[-9:] == "peaks.dat":
			aaOutputDatFileName = directory + filename
			parameters = analysis_funcs.params_from_filename(filename)
			print(filename)
			with open("noisepeaks.txt", 'a') as outfile:
				outfile.write(aaOutputDatFileName + "\n" + str(parameters["period"]) + "\n")


	