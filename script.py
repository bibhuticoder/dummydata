import csv
from random import randint

data = []
with open("data.csv", 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			data.append({
				"firstname" : row[0],
				"lastname" : row[1],
				"gender" : row[2],
				"age" : row[3],
				"email" : row[4],
				"phone" : row[5],
				"address" : row[6] + ", " + row[7]
			})

print(data[randint(0, len(data)-1)])

