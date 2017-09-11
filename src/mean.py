#! /usr/bin/env python3

# Open data file
infile = open("../data/data1.txt", "r")  # ".." means "go up one directory"

# Initialise values
mean = 0
n = 0

# Loop to perform sum
for number in infile:
    number = float(number) # this is because the numbers are strings
    mean = mean + number
    n += 1 # n = n + 1 (this is an inplace assignment operator)

# It is good practice to close a file when you are finished.
infile.close()

# Calculate the mean.
mean = mean/n
print(mean)
