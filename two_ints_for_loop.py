# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 10:39:08 2025

@author: rafael
"""
##
#This program is to get two numbers from the user
#The first number is between -100 and -10 the second number between 10 - 100
#The program outputs the sum of all numbers in between and the median
#As well with a count for how many numbers there are

#This is the introduction that introduces the program to the user
print("Hello! You will be prompted to enter two numbers, please read instructions when doing so")
print("You will receive the sum, the mean, and a count for the numbers between")

#We get the two numbers from the user and hold them in variables
num1 = int(input("Please enter the first number between -100 and -10:"))
num2 = int(input("Please enter the second number between 10 and 100:"))

#creating a variable that contains 0 to add the sum and a counter 
sum_of_numbers = 0
count = 0

#For loop with a range of the two inputs. Num1 has one added to it so we can skip it in our program 
for i in range(num1 +1 , num2):
    sum_of_numbers = sum_of_numbers + i
    count = count + 1
    #An equation to get the average of the numbers inside the for loop because of indentation
    average = sum_of_numbers / count

#Prints the results to the user
print("The sum of your numbers in between are:", sum_of_numbers)
print("The count of the numbers between are:" , count)
print("The average of the numbers in between are:", average)