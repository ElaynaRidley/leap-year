'''
Program: leapyear.py
Author: Elayna Ridley
Course: CSC 111L, Lab 4
Purpose: To print out whether or not the year is a leap year given an input of a year.
'''
year = int(input('Enter the year: '))

if year % 4 != 0:
    print('The year', year, 'is not a leap year')
elif year % 4 == 0 and year % 100 != 0:
    print('The year', year, 'is a leap year')
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print('The year', year, 'is not a leap year')
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print('The year', year, 'is a leap year')
           
