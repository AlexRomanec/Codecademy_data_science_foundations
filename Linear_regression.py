# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:53:10 2024

@author: alexr

Project to build a linear regression function to minimize error on best fit line
"""

import matplotlib.pyplot as plt

#%% Defining line function

def get_y(m,b,x):
    y = m*x + b
    return y

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)

#%% Error calculation function

def calculate_error(m,b,point):
    x_point = point[0]
    y_point = point[1]
    y_predicted = get_y(m,b,x_point)
    
    y_diff = abs(y_point - y_predicted)
    return y_diff

# Checking the function
# print(calculate_error(1, 0, (3, 3)))
# print(calculate_error(1, 0, (3, 4)))
# print(calculate_error(1, -1, (3, 3)))
# print(calculate_error(-1, 1, (3, 3)))

#%% Datapoints to use

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
x_data = [point[0] for point in datapoints]
y_data = [point[1] for point in datapoints]

plt.plot(x_data, y_data)
plt.xlabel('Width of ball / cm')
plt.ylabel('Height of bounce / cm')

#%% Calculate total error function

def calculate_all_error(m,b,points):
    total_y_error = 0
    for point in points:
        error = calculate_error(m,b,point)
        total_y_error += error
    return total_y_error

# Checking the function
# datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
# print(calculate_all_error(1, 0, datapoints))
# print(calculate_all_error(1, 1, datapoints))
# print(calculate_all_error(1, -1, datapoints))
# print(calculate_all_error(-1, 1, datapoints))

#%% Possible m and b values

possible_ms = [x/10 for x in range(-100,101,1)]
# print(possible_ms)
possible_bs = [x/10 for x in range(-200,201,1)]

#%% Finding smallest error 

smallest_error = float("inf") # Initialise at infinity so anything is smaller
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

print(best_b)
print(best_m)
print(smallest_error)


#%% Plotting result

best_fit_ys = [best_m*x+best_b for x in x_data]

plt.plot(x_data, y_data)
plt.plot(x_data, best_fit_ys)
plt.xlabel('Width of ball / cm')
plt.ylabel('Height of bounce / cm')
