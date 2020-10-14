import csv

csv_fileds = ['Parameter', 'Variable', 'Variable Location']
cvs_file = 'parameterMap.csv'

in_file = open('rawVarData', 'r')

lines = in_file.readlines()

with open(cvs_file, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(csv_fileds)
	
	for line in lines:
		strs = line.split('=')
		param = strs[-1].split('\"')[-2]
		temp = strs[-2].split()
		var_loc = './' + temp[0][:-1]
		var = temp[-1]
		csvwriter.writerow([param, var, var_loc])
