import json
import math
import os
import csv
import analysis_funcs

if __name__ == "__main__":
	directory = "/home/jack/hdd/fil/"
	datFileList = os.listdir(directory)
	for filename in datFileList:
		filFileName = directory + filename[:-4] + '.fil'
		parameters = analysis_funcs.params_from_filename(filFileName.split("/")[-1], False)
#		print(parameters)
		print(filFileName)
		filepath_parameters = {'filepath':filFileName, 'parameters':parameters}
		with open("aaToDoList.txt", "a") as f:
			f.write(str(json.dumps(filepath_parameters)) + "\n")
