#loan_principal = 'Loan principal: 1000'
#final_output = 'The loan has been repaid!'
#first_month = 'Month 1: repaid 250'
#second_month = 'Month 2: repaid 250'
#third_month = 'Month 3: repaid 500'


#print(loan_principal)
#print(first_month)
#print(second_month)
#print(third_month)
#print(final_output)

import math
#m = 0 # кол-во платежей в месяцах
#p = 0 # ежемесячный платеж
#loan_principal = int(input('Enter the loan principal:'))
#calculate_param = input("What do you want to calculate?")
#if calculate_param == 'm':
#    payment = int(input("Enter the monthly payment:"))
#    m = math.ceil(loan_principal/payment)
#    if m == 1:
#        print('It will take 1 month to repay the loan')
#    else:
#        print('It will take', int(m), 'months to repay the loan')
#elif calculate_param == 'p':
#    m = int(input("Enter the number of months:"))
#    payment = math.ceil(loan_principal/m)
#    last_payment = loan_principal - (m-1) * payment
#    if payment == last_payment:
#        print("Your monthly payment =", payment)
#    else:
#        print("Your monthly payment =", payment, "and the last payment =", last_payment, end='.')
# аннуитетный платеж
#calculate_param = input("What do you want to calculate?")
#if calculate_param == 'n':
#    loan_principal = int(input('Enter the loan principal:'))
#    month_payment = int(input("Enter the monthly payment:"))
#    loan_interest = int(input('Enter the loan interest:'))
#    nominal_percent = loan_interest/(12*100)
#    n = math.ceil(math.log(month_payment/(month_payment - nominal_percent * loan_principal), 1 + nominal_percent))
#    if n > 12:
#        print("It will take", n//12, "years and", n%12, "months to repay this loan!")
#    elif n == 12:
#        print("It will take 1 year to repay this loan!")
#    else:
#        print("It will take", n, "months to repay this loan!")
#elif calculate_param == 'a': #расчет ежемесячного платежа
#    loan_principal = int(input('Enter the loan principal:'))
#    n = int(input("Enter the number of periods:")) # number periods
#    loan_interest = float(input('Enter the loan interest:'))
#    nominal_percent = loan_interest / (12 * 100)
#    a = math.ceil(loan_principal * nominal_percent*(1+nominal_percent)**n/((1+nominal_percent)**n - 1))
#    print("Your monthly payment =", a, end='!')
#elif calculate_param == 'p': # расчет основной суммы кредита
#    annuity_payment = input("Enter the annuity payment:")
#    n = int(input("Enter the number of periods:"))
#    loan_interest = input('Enter the loan interest:')
#    nominal_percent = float(loan_interest) / (12 * 100)
#    p = float(annuity_payment)/(nominal_percent * (1+nominal_percent)**n/((1+nominal_percent)**n - 1))
#    print("Your loan principal =", int(p), end='!')

import argparse

parser = argparse.ArgumentParser("This program calculates credit parameters for annuity and differentiated payment")

parser.add_argument('-t', "--type", choices=["diff", "annuity"], help="You need to choose one type of loan")
parser.add_argument('-pr', "--principal", type=int, help="Enter the principal amount of the loan")
parser.add_argument('-i', "--interest", type=float, help="Enter the interest rate")
parser.add_argument('-p', "--periods", type=int)
parser.add_argument('-pay', "--payment", type=int)
args = parser.parse_args()

if args.type == 'diff' and args.principal > 0 and args.interest > 0 and args.periods > 0:
    nominal_percent = args.interest/(12*100)
    all_payment = 0
    for i in range(1, args.periods + 1):
        payment = math.ceil(args.principal/args.periods + nominal_percent*(args.principal
                                                                          - (args.principal*(i-1))/args.periods))
        all_payment +=payment
        print("Month", i, end=':')
        print(" payment is", payment)
    print("Overpayment =", all_payment - args.principal)

elif (args.type == 'annuity') and (args.principal != None) and (args.interest != None) and (args.periods != None):
    nominal_percent = args.interest / (12 * 100)
    payment = math.ceil(args.principal * nominal_percent*(1+nominal_percent)**args.periods/((1+nominal_percent)**args.periods-1))
    all_payment = payment * args.periods
    print("Your annuity payment =", payment, end='! ')
    print("Overpayment =", all_payment - args.principal)

elif args.type == 'annuity' and (args.payment != None) and (args.interest != None) and (args.periods != None):
    nominal_percent = args.interest / (12 * 100)
    all_payment = args.payment * args.periods
    principal = args.payment/(nominal_percent*(1+nominal_percent)**args.periods/((1+nominal_percent)**args.periods -1))
    print("Your loan principal =", int(principal), end='! ')
    print("Overpayment =", all_payment - int(principal))
elif args.type == 'annuity' and (args.payment != None) and (args.interest != None) and (args.principal != None):
    nominal_percent = args.interest / (12 * 100)
    periods = math.ceil(math.log(args.payment/(args.payment - nominal_percent * args.principal), 1 + nominal_percent))
    if periods > 12 and periods%12 != 0:
        print("It will take", periods//12, "years and", periods%12, "months to repay this loan!")
    elif periods % 12 == 0:
        print("It will take", periods//12, "year to repay this loan!")
    else:
        print("It will take", periods, "months to repay this loan!")
    print("Overpayment =", args.payment*periods - args.principal)
else:
    print("Incorrect parameters")



