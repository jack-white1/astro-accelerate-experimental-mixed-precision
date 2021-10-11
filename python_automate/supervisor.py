import os
import math
import numbers
import subprocess
import multiprocessing as mp
import numpy as np
import csv
import itertools
import json
from datetime import datetime
import time
import random
import string
import shutil

def round_trailing_zeros(targetDict):
	roundedDict = {}
	for key in targetDict:
		if targetDict[key] % 1 == 0:
			roundedDict[key] = int(targetDict[key])
		else:
			roundedDict[key] = targetDict[key]
	return roundedDict


def is_non_zero_file(filepath):
	return (os.path.isfile(filepath) and (os.path.getsize(filepath) > 0))

def deleteLastLine(filepath):
	lines = []
	with open(filepath, 'r+') as f:
		lines = f.readlines()
		f.truncate(0)
	lines = lines[:-1]
	with open(filepath, 'a') as f:
		f.writelines(lines)

def returnNumLines(filepath):
	with open(filepath,'r') as f:
		Counter = 0
		Content = f.read()
		CoList = Content.split("\n")
		for i in CoList:
			if i:
				Counter += 1
		return Counter

def returnLastLine(filepath):
	with open(filepath, 'r') as f:
		lines = f.read().splitlines()
		last_line = lines[-1]
		return last_line

def makeRandomFakeParameters(parameterBounds = {}):
	nsamps = 1
	if parameterBounds == {}:
		parameterBounds = {'seed': [0,1],\
					'period': [1.25, 8000],\
					'width':[4,50],\
					'snrpeak':[0.0125, 0.125],\
					'dm':[5,500],\
					'nbits':[8],\
					'nchans':[1024],\
					'tsamp':[128],\
					'tobs':[600],\
					'fch1':[1550],\
					'foff':[0.292968752],\
					'binary':[float('nan')],\
					'bper':[1.5, 336],\
					'bphase':[0.2],\
					'bpmass':[1.0, 1.5],\
					'bcmass':[0.1, 5.0]}

	fakeParameters = {}
	for key in parameterBounds:
		try:
			lb = parameterBounds[key][0]
			ub = parameterBounds[key][1]
			if key == "seed":
				fakeParameters[key] = random.randint(0,2147483647)
			elif key == "dm":
				fakeParameters[key] = np.random.randint(lb,ub,nsamps).tolist()[0]
			else:
				fakeParameters[key] = [round(elem, 5) for elem in np.random.uniform(lb,ub,nsamps).tolist()][0]
		except:
			fakeParameters[key] = [parameterBounds[key][0]][0]
			print(key + " is not a variable parameter")

	return fakeParameters

def makeLogUniformFakeParameters(parameterBounds = {}):
	nsamps = 1
	if parameterBounds == {}:
		parameterBounds = {'seed': [0,1],\
					'period': [1.25, 1000],\
					'width':[4,50],\
					'snrpeak':[0.0125, 0.125],\
					'dm':[5,500],\
					'nbits':[8],\
					'nchans':[1024],\
					'tsamp':[128],\
					'tobs':[600],\
					'fch1':[1550],\
					'foff':[0.292968752],\
					'binary':[float('nan')],\
					'bper':[1.5, 336],\
					'bphase':[0.2],\
					'bpmass':[1.0, 1.5],\
					'bcmass':[0.1, 5.0]}
	fakeParameters = {}
	base = 2
	for key in parameterBounds:
		if len(parameterBounds[key]) == 2:
			if key == "seed":
				fakeParameters[key] = random.randint(0,2147483647)
			elif key == "dm":
				lb = math.log(parameterBounds[key][0],base)
				ub = math.log(parameterBounds[key][1],base)
				fakeParameters[key] = [int(round(base**elem, 5)) for elem in np.random.uniform(lb,ub,nsamps).tolist()][0]
			else:
				lb = math.log(parameterBounds[key][0],base)
				ub = math.log(parameterBounds[key][1],base)
				fakeParameters[key] = [round(base**elem, 5) for elem in np.random.uniform(lb,ub,nsamps).tolist()][0]
		elif len(parameterBounds[key]) == 1:
			fakeParameters[key] = [parameterBounds[key][0]][0]
#				print(key + " is not a variable parameter")
	return fakeParameters

def make1DFakeParameters(axis):
	nsamps = 25

	parameterBounds = {'seed' : [0,1],\
					'period': [1.25, 8000],\
					'width':[4,50],\
					'snrpeak':[0.0125, 0.125],\
					'dm':[5,500],\
					'nbits':[8],\
					'nchans':[1024],\
					'tsamp':[128],\
					'tobs':[600],\
					'fch1':[1550],\
					'foff':[0.292968752],\
					'binary':[float('nan')],\
					'bper':[1.5, 336],\
					'bphase':[0.2],\
					'bpmass':[1.0, 1.5],\
					'bcmass':[0.1, 5.0]}

	defaultParameters = {'seed' : [random.randint(0,2147483647)],\
					'period': [22.9],\
					'width':[47],\
					'snrpeak':[1],\
					'dm':[50],\
					'nbits':[8],\
					'nchans':[1024],\
					'tsamp':[128],\
					'tobs':[600],\
					'fch1':[1550],\
					'foff':[0.292968752],\
					'binary':[float('nan')],\
					'bper':[2.45],\
					'bphase':[0.2],\
					'bpmass':[1.338],\
					'bcmass':[1.249]}

	fakeParameters = defaultParameters
	try:
		lb = parameterBounds[axis][0]
		ub = parameterBounds[axis][1]
		if axis == "dm":
			fakeParameters[axis] = np.random.randint(lb,ub,nsamps).tolist()
		else:
			fakeParameters[axis] = [round(elem, 2) for elem in np.random.uniform(lb,ub,nsamps).tolist()]
	except:
		fakeParameters[axis] = [parameterBounds[axis][0]]
		print(axis + " is not a variable parameter")

	return fakeParameters

def make1DLinSpaceFakeParameters(axis):
	nsamps = 300

#	parameterBounds = {'seed' : [0,1],\
	parameterBounds = {'seed' : [1970963475],\
					'period': [22.89843, 22.9],\
					'width':[4,50],\
					'snrpeak':[0.0125, 0.125],\
					'dm':[5,500],\
					'nbits':[8],\
					'nchans':[1024],\
					'tsamp':[128],\
					'tobs':[600],\
					'fch1':[1550],\
					'foff':[0.292968752],\
					'binary':[float('nan')],\
					'bper':[1.5, 336],\
					'bphase':[0.51, 0.54],\
					'bpmass':[1.0, 1.5],\
					'bcmass':[0.1, 5.0]}

#	defaultParameters = {'seed' : [random.randint(0,2147483647)],\
	defaultParameters = {'seed' : [1970963475],\
					'period': [22.9],\
					'width':[47],\
					'snrpeak':[1],\
					'dm':[50],\
					'nbits':[8],\
					'nchans':[1024],\
					'tsamp':[128],\
					'tobs':[600],\
					'fch1':[1550],\
					'foff':[0.292968752],\
					'binary':[float('nan')],\
					'bper':[2.45],\
					'bphase':[0.2],\
					'bpmass':[1.338],\
					'bcmass':[1.249]}

	fakeParameters = defaultParameters
	try:
		lb = parameterBounds[axis][0]
		ub = parameterBounds[axis][1]
		if axis == "dm":
			fakeParameters[axis] = [round(elem, 0) for elem in np.linspace(lb,ub,nsamps).tolist()]
		else:
			fakeParameters[axis] = [round(elem, 8) for elem in np.linspace(lb,ub,nsamps).tolist()]
	except:
		fakeParameters[axis] = [parameterBounds[axis][0]]
		print(axis + " is not a variable parameter")

	#print(fakeParameters)
	return fakeParameters


def makeFakeToDoList(fakeParameters):
	keys, values = zip(*fakeParameters.items())
	permutations_dicts = [dict(zip(keys,v)) for v in itertools.product(*values)]
	for permutation in permutations_dicts:
		with open("fakeToDoList.txt", "a") as f:
			f.write(str(json.dumps(permutation))+"\n")

def makeRandomFakeToDoList(fakeParameters):
	for parameter_set in fakeParameters:
		with open("fakeToDoList.txt", "a") as f:
			f.write(str(json.dumps(parameter_set))+"\n")

def makeFilFile(parameters):
	t_start = time.perf_counter()
	fakeArguments = ''
	filFileName = ''

	for key in parameters:
		filFileName += key + '_' + str(parameters[key]) + '_'
		if math.isnan(parameters[key]):
			fakeArguments += (' -' + key)
		elif isinstance(parameters[key], numbers.Number):
			fakeArguments += (' -'+ key + ' ' + str(parameters[key]))
		else:
			print("Error reading parameters")

	now = datetime.now() # current date a
	filFileName += now.strftime("%d-%m-%Y-%H-%M-%S.%f_")
	aaOutputDatFileName = "./dat/"+filFileName
	filFileName ='/home/jack/data/fil/' +filFileName+ '.fil'
	fakeArguments +=(' > ' + filFileName)
	fakeExecutable = '/home/jack/sigproc/executables/bin/fake ' + fakeArguments
	#print(fakeExecutable)
	os.system(fakeExecutable)
	filepath_parameters = {'filepath':filFileName, 'parameters':parameters}
	with open("aaToDoList.txt", "a") as f:
		f.write(str(json.dumps(filepath_parameters)) + "\n")
	t_finish = time.perf_counter()
	print("1 Thread of makeFilFile took: " +str(t_finish-t_start)+ " seconds")


def makeDatFile(filepath, parameters, precision):

	standardInputFilePath = '/home/jack/astro-accelerate-experimental-mixed-precision/python_automate/input_files/standard_input.txt'
	tempInputFilePath = '/home/jack/astro-accelerate-experimental-mixed-precision/python_automate/input_files/temp_input.txt'

	aaPath = {'bfloat':'/home/jack/astro-accelerate-experimental-mixed-precision/astro-accelerate-partial-bfloat/astro-accelerate/astro-accelerate',\
			'single':'/home/jack/astro-accelerate-experimental-mixed-precision/astro-accelerate-single/astro-accelerate/astro-accelerate',
			'double':'/home/jack/astro-accelerate-experimental-mixed-precision/astro-accelerate-double/astro-accelerate/astro-accelerate'}

	aaOutputDatFileName = ''
	for key in parameters:
		aaOutputDatFileName += key + '_' + str(parameters[key]) + '_'
	aaOutputDatFileName = "/home/jack/data/dat/" + aaOutputDatFileName + filepath[-31:-5] + '_' + precision + '_'

	aaTargetDM = str(parameters['dm'])

	minDM = max(1,int(float(aaTargetDM))-50)
	maxDM = int(float(aaTargetDM)) + 50

	with open(standardInputFilePath, 'r') as file:
			inputFileText = file.read()

	inputFileText = "range\t"+str(minDM)+"\t"+str(maxDM)+"\t" + inputFileText
	inputFileText += filepath

	print(inputFileText)

	with open(tempInputFilePath, "w+") as text_file:
		text_file.write(inputFileText)

	aaExecutable = aaPath[precision]+' '+ tempInputFilePath + ' ' + aaTargetDM + ' ' + aaOutputDatFileName #+ ' >/dev/null 2>&1'
	print("Running AA...")
	print(aaExecutable)
	os.system(aaExecutable)
	print("Finished AA...")
	aaOutputDatFileName += "peaks.dat"
	print(aaOutputDatFileName)


def makePrestoDatFile(filepath, parameters, precision):

	rand_str_length = 25
	prestoTargetDM = 50
	prestoNumharm = 1
	prestoZmax = 200
	rand_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(rand_str_length))
	#make symlink to fil file
	targetFilFile = filepath
	alias = "/home/jack/hdd/symlinks/" + rand_str + ".fil"
	os.symlink(filepath, alias)

	prepsubbandExecutable = '/home/jack/Documents/PRESTO/presto/bin/prepsubband -o ' + rand_str + ' -nobary '+ alias + ' -lodm '+str(prestoTargetDM)+' -dmstep 1 -numdms 1'
	print(prepsubbandExecutable)
	os.system(prepsubbandExecutable)
	shutil.move('/home/jack/Documents/aa_mixed/astro-accelerate-experimental-mixed-precision/python_automate/' + rand_str + "_DM" +str(prestoTargetDM)+ ".00.dat",'/home/jack/hdd/presto/' + rand_str + ".dat")
	shutil.move('/home/jack/Documents/aa_mixed/astro-accelerate-experimental-mixed-precision/python_automate/' + rand_str + "_DM" +str(prestoTargetDM)+ ".00.inf",'/home/jack/hdd/presto/' + rand_str + ".inf")
	
	accelsearchExecutable = '/home/jack/Documents/PRESTO/presto/bin/accelsearch -flo 0 -fhi 800 -zmax '+str(prestoZmax)+' -wmax 0 -numharm '+str(prestoNumharm)+' /home/jack/hdd/presto/' + rand_str + ".dat"
	print(accelsearchExecutable)
	os.system(accelsearchExecutable)

	accelsearchOutput = '/home/jack/hdd/presto/' +rand_str + "_ACCEL_" + str(prestoZmax)
	accelsearchMetaOutput = ''
	for key in parameters:
		accelsearchMetaOutput += key + '_' + str(parameters[key]) + '_'
	accelsearchMetaOutput += filepath[-31:-5] + '_PRESTO_peaks.dat'
	print("filepath: ")
	print(filepath)
	print("parameters: ")
	print(parameters)
	print("precision: ")
	print(precision)
	print("accelsearchOutput: " + accelsearchOutput)
	print("accelsearchMetaOutput: " + accelsearchMetaOutput)
	shutil.move(accelsearchOutput, '/home/jack/hdd/presto/' + accelsearchMetaOutput)
	os.remove('/home/jack/hdd/presto/' + rand_str + ".dat")
	os.remove('/home/jack/hdd/presto/' + rand_str + ".inf")
	os.remove('/home/jack/hdd/presto/' + rand_str + "_ACCEL_" + str(prestoZmax) + ".cand")
	#prepsubband with 100char random filename output and symlink input

	#accelsearch with 100char random filename input, move it to /hdd/presto/original_fil_filename
	#delete all intermediate presto files
	#os.unlink()


if __name__ == "__main__":

#	fakeParameters = make1DFakeParameters("bcmass")
#	print(fakeParameters)
#	makeFakeToDoList(fakeParameters)

#	fakeParameters = make1DLinSpaceFakeParameters("bphase")
#	print(fakeParameters)
#	makeFakeToDoList(fakeParameters)


	randomSamples = 32
	fakeParameters = []
	for i in range(randomSamples):
		fakeParameters.append(makeLogUniformFakeParameters())
	print(fakeParameters)
	makeRandomFakeToDoList(fakeParameters)
#
	numthreads = 32

	while is_non_zero_file("fakeToDoList.txt"):
		numlines = returnNumLines("fakeToDoList.txt")
		print("There are: "+str(numlines)+" lines in fakeToDoList.txt")
		if numlines < numthreads:
			numthreads = numlines
		params_map = []
		for i in range(numthreads):
			last_line = returnLastLine("fakeToDoList.txt")
			deleteLastLine("fakeToDoList.txt")
			parameters = json.loads(last_line)
			params_map.append(parameters)
		print("Running " + str(numthreads) + " processes concurrently:")
		with mp.Pool(numthreads) as p:
			p.map(makeFilFile, params_map)


	while is_non_zero_file("aaToDoList.txt"):
		last_line = returnLastLine("aaToDoList.txt")
		deleteLastLine("aaToDoList.txt")
		filepath_parameters = json.loads(last_line)
		filepath = filepath_parameters['filepath']
		parameters = round_trailing_zeros(filepath_parameters['parameters'])
		print(parameters)
		makeDatFile(filepath, parameters, 'bfloat')
		makeDatFile(filepath, parameters, 'single')
		makeDatFile(filepath, parameters, 'double')
#		makePrestoDatFile(filepath, parameters, 'presto')
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			print(filepath + " does not exist")





















#	os.system("python3 graph_generators/dat2results.py")

#
#	if os.path.exists("aaToDoList.txt"):
#		os.remove("aaToDoList.txt")
#	else:
#		print("aaToDoList.txt does not exist")
#
#	if os.path.exists("fakeToDoList.txt"):
#		os.remove("fakeToDoList.txt")
#	else:
#		print("fakeToDoList.txt does not exist")
#
