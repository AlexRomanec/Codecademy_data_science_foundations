# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:16:55 2024
Python Exercise to manipulate fictional medical records data using dictionarys
@author: alexr
"""

#%% Task 1 - Initialise dictionary

medical_costs = {}

#%% Task 2, 3 & 4- Populating Dictionary

medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0

medical_costs.update({'Connie': 8886.0, 'Isaac':16444.0, 'Valentina': 6420.0})
print(medical_costs)

#%% Task 5 - Update Vinay's cost

medical_costs['Vinay'] = 3325.0
print(medical_costs)

#%% Task 6 & 7 - Calculate average cost

total_cost = 0
for cost in medical_costs.values():
    total_cost += cost
avg_cost = total_cost/len(medical_costs)
print('Average Insurance Cost: {}'.format(avg_cost))

#%% Alternative Average Calculation

import numpy as np
print('Average Cost: {}'.format(np.average([cost for cost in medical_costs.values()])))

#%% Tasks 8-11 - Mapping Patient Names to Ages

names = ['Marina', 'Vina', 'Connie', 'Isaac', 'Valentina']
ages = [27,24,43,35,52]

zipped_ages = zip(names, ages)

names_to_ages = {name:age for name, age in zipped_ages}
print(names_to_ages)

marina_age = names_to_ages.get('Marina')
print(marina_age)

#%% Tasks 12-18 - Medical Database Dictionary

medical_records = {}

medical_records.update({'Marina': {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Cost': 6607.0},
                        'Isaac': {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Cost': 16444.0}, 
                        'Vinay': {'Age': 24, 'Sex': 'Male', 'BMI': 26.9, 'Cost': 3225.0}, 
                        'Connie': {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Cost': 8886.0}})

print(medical_records)

print("Connie's insurance cost is {} dollars".format(medical_records['Connie']['Cost']))

#Delete Vinay's Record
medical_records.pop('Vinay')
print(medical_records)

#%%
for name, record in medical_records.items():
    print("{} is a {} year old with a BMI of {} and insurance cost of {}".format(name,record['Age'],record['BMI'],record['Cost']))
