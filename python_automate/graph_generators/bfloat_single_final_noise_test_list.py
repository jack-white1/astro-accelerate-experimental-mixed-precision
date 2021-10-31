import json
import math
import os
import csv
import analysis_funcs

if __name__ == "__main__":
	#list all file names
	#extract seed list
	#get unique seed list
	#get bfloat,single plane for each seed
	#if there are more than 2 planes with the same seed, delete all
	#write to outfile:
		#single dir
		#bfloat dir
		#period

	directory = "/home/jack/hdd/noise/"
	datFileList = os.listdir(directory)
	
	seed_list = []
	for filename in datFileList:
		if filename[-9:] == "peaks.dat":
			parameters = analysis_funcs.params_from_filename(filename)
			seed_list.append(int(parameters['seed']))

	seed_list_no_duplicates = list(dict.fromkeys(seed_list))

	for seed in seed_list_no_duplicates:
		matching_bfloat_seed_files = analysis_funcs.find("seed_" + str(seed) + "_*_bfloat_peaks.dat", directory)
		matching_single_seed_files = analysis_funcs.find("seed_" + str(seed) + "_*_single_peaks.dat", directory)
		print(matching_single_seed_files)
		print(matching_bfloat_seed_files)
		if (len(matching_single_seed_files) == 1) and (len(matching_bfloat_seed_files) == 1):
			parameters = analysis_funcs.params_from_filename(matching_single_seed_files[0])
			with open("noisepeaks.txt", 'a') as outfile:
				outfile.write(matching_bfloat_seed_files[0] + "\n" + matching_single_seed_files[0] + "\n" + str(parameters["period"]) + "\n")
