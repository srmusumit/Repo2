# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 04:09:50 2020

@author: Sumit
"""
salary = int(input('Please enter your salary:'))
hr = int(input('Please enter the house rent:'))
personal = float(input("Please enter the personal expenses:"))
loan = float(input('Please enter the loan amount:'))
credit = float(input('Enter the amount you need to repay in credit card'))
petrol = float(input("Please ente the petrol amount:"))
misc = float(input("Please enter the misclenious expenditure:"))
mf = float(input("Please enter the amount you would like to invest in MF: "))
ppf = float(input("Please enter the amount you would like to invest in ppf:"))
travel= float(input("Please enter the amount for traveling purpose:"))
interest = float(input("Please enter the interest amount if any? "))
total = (hr + loan + credit + petrol + personal + misc + mf + ppf + travel + interest)
investment = (mf + ppf)
personal_expen = (hr + personal + credit + petrol + misc + travel + interest)
print ('\nYour toal investment in this month is: ', investment, 'Rupees')
print ('Your total expenditure in this month is: ', total , 'Rupees')
print ('Your total personal expenditure in this month is: ', personal_expen, 'Rupees')
saving = salary - total
print ('Total savings in this month is: ', saving)
if salary > total:
    print ('You are in surplus, you toal saving percentage is: ', (saving * 100)/ salary, '%')
    print ('Your total investment in this month is: ', (investment * 100)/ salary, '%')
    print ('Your total expenditure on your daily needs is:  ', (personal_expen * 100)/ salary, '%')
else:
    print('You are in deficit and your toal deficit is: ', total - salary)
    print ('Your total investment in this month is: ', (investment * 100)/ salary, '%')
    print ('Your total expenditure on your daily needs is:  ', (personal_expen * 100)/ salary, '%')
    