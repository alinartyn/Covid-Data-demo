# wc -l owid-covid-data.csv

## python3 -m pip install --upgrade pip
## python3 -m pip install --upgrade pandas
## python3 -m pip install --upgrade pandasql

import numpy as np
import pandas as pd
import pandasql as ps
from datetime import datetime
# from library import module

print("[LOG: " + str(datetime.now()) + " - about to load CSV data]")
df_covid_data = pd.read_csv('owid-covid-data.csv')
print("[LOG: " + str(datetime.now()) + " - loaded CSV data!]")

# # Demo 1 - data imported successfully
print("[LOG: " + str(datetime.now()) + " - about to run demo 1]")
print(df_covid_data) # Note - this takes about 15 seconds...
# keep in mind you can make use of pd.set_options like max rows = 200
print("[LOG: " + str(datetime.now()) + " - finished demo 1]")

# Demo 2 - data headings
print(df_covid_data.info())

print("[LOG: " + str(datetime.now()) + " - about to run demo 2]")
df_demo2 = pd.DataFrame(df_covid_data.columns.values.tolist(), columns=['Property'])
df_demo2.to_csv("df_demo2.csv")
print("[LOG: " + str(datetime.now()) + " - finished demo 2]")

# Demo 3 - no. of countries
print("[LOG: " + str(datetime.now()) + " - about to run demo 3]")
df_demo3 = ps.sqldf("SELECT DISTINCT location FROM df_covid_data")
print(df_demo3)
df_demo3.to_csv("df_demo3.csv")
print("[LOG: " + str(datetime.now()) + " - finished demo 3]")

# # # Demo 4 - confirm dates
print("[LOG: " + str(datetime.now()) + " - about to run demo 4]")
df_demo4 = ps.sqldf("SELECT location, MAX(date) as max_date FROM df_covid_data GROUP BY location")
print(df_demo4)
df_demo4.to_csv("df_demo4.csv")
print("[LOG: " + str(datetime.now()) + " - finished demo 4]")  

# # Demo 5 - confirm vacc
print("[LOG: " + str(datetime.now()) + " - about to run demo 5]")
df_demo5 = ps.sqldf(
	"SELECT location, MAX(people_fully_vaccinated_per_hundred) AS max_full_vac, date"
	+ " FROM df_covid_data GROUP BY location"
	+ " HAVING location != 'World'"
	+ " ORDER BY 2 DESC"
)
print(df_demo5)
df_demo5.to_csv("df_demo5.csv")
print("[LOG: " + str(datetime.now()) + " - finished demo 5]")

# # # Demo 6 - REQUIRES DEMO 5 TO HAVE BEEN RUN - create pairings
print("[LOG: " + str(datetime.now()) + " - about to run demo 6]")
df_demo5 = pd.read_csv("df_demo5.csv")
blacklist = ['Gibraltar', 'Pitcairn'] # blacklisted due to questionable data accuracy
list_location_pairs = []
for index, row in df_demo5.iterrows():
	if row['location'] in blacklist:
		print("Ignored due to blacklist: " + row['location'])
	elif pd.isnull(row['max_full_vac']):
		print("Ignored due to null value for max_full_vac: " + row['location'])
	elif row['max_full_vac'] < 1:
		print("Ignored due to max_full_vac < 1: " + row['location'])
	else:
		if index % 2 == 0:
			this_dictionary = {"location1": "", "location2": ""}
			this_dictionary["location1"] = row['location']
			list_location_pairs.append(this_dictionary)
		else:
			pos_of_last_item = len(list_location_pairs) - 1
			list_location_pairs[pos_of_last_item]["location2"] = row['location']

df_demo6 = pd.DataFrame(list_location_pairs)
print(df_demo6)
df_demo6.to_csv("df_demo6.csv")
print("[LOG: " + str(datetime.now()) + " - finished demo 6]")