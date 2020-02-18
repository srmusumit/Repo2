# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 01:06:33 2020

@author: Sumit
"""
#
var_1 = 19
var_2 =20
print('Checking equility of', var_1 == var_2)
print('Checking not equal to', var_1 != var_2)
print('Checking greater then and equal to', var_1 >= var_2)
print('CHecking smaller and equal to', var_1 <= var_2)

num1 = 12
num2 = 45
print ('Both numbers are less then 50?', num1 <= 50 and num2 <50)
print ('Both number are greater then 10', num1 >=10 and num2 >=10)
print ('EIther of the nuber is greater then 30? ', num1>=30 or num2 >=30)


name = input('Please enter your name,?')
print ('Hey', name.upper())
age = int(input('Please enter your age:'))
if age <18:
    print('You need to be someone who is older then 18 years to come into the party')
elif age > 18 and age <=35:
    print ('Hey', name.upper(), 'Welcome to the party, enjoy your free time..')
elif age > 35 and age <= 50:
    print('Hello', name , 'You can come to the party but you may not find an older people like you')
else:
    print(name,'Sorry, you are not allowed to the party, Hope you understand')

my_string = 'Python'
print (my_string[1:4])
print (my_string.upper())

