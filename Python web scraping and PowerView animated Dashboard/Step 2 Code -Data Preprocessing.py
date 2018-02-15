import csv
import operator
import copy
import pdb
from token import EQUAL
from __builtin__ import sorted

#open the csv file
reader = csv.reader(open('C:\Users\Apurva\Desktop\Largest_Cities_CSV(1).csv'), delimiter=",")

#initialize the variables
u = 'State - Place'
x = 'Year'
y = 'Population'
z = 'Godghase - Rank'
rows_so_far = 0
c = 0

#initializing the 2 dimentional list
pool = []

pool.append([])

#loop through the csv file and append the list
for row in reader:
	if rows_so_far == 0:
		rows_so_far += 1
		header = row
#populate header
#header for the csv file should include
#state - city, year, population, rank
		for j in range(0,4):
			if j==0:
				pool.append([])
				pool[0].append(u)
			if j==1:
				pool[0].append(x)
			if j==2:
				pool[0].append(y)
			if j==3:
				pool[0].append(z)
	else:
# populate items
# append the population of a city for each year
		for i in range(len(row)-2):
			a = len(pool)
			if not row == []:
				if i==0 or i>=1:
					item = copy.deepcopy(row)
					r = copy.deepcopy(row)
# populate the values for the columns
					for j in range(0, 4):
						if item[i+2] is not '':
							if j==0:
# concatanate the state and city value
								r[0] = item[j+1]+' - '+item[j]
								pool.append([])
								pool[a-1].append(r[0])
# populate year value							
							if j==1:
								pool[a-1].append(int(header[i+2]))
# populate population value
# in case the population is nil, do not append the record in the list
							if j==2:
								if item[i+2] == '':
									pool[a-1].append(int(0))
								else:
									pool[a-1].append(int(item[i+2]))
#initialize the rank to 0, ranks are calculated later in the program
							if j==3:
								pool[a-1].append(int(0))
	rows_so_far += 1

# check the length of the list
a = len(pool)

# populate the list with all values except header as
# sorting cannot be done on integer values when one record has character value
list = pool[1:a-1]

# sort the list by year & population	
list.sort(key=lambda b: (b[1],b[2]), reverse=True)

# add the header to the list
list1 = []
list1.append([])
list1[0] = pool[0]
list1[1:a-1] = list[0:a-2]

#convert the list into csv file
mycsv = csv.writer(open('C:\Users\Apurva\Desktop\Apurva_Godghase.csv', 'wb'))
for row in list1:
# fetching the row index
# no calculation is done at header value
	e = list1.index(row)	
#compare the year value of the current record with the year value of the previous record
#if same calculate the rank, if different assign the rank as one
	if row[1] <> c and e<>0:
		v = 1
		c = row[1]
		row[3] = v
	else:
		if row[1] == c and e <> 0:
			v+=1
			row[3] = v
#write row to csv
	mycsv.writerow(row)