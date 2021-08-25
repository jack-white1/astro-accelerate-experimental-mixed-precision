import json
import math
import datetime

def relative_difference (a,b):
	try:
		return 100*(a-b)/(0.5*(a+b))
	except:
		return 0

def group_results(resultsFilePath, nPeaks, dateSince):
	rawResultsList = []
	with open(resultsFilePath, "r") as resultsFile:
		for line in resultsFile:
			rawResultsList.append(json.loads(line))

	results = []

	for i in rawResultsList:
		peak_list = i["peak_list"]
		precision = i["precision"]
		parameters = {"period": i["period"],\
		"width": i["width"],\
		"snrpeak": i["snrpeak"],\
		"dm": i["dm"],\
		"nbits": i["nbits"],\
		"nchans": i["nchans"],\
		"tsamp": i["tsamp"],\
		"tobs": i["tobs"],\
		"fch1": i["fch1"],\
		"foff": i["foff"],\
		"binary": i["binary"],\
		"bper": i["bper"],\
		"bphase": i["bphase"],\
		"bpmass": i["bpmass"],\
		"bcmass": i["bcmass"],\
		}
		aaOutputDatFileName = i["aaOutputDatFileName"]
		date = i["date"]

		if datetime.datetime.strptime(date, "%d-%m-%Y-%H-%M-%S.%f") > dateSince:
			results.append({"peak_list": peak_list, "precision":precision, "parameters":parameters, "date":date, "aaOutputDatFileName":aaOutputDatFileName})

	grouped_results = []
	for result in results:
		result_group = {}
		if result["precision"] == "bfloat":
			result_group["bfloat_peaks"] = json.loads(result["peak_list"])[0:nPeaks]
			result_group["parameters"] = result["parameters"]
			result_group["aaOutputDatFileName"] = result["aaOutputDatFileName"]
			result_group["date"] = result["date"]
			for candidate in results:
				if candidate["parameters"] == result["parameters"]:
					if candidate["precision"] == "single":
						result_group["single_peaks"] = json.loads(candidate["peak_list"])[0:nPeaks]
					if candidate["precision"] == "double":
						result_group["double_peaks"] = json.loads(candidate["peak_list"])[0:nPeaks]
			results.remove(result)
			grouped_results.append(result_group)
	#print("Returning grouped_results: " + str(grouped_results))
	return grouped_results

def extract_diff_hist_save_params(grouped_results, harmonic, index):

	b2s_hist = []
	s2d_hist = []
	b2d_hist = []

	for group in grouped_results:
		print("group: " + str(group))
		if datetime.datetime.strptime(group["date"], '%d-%m-%Y-%H-%M-%S.%f') > datetime.datetime(2021,8,20):
			try:
				bfloat_peak = group["bfloat_peaks"][harmonic][index]
				single_peak = group["single_peaks"][harmonic][index]
				double_peak = group["double_peaks"][harmonic][index]


				b2s_diff = relative_difference(bfloat_peak,single_peak)
				s2d_diff = relative_difference(single_peak,double_peak)
				b2d_diff = relative_difference(bfloat_peak,double_peak)

			#print(str(b2s_diff) +"\t"+ str(s2d_diff) +"\t"+ str(b2d_diff))

				b2s_hist.append([b2s_diff,group["parameters"]])
				s2d_hist.append([s2d_diff,group["parameters"]])
				b2d_hist.append([b2d_diff,group["parameters"]])
			except:
				print("nothing to add to histogram, dump group:")
				print(group)
				print("\n\n\n")

	return b2s_hist, s2d_hist, b2d_hist

def extract_diff_hist(grouped_results, harmonic, index):

	b2s_hist = []
	s2d_hist = []
	b2d_hist = []

	for group in grouped_results:
		try:
			bfloat_peak = group["bfloat_peaks"][harmonic][index]
			single_peak = group["single_peaks"][harmonic][index]
			double_peak = group["double_peaks"][harmonic][index]


			b2s_diff = relative_difference(bfloat_peak,single_peak)
			s2d_diff = relative_difference(single_peak,double_peak)
			b2d_diff = relative_difference(bfloat_peak,double_peak)

			#print(str(b2s_diff) +"\t"+ str(s2d_diff) +"\t"+ str(b2d_diff))

			b2s_hist.append(b2s_diff)
			s2d_hist.append(s2d_diff)
			b2d_hist.append(b2d_diff)
		except:
			print("nothing to add to histogram, dump group:")
			print(group)
			print("\n\n\n")

	return b2s_hist, s2d_hist, b2d_hist

def extract_diff_hist_perc_diff_b2s(grouped_results, harmonic, index):

	b2s_hist = []

	for group in grouped_results:
		try:
			bfloat_peak = group["bfloat_peaks"][harmonic][index]
			single_peak = group["single_peaks"][harmonic][index]

			b2s_diff = abs(relative_difference(bfloat_peak,single_peak))

			b2s_hist.append([b2s_diff, bfloat_peak])

		except:
			print("nothing to add to histogram, dump group:")
			print(group)
			print("\n\n\n")

	return b2s_hist

def extract_bounded_diff_hist(grouped_results, harmonic, index, lb, ub):

	b2s_hist = []
	s2d_hist = []
	b2d_hist = []

	for group in grouped_results:
		try:
			bfloat_peak = group["bfloat_peaks"][harmonic][index]
			single_peak = group["single_peaks"][harmonic][index]
			double_peak = group["double_peaks"][harmonic][index]


			b2s_diff = relative_difference(bfloat_peak,single_peak)
			s2d_diff = relative_difference(single_peak,double_peak)
			b2d_diff = relative_difference(bfloat_peak,double_peak)

			#print(str(b2s_diff) +"\t"+ str(s2d_diff) +"\t"+ str(b2d_diff))
			#print("Single peak: " + str(single_peak))
			if (single_peak > lb) and (single_peak < ub):
				b2s_hist.append(b2s_diff)
				s2d_hist.append(s2d_diff)
				b2d_hist.append(b2d_diff)
		except:
			print("nothing to add to histogram, dump group:")
			print(group)
			print("\n\n\n")

	return b2s_hist, s2d_hist, b2d_hist

def rounddown(number, nearest):
	if number < 0:
		return nearest*(-1)*math.ceil(abs(number/nearest)) - nearest
	elif number > 0:
		return nearest*math.floor(number/nearest) - nearest
	else:
		return (-1)*nearest

def roundup(number, nearest):
	if number < 0:
		return nearest*(-1)*math.floor(abs(number/nearest)) + nearest
	elif number > 0:
		return nearest*math.ceil(number/nearest) + nearest
	else:
		return nearest

def params_from_filename(filename):
	print("extracing params from " + filename)
	params = {}
	params_list = filename.split('_')
	i = 0
	for i in range(0, len(params_list), 2):
		try:
			params[params_list[i]] = float(params_list[i+1])
		except:
			print("Reached end of string")
		try:
			date = datetime.datetime.strptime(params_list[i], '%d-%m-%Y-%H-%M-%S.%f')
			params["date"] = params_list[i]
		except:
			#print("params_list: " + str(params_list) + " params_list[i]:" +params_list[i] + " is not datetime")
			pass
	for element in params_list:
		if element == "bfloat":
			params["precision"] = "bfloat"
		if element == "single":
			params["precision"] = "single"
		if element == "double":
			params["precision"] = "double"
	print("Returning params: " + str(params))
	return params

#add the bfloat, single, double peak if all parameters EXCEPT target are default values
def extract_1D_hist(grouped_results, harmonic, index, target_axis):
	b2s_hist = []
	s2d_hist = []
	b2d_hist = []

	for group in grouped_results:
		try:
			print(group)
			bfloat_peak = group["bfloat_peaks"][harmonic][index]
			single_peak = group["single_peaks"][harmonic][index]
			double_peak = group["double_peaks"][harmonic][index]


			b2s_diff = relative_difference(bfloat_peak,single_peak)
			s2d_diff = relative_difference(single_peak,double_peak)
			b2d_diff = relative_difference(bfloat_peak,double_peak)


			if check_1d(group["parameters"], target_axis):
				b2s_hist.append(b2s_diff)
				print("appending: " + str(b2s_diff))
				s2d_hist.append(s2d_diff)
				print("appending: " + str(s2d_diff))
				b2d_hist.append(b2d_diff)
				print("appending: " + str(b2d_diff))
		except:
			print("nothing to add to histogram, dump group:")
			print(group)
			#print("\n\n\n")
#			pass

	return b2s_hist, s2d_hist, b2d_hist

#check all params are default, return true if the specified axis is different
def check_1d(params, target_axis):
	is_on_axis = True
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
	for param in params:
		if param != target_axis:
			if (not math.isnan(params[param])) and (params[param] != defaultParameters[param][0]):
				is_on_axis = False
				#print("FLAG1")
				#print(str(params[param]) + " is not equal to " + str(defaultParameters[param][0]))
		if param == target_axis:
			if params[param] == defaultParameters[param]:
				is_on_axis = False
				#print("FLAG2")
	print("is on axis: " + str(is_on_axis))
	return (is_on_axis)



