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
		parameterBounds = {	'period': [1.25, 8000],\
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
			if key == "dm":
				fakeParameters[key] = np.random.randint(lb,ub,nsamps).tolist()[0]
			else:
				fakeParameters[key] = [round(elem, 5) for elem in np.random.uniform(lb,ub,nsamps).tolist()][0]
		except:
			fakeParameters[key] = [parameterBounds[key][0]][0]
			print(key + " is not a variable parameter")
	return fakeParameters

def make1DFakeParameters(axis):
	nsamps = 25

	parameterBounds = {	'period': [1.25, 8000],\
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

	defaultParameters = {'period': [10],\
					'width':[25],\
					'snrpeak':[0.25],\
					'dm':[100],\
					'nbits':[8],\
					'nchans':[1024],\
					'tsamp':[128],\
					'tobs':[600],\
					'fch1':[1550],\
					'foff':[0.292968752],\
					'binary':[float('nan')],\
					'bper':[15],\
					'bphase':[0.2],\
					'bpmass':[1.25],\
					'bcmass':[2.0]}

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
	filFileName ='/home/jack/hdd/fil/' +filFileName+ '.fil'
	fakeArguments +=(' > ' + filFileName)
	fakeExecutable = '/home/jack/Documents/mk_sigproc/executables/bin/fake ' + fakeArguments
	os.system(fakeExecutable)
	filepath_parameters = {'filepath':filFileName, 'parameters':parameters}
	with open("aaToDoList.txt", "a") as f:
		f.write(str(json.dumps(filepath_parameters)) + "\n")
	t_finish = time.perf_counter()
	print("1 Thread of makeFilFile took: " +str(t_finish-t_start)+ " seconds")


def makeDatFile(filepath, parameters, precision):

	standardInputFilePath = '/home/jack/Documents/aa_mixed/astro-accelerate-experimental-mixed-precision/python_automate/input_files/standard_input.txt'
	tempInputFilePath = '/home/jack/Documents/aa_mixed/astro-accelerate-experimental-mixed-precision/python_automate/input_files/temp_input.txt'

	aaPath = {'bfloat':'/home/jack/Documents/aa_mixed/astro-accelerate-experimental-mixed-precision/astro-accelerate-partial-bfloat/astro-accelerate/astro-accelerate',\
			'single':'/home/jack/Documents/aa_mixed/astro-accelerate-experimental-mixed-precision/astro-accelerate-single/astro-accelerate/astro-accelerate',
			'double':'/home/jack/Documents/aa_mixed/astro-accelerate-experimental-mixed-precision/astro-accelerate-double/astro-accelerate/astro-accelerate'}

	aaOutputDatFileName = ''
	for key in parameters:
		aaOutputDatFileName += key + '_' + str(parameters[key]) + '_'
	aaOutputDatFileName = "/home/jack/hdd/dat/" + aaOutputDatFileName + filepath[-31:-5] + '_' + precision + '_'

	aaTargetDM = str(parameters['dm'])

	minDM = max(1,int(aaTargetDM)-50)
	maxDM = int(aaTargetDM) + 50

	with open(standardInputFilePath, 'r') as file:
			inputFileText = file.read()

	inputFileText = "range\t"+str(minDM)+"\t"+str(maxDM)+"\t" + inputFileText
	inputFileText += filepath

	print(inputFileText)

	with open(tempInputFilePath, "w+") as text_file:
		text_file.write(inputFileText)

	aaExecutable = aaPath[precision]+' '+ tempInputFilePath + ' ' + aaTargetDM + ' ' + aaOutputDatFileName# + ' >/dev/null 2>&1'
	print("Running AA...")
	#subprocess.run(['astro-accelerate', tempInputFilePath, aaTargetDM, aaOutputDatFileName], shell=True, cwd=aaPath[precision])
	print(aaExecutable)
	os.system(aaExecutable)
	print("Finished AA...")
	aaOutputDatFileName += "peaks.dat"
	print(aaOutputDatFileName)
	#result = subprocess.run(['ls', '-t', '/home/jack/hdd/dat'], capture_output=True)

	#datFilePath = './dat/'+result.stdout.decode("utf-8").partition('\n')[0].split()[0]
#	peaks = []
#	with open(aaOutputDatFileName, newline='') as csvfile:
#		datreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
#		for row in datreader:
#			peaks.append([float(row[0]),float(row[3]),float(row[5])]) #acceleration, frequency, snr


	#print(data)
	#data = data.sort(key = lambda x: x[2])
	#print(sorted(data, key = lambda x: x[2]))
	#data = np.asarray(sorted(data, key = lambda x: x[2]))
#	peaks = sorted(peaks, key = lambda x: x[2], reverse=True)
	#print(peaks[0:100])

#	max_freq = sorted(peaks, key = lambda x: x[1], reverse=True)[0][1]
#	print("max_freq: " + str(max_freq))

	#max_result = data[np.argmax(data[:,2]),:].tolist()

#	max_result = peaks[0]
#	print("peak at " + str(max_result))

#	period = parameters['period']*0.001		# convert to ms
#	fundamental_freq = 1/period				# Hz
#	print("fundamental_freq at : " + str(fundamental_freq) + " Hz" )

#	nBands = math.floor(max_freq/fundamental_freq)

#	bandBoundaries = []

#	print("nBands = " + str(nBands))
#	for i in range(nBands):
#		bandBoundaries.append([fundamental_freq*(i+0.9), fundamental_freq*(i+1.1)])
#	harmonics = []

#	for band in range(nBands):
#		#print("Harmonic band "+str(band)+" from "+ str(bandBoundaries[band][0]) +" Hz to "+ str(bandBoundaries[band][1]) +" Hz")
#		candidate_peak = [0,0,0]
#		for peak in peaks:
#			if ((peak[1] > bandBoundaries[band][0]) and (peak[1] < bandBoundaries[band][1]) and peak[2] > candidate_peak[2]):
#				candidate_peak = peak
#		harmonics.append(candidate_peak)

	#print("Harmonics:")
#	i = 0
#	for harmonic in harmonics:
		#print("Max peak in band "+str(i)+", [acc,f,pow] = " +str(harmonic) + " which is " + str(harmonic[1]/fundamental_freq) + "x the fundamental freq")
#		i+=1

#	results = {"peak_list":json.dumps(harmonics),'precision':precision,"filFilePath":filepath,"aaOutputDatFileName":aaOutputDatFileName}
#	results.update(parameters)
#	with open("results.txt", "a") as f:
#		f.write(json.dumps(results)+"\n")



if __name__ == "__main__":

#	fakeParameters = make1DFakeParameters("bcmass")
#	print(fakeParameters)
#	makeFakeToDoList(fakeParameters)

	randomSamples = 1
	fakeParameters = []
	for i in range(randomSamples):
		fakeParameters.append(makeRandomFakeParameters())
	print(fakeParameters)
	makeRandomFakeToDoList(fakeParameters)


	numthreads = 12

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

#	with open("aaToDoList.txt", "a") as f:
#		f.write('{"filepath": "/home/jack/hdd/fil/period_22.9_width_50.0_snrpeak_5_dm_50_nbits_8_nchans_1024_tsamp_128_tobs_600_fch1_1550_foff_0.292968752_binary_nan_bper_2.45_bphase_0.1_bpmass_1.338_bcmass_1.249_09-08-2021-11-21-26.349980_.fil", "parameters": {"period": 22.9, "width": 50.0, "snrpeak": 5, "dm": 50, "nbits": 8, "nchans": 1024, "tsamp": 128, "tobs": 600, "fch1": 1550, "foff": 0.292968752, "binary": NaN, "bper": 2.45, "bphase": 0.1, "bpmass": 1.338, "bcmass": 1.249}}')
#		f.write('{"filepath": "/home/jack/hdd/fil/period_616.6_width_25_snrpeak_0.25_dm_100_nbits_8_nchans_1024_tsamp_128_tobs_600_fch1_1550_foff_0.292968752_binary_nan_bper_15_bphase_0.2_bpmass_1.25_bcmass_2.0_17-08-2021-13-45-15.719242_.fil", "parameters": {"period": 616.6, "width": 25.0, "snrpeak": 0.25, "dm": 100, "nbits": 8, "nchans": 1024, "tsamp": 128, "tobs": 600, "fch1": 1550, "foff": 0.292968752, "binary": NaN, "bper": 15, "bphase": 0.2, "bpmass": 1.25, "bcmass": 2.0}}')


	while is_non_zero_file("aaToDoList.txt"):
		last_line = returnLastLine("aaToDoList.txt")
		deleteLastLine("aaToDoList.txt")
		filepath_parameters = json.loads(last_line)
		filepath = filepath_parameters['filepath']
		parameters = filepath_parameters['parameters']
		makeDatFile(filepath, parameters, 'bfloat')
		makeDatFile(filepath, parameters, 'single')
		makeDatFile(filepath, parameters, 'double')
#
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
#	fakeParameters = {	'period': [22.9],\
#						'width':[50.0],\
#						'snrpeak':[1],\
#						'dm':[50],\
#						'nbits':[8],\
#						'nchans':[1024],\
#						'tsamp':[128],\
#						'tobs':[600],\
#						'fch1':[1550],\
#						'foff':[0.292968752],\
#						'binary':[float('nan')],\
#						'bper':[2.45],\
#						'bphase':[0.1],\
#						'bpmass':[1.338],\
#						'bcmass':[1.249]}

#	fakeParameters = {	'period': [22.9],\
#						'width':[50.0],\
#						'snrpeak':[5],\
#						'dm':[50],\
#						'nbits':[8],\
#						'nchans':[1024],\
#						'tsamp':[128],\
#						'tobs':[600],\
#						'fch1':[1550],\
#						'foff':[0.292968752]}


#	fakeParameters = {	'period': [1.25, 8],\
#						'width':[4.0, 50.0],\
#						'snrpeak':[0.025, 1],\
#						'dm':[5, 500],\
#						'nbits':[8],\
#						'nchans':[1024],\
#						'tsamp':[128],\
#						'tobs':[600],\
#						'fch1':[1550],\
#						'foff':[0.292968752],\
#						'binary':[float('nan')],\
#						'bper':[1.5, 336],\
#						'bphase':[0.0,0.025, 0.05, 0.075, 0.1,0.125,0.15,0.175,0.2,0.225,0.25,0.275,0.3,0.325,0.35,0.375,0.4,0.425,0.45,0.475,0.5,0.525,0.55,0.575,0.6,0.625,0.65,0.675,0.7,0.725,0.75,0.775,0.8,0.825,0.85,0.875,0.9,0.925,0.95,0.975,1.0],\
#						'bpmass':[1.0, 1.35, 1.5],\
#						'bcmass':[0.1, 0.25, 5.0]}
	#each thread takes 10 mins, then 576 overnight

	#
#	with open("aaToDoList.txt", "a") as f:
#		f.write('{"filepath": "/home/jack/hdd/fil/period_22.9_width_50.0_snrpeak_5_dm_50_nbits_8_nchans_1024_tsamp_128_tobs_600_fch1_1550_foff_0.292968752_binary_nan_bper_2.45_bphase_0.1_bpmass_1.338_bcmass_1.249_09-08-2021-11-21-26.349980_.fil", "parameters": {"period": 22.9, "width": 50.0, "snrpeak": 5, "dm": 50, "nbits": 8, "nchans": 1024, "tsamp": 128, "tobs": 600, "fch1": 1550, "foff": 0.292968752, "binary": NaN, "bper": 2.45, "bphase": 0.1, "bpmass": 1.338, "bcmass": 1.249}}')
