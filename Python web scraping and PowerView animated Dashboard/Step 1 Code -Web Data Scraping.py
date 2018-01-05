import sys
reload(sys)
sys.setdefaultencoding('utf8')

import csv
import requests
from bs4 import BeautifulSoup

#Fetching data from the website
url = 'http://worldpopulationreview.com/us-cities/1790-1990'
response= requests.get(url)
html=response.content

#Retrieving data from the html 
soup = BeautifulSoup((html), "lxml")
table = soup.find('table',attrs={'class': 'tablehead'})


list_of_rows=[]
for row	in table.findAll('tr')[0:]:
	list_of_cells=[]
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;', '')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)

#Writing output to the output file	
outfile= open("./Largest_Cities_CSV","wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)

