import csv

with open('results.dat') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	freq_diffs = []
	acc_diffs = []
	for row in csv_reader:
		bfloat_pow = row[0]
		bfloat_acc = row[1]
		bfloat_freq = row[2]
		bfloat_path = row[3]
		single_pow = row[4]
		single_acc = row[5]
		single_freq = row[6]
		single_path = row[7]
		#print("bfloat_freq: " + str(bfloat_freq) + "\tsingle_freq: " + str(single_freq))
		freq_diffs.append(float(bfloat_freq)-float(single_freq))
		#print("freq_diff: " + str(freq_diff))
		acc_diffs.append(float(bfloat_acc)-float(single_acc))
		#print("acc_diff: " + str(acc_diff))

	print("max(freq_diffs) = " + str(max(freq_diffs)) + ", max(acc_diffs): " + str(max(acc_diffs)))
	print("min(freq_diffs) = " + str(min(freq_diffs)) + ", min(acc_diffs): " + str(min(acc_diffs)))

	print(f'Processed {line_count} lines.')