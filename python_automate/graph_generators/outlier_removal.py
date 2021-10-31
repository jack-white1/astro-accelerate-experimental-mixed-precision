import json
import math
import os
import csv
import analysis_funcs
import fnmatch


if __name__ == "__main__":

	directory = "/home/jack/hdd/arc/dat/dat/"
	f = open("thermal_outliers.txt")
	lines = f.readlines()


	a = []
	for line in lines:
		a.append(line.split("\n")[0])

	#print(a)

	files_to_delete = []
	for seed in a:
		print("finding " + str(seed))
		missing_files = analysis_funcs.find("seed_" + seed + "_*.dat", directory)
		for file in missing_files:
			files_to_delete.append(file)

	print(files_to_delete)

	for filepath in files_to_delete:
		if os.path.exists(filepath):
			print("remove " + filepath)
			#os.remove(filepath)
		else:
			print(filepath + " does not exist")

