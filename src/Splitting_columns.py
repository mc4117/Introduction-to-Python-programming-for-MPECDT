#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# open python file
import numpy as np
import pylab

infile = open("../data/xy.dat", "r")  

# Initialise values
x = []
y = []

# Loop to perform sum
for number in infile:
    a = (number.split("       "))
    # xy = map(float, line.split())
    x.append(float(a[0]))
    y.append(float(a[1]))

x_array = np.array(x)
y_array = np.array(y)

pylab.plot(x_array,y_array)

print(np.min(y))
print(np.max(y))