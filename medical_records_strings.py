# -*- coding: utf-8 -*-
"""
Python Exercise to clean and analyse a given set of medical record data, practicing string manipulation techniques
@author: alexr
"""

#%% Medical record data

medical_data = \
"""Marina Allison   ,27   ,   31.1 , #7010.0   ;Markus Valdez   ,   30, 22.4,   #4050.0 ;Connie Ballard ,43 ,   25.3 , #12060.0 ;Darnell Weber   ,   35   , 20.6   , #7500.0;Sylvie Charles   ,22, 22.1 ,#3022.0   ;   Vinay Padilla,24,   26.9 ,#4620.0 ;Meredith Santiago, 51   , 29.3 ,#16330.0;   Andre Mccarty, 19,22.7 , #2900.0 ; Lorena Hodson ,65, 33.1 , #19370.0; Isaac Vu ,34, 24.8,   #7045.0"""


#%% Cleaning medical record data

# print(medical_data)
updated_medical_data = medical_data.replace("#", "$")
# print(updated_medical_data)

#%% Calculate number of medical records

num_records = 0
for i in updated_medical_data:
  if i == '$':
    num_records += 1
print('There are {} sets of medical records in the data'.format(num_records))

#%% Splitting the records into seperate lists

medical_data_split = updated_medical_data.split(";")
# print(medical_data_split)

medical_records = []
for record in medical_data_split:
  medical_records.append(record.split(','))
# print(medical_records)

#%% Cleaning data of whitespace etc

medical_records_clean =[]

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

print(medical_records_clean)

#%% Data analysis 

#Printing names of individuals
for record in medical_records_clean:
    print(record[0].upper())

# Create lists of all items seperately
names = [record[0].upper() for record in medical_records_clean]
ages = [record[1] for record in medical_records_clean]
bmis = [record[2] for record in medical_records_clean]
insurance_costs = [record[3] for record in medical_records_clean]

# print(names)
# print(ages)
# print(bmis)
# print(insurance_costs)

# Calculate average bmi
total_bmi = 0
for value in bmis:
    value = float(value)
    total_bmi += value
avg_bmi = total_bmi/len(bmis)
print('Average BMI: {:.2f}'.format(avg_bmi))

# Total overall insurance cost
total_cost = 0
for value in insurance_costs:
    value = float(value[1:])
    total_cost += value
print('The total cost of insurance for this group is ${:.2f}'.format(total_cost))
