# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 15:04:44 2025

@author: rafael
"""

##
#This program takes in 2 integers from the user, the first between 0 and 20 and the 
#second one between 30 and 100, the program then determines which numbers in between are even using a for loop
#Then a count, sum, and average are output of the even numbers between the two integers from the user

#We are explaining the program and taking in the inputs to compute
print("This program will take in two numbers, a lower-limit and an upper-limit")
print("Then it will tell you which numbers are even in between, then tell you the sum, average and count of the even numbers")
lower_limit = int(input("Please enter a number between 0 and 20: "))
upper_limit = int(input("Please enter a number between 30 and 100: "))

#setting up variables equal to 0 or empty so we can use later
count = 0
even_sum = 0
even_list = []

#The for loop uses the lower and upper limit for the range to look through
#the if statement makes sure we only work with even numbers using the modulo arithmetic 
for i in range(lower_limit + 1, upper_limit):
    if i % 2 == 0:
        count = count + 1
        even_sum =  even_sum + i
        even_list.append(i)

#Again i used a list to place out the numbers for neatness, I could have just printed
#each number but it elongates the console output
#Solution to get the average outside of the for loop
average = even_sum / count

#outputs the expected results from what the program should be doing
print("These are the even numbers in between:", even_list)
print("The count is:", count)
print("The sum of the even numbers are:", even_sum)
print("The average of the even numbers is: ", average)