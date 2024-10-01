# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:51:09 2024

@author: alexr
"""
#%% Hurricane Data

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#%% Task 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
# print(len(damages))
# test = float(damages[3][:-1])*conversion[damages[3][-1]]
# print(test)

def converter(damages):
  updated_damages = []
  for i in range(len(damages)):
    if damages[i] == 'Damages not recorded':
      updated_damages += ['Damages not recorded']
    else:
      converted = float(damages[i][:-1])*conversion[damages[i][-1]]
      updated_damages += [converted]
  return updated_damages

# test function by updating damages
updated_damages = converter(damages)
# print(updated_damages)


#%% Task 2 
# Create a Table
hurricane_dict = {}
for i in range(34):
  hurricane_dict[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}
# Create and view the hurricanes dictionary
# print(hurricane_dict)


#%% Task 3
# Organizing by Year
# def sort_by_year()
#   for hurricane in hurricane_dict:

# create a new dictionary of hurricanes with year and key

#%% Task 4
# Counting Damaged Areas
def area_count(hurricane_dict):
  area_count_dict = {}
  for hurricane in hurricane_dict:
    for area in hurricane_dict[hurricane]['Areas Affected']:
      if area in area_count_dict:
        area_count_dict[area] += 1
      else:
        area_count_dict[area] = 1
  return area_count_dict
# create dictionary of areas to store the number of hurricanes involved in
area_count_dict = area_count(hurricane_dict)
print(area_count_dict)


#%% Task 5 
# Calculating Maximum Hurricane Count
def max_canes(area_count_dict):
  max_count = 0
  for area in area_count_dict:
    area_count = area_count_dict[area]
    if area_count > max_count:
      max_count = area_count
      max_area = area
  print('Area with the most hurricanes is {} with {}'.format(max_area,max_count))
# find most frequently affected area and the number of hurricanes involved in
max_canes(area_count_dict)

#%% Task 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

#%% Task 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key


#%% Task 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


#%% Task 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
