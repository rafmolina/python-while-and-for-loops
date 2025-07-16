# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 20:57:00 2025

@author: rafael
"""
##
#This program generates 100 random numbers between 0-8
#It will output the numbers to the user

#I am importing the module or library random for use in the program
import random 
#creating an input so the user may decide to run the random gen
print("Hello! This is a random number generator")
run_it = input('Type "Yes" to generate 100 random numbers between 0-8: ')
#Creating a for loop with the range of 101 so it prints 100 times
for i in range(101):
    if run_it == "Yes":
        random_num = random.randint(0, 8)
        print(random_num)
    elif run_it != "Yes":
        print("You need to type 'Yes'")
        break
#In this program I had to look up the random library to use it properly, putting in the range of 0-8
#As well as using the break method or else it was printing out my elif 100 times 
    