import math
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



