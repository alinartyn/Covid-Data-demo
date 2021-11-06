# Before starting, please run:
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade pandas
# python3 -m pip install --upgrade pandasql

import numpy as np
import pandas as pd
import pandasql as ps
from datetime import datetime

df_covid_data = pd.read_csv('owid-covid-data.csv')

known_locs = ps.sqldf(
	"SELECT location, MAX(people_fully_vaccinated_per_hundred) AS max_full_vac, date"
	+ " FROM df_covid_data GROUP BY location"
	+ " HAVING location != 'World'"
	+ " ORDER BY 2 DESC"
)
known_locs = known_locs.loc[known_locs['location'] == 'Croatia']
known_locs = known_locs.loc[known_locs['location'] == 'Slovakia']
known_locs = known_locs.loc[known_locs['location'] == 'Cuba']
known_locs = known_locs.loc[known_locs['location'] == 'Tuvalu']
known_locs = known_locs.loc[known_locs['location'] == 'Fiji']

# # blacklisted conditions
known_locs = known_locs.loc[known_locs['location'] != 'Gibraltar']
# 22 = give me the values from known_locs with location not = GIL.Only keeps values that are true.
# 22: known_locs data frame will be replaced with filtered version, only keeping rows =
known_locs = known_locs.loc[known_locs['location'] != 'Pitcairn']
known_locs = known_locs.loc[known_locs['max_full_vac'].notnull()]
known_locs = known_locs.loc[known_locs['max_full_vac'] > 1]
known_locs.reset_index(drop=True, inplace=True)

#print([known_locs['location'] != 'Gibraltar'])
# 29: for every row , checks if row is = GILBRATAR

list_location_sets = []
for index, row in known_locs.iterrows():
	if index % 5 == 0:
		this_set = [row['location']]
		list_location_sets.append(this_set)
	else:
		pos_of_last_item = len(list_location_sets) - 1
		list_location_sets[pos_of_last_item].append(row['location'])

df_location_sets = pd.DataFrame(list_location_sets, columns=['Croatia','Slovakia','Cuba','Tuvalu','Fiji'])
df_location_sets.to_csv("df_location_sets.csv")