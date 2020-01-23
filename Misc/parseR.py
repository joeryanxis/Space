import csv
reader = csv.reader(open('resource2.csv', 'r'), delimiter = ",")

for row in reader:
	print 'ID: ' + row[0] + '\n' + 'Image: ' + row[1] + '\n' + 'Species ID: ' + row[2] + '\n' + 'Species: ' + row[3] + '\n' + 'Sex: ' + row[4] + '\n' + 'River: ' + row[5] + '\n'