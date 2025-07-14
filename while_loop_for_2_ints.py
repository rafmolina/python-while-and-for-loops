# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 12:31:19 2025

@author: rafael
"""

##
#This program will take in three inputs from the user that are integers
#The first number will be a start, the second will be the stop, and the last will be the step
#Using a while loop you will print the numbers from start to stop with the step value increments
#Then also print out the counter, sum, and average of the numbers

#Welcome prompt for the user using the program
print("Hey there, welcome to the program about incremented numbers")
print("You will enter three numbers, please read the instructiosn carefully for each prompt")
print("At the end you will be given the list of numbers with the average, sum, and count")

#Taking the three inputs from the user, lower-limit for start and upper_limit for end, third variable is increasement
lower_limit = int(input("Please enter a number between 10 and 35, this will be your start number:"))
upper_limit = int(input("Please enter a number between 60 and 100, this will be your stopping number:"))
increment_value = int(input("Please enter a number between 3 and 7, this number is how we will increment between the first two numbers:"))

#iniate some variables to modify within the while loop
#we start the count at 0 and the total sum, we also create a blank list to contain the numbers between 
count = 0
sum_of_numbers = lower_limit
total_sum = 0
list_of_numbers = []

#while loop's condition is 'while the lower number is lesser or equal to the upper number do this:
#We are updating the sum by the increment and if it stays True it counts, sums again, and places the number in the list

while sum_of_numbers <= upper_limit:
    sum_of_numbers = sum_of_numbers + increment_value
    count = count + 1
    total_sum = total_sum + sum_of_numbers
    list_of_numbers.append(sum_of_numbers)
    #print(list_of_numbers)
 
#arithmetic for the average outside of the while loop, doesn't need to be inside the while loop
average = sum_of_numbers / count

#output expected for the program
#I could not output the numbers neatly without using a list, another method is appreciated if known or taught later but 
#lists were in the 5s module so I believe its safe to use
print("These are the numbers:",list_of_numbers)
print("Count:",count)
print("Average:",average)
print("Sum:",total_sum)
        