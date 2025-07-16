# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 20:38:18 2025

@author: rafael
"""

##
#This program is about taking in an input from the user
#The input is then inpsected to see if it is a string, int, or white-space
#If it's a string the output will be the string in upper and lower case
#If the input is an Int we output the square root of the number
#If is an empty space then the program tells you that you entered a space
#Lastly, if its anything else, it returns a print statement 

#input from the user, being kinda specific, not sure if its supposed to be just a letter or a word
print("Hello, this program will take a letter, word, number, or anything you want to try")
print("It will output something depending on which you choose!")
user_input = input("Enter a string:")

#building a for loop to parse through the string
for i in user_input:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        print("Uppercase:", i.upper(), "lowercase:", i.lower())
    elif "0" <= i <= "9":
        num = int(i)
        sqared = num ** 2
        print("Squared Value:",sqared)
    elif i == " ":
        print(i, "is a SPACE")
    else:
        print(i, "is special- just like you!!!")
        
#The for loop uses boolean expression by using i to move through the index and 
#compare, depending on what comparison, the appropriate if statement is executed