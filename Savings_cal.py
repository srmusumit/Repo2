name = input ('Please enter your name: ')
salary = float(input('Please enter your salary: '))
print ('Hello', name,'As per the input your salary is: ', salary)
rent = float(input('please enter the rent amount: '))
loan = float(input('Enter the amount you need to repay as loan: '))
personal = float(input('Enter the personal expenses: '))
petrol = float(input('Enter the amount needed for petrol: '))
misc = float(input('Enter the misclenious expenses:'))
home = float(input('Amount needed to send home if any: '))
travel = float(input('Amount needed for traveling ticket if any?'))
ppf = float(input('Amount investing in PPF:'))
mutual  = float(input('Amount investing in mutual fund: '))
total = rent + loan + personal + petrol + home + travel + ppf + mutual
daily = rent + personal + petrol + misc
investment = ppf + mutual
saving = salary - total
deficit = total - salary
print (name,', your total expenditure in this months is: ', total, '₹')
if salary > total:
    print ('your have a surplus of', saving, '₹')
    print ('In terms of % your total saving percent is: ', (saving * 100)/ salary, '%.2f')
    print ('your total expenditure on your daily needs is: ', daily, '₹, in terms of percentage: ', (daily * 100)/salary, '%')
    print ('your investment in this month is:', investment, '₹, in terms of percentage it is: ', (investment * 100)/salary, '%')
    print ('Total loan repayment is: ', loan , '₹, in terms of percentage it is: ', (loan * 100)/salary, '%')
else:
    print ('you are in deficit and amount need to meet your require ment is: ', total - salary)
    print ('In terms of % your total deficit percent is: ', (deficit * 100)// salary, '%.2f')
    print ('your total expenditure on your daily needs is: ', daily, '₹, in terms of percentage: ', (daily * 100)/salary, '%')
    print ('your investment in this month is:', investment, '₹, in terms of percentage it is: ', (investment * 100)/salary, '%')
    print ('Total loan repayment is: ', loan , '₹, in terms of percentage it is: ', (loan * 100)/salary, '%.2f')
    print ('=======================================Cut your expenses to remove the deficit==========================================================')
