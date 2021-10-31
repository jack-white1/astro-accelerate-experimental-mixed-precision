import json
import math
import os
import csv
import analysis_funcs
import fnmatch


if __name__ == "__main__":
	directory = "/home/jack/hdd/arc/dat/dat/"
	datFileList = os.listdir(directory)
	seed_list = []
	for filename in datFileList:
		parameters = analysis_funcs.params_from_filename(filename)
		seed_list.append(parameters['seed'])

	a = set([x for x in seed_list if seed_list.count(x) <3])

	a = [str(int(x)) for x in a]

	files_to_delete = []

	for seed in a:
		missing_files = analysis_funcs.find("seed_" + seed + "_*.dat", directory)
		for file in missing_files:
			files_to_delete.append(file)

	print(files_to_delete)

	for filepath in files_to_delete:
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			print(filepath + " does not exist")

