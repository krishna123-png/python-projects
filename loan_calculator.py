import math
import argparse


def payment(p, n, i):
    payment = int(math.ceil(p * (i/1200) * pow(1 + i/1200, n) / (pow(1 + i/1200, n) - 1)))
    print(f"Your annuity payment = {payment}!")
    print(f'Overpayment = {payment * n - p}')


def principal(a, n, i):
    principal = a / ((i/1200 * pow((i/1200 + 1), n)) / (pow((i/1200 + 1), n) - 1))
    print(f"Your loan principal = {principal}!")
    print(f'Overpayment = {a * n - principal}')

def periods(p, a, i):
    periods = int(math.ceil(math.log(a / (a - (i/1200) * p), (i/1200) + 1)))
    years = periods // 12
    months = periods % 12

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")
    print(f'Overpayment = {a * periods - p}')
    
def differentiate(p, n, i):
    total_payment = 0
    for j in range(1, n + 1):
        monthly_payment = math.ceil((p/n) + ((i / 1200 / n) * (p * n - p * j + p)))
        print(f'Month {j}: payment is {monthly_payment}')
        total_payment += monthly_payment
    print(f'Overpayment = {math.ceil(total_payment - p)}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payment")
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    parser.add_argument("--type")
    
    args = parser.parse_args()

    if args.type != "annuity" and args.type != "diff":
        print("Incorrect parameters")
    elif args.type == "diff" and args.payment:
        print("Incorrect parameters")
    elif args.interest is None:
        print("Incorrect parameters")
    elif len(vars(args)) < 4:
        print("Incorrect parameters")
    elif args.principal and float(args.principal) < 0:
        print("Incorrect parameters")
    elif args.payment and float(args.payment) < 0:
        print("Incorrect parameters")
    elif args.periods and float(args.periods) < 0:
        print("Incorrect parameters")
    elif args.interest and float(args.interest) < 0:
        print("Incorrect parameters")
    elif args.type == "diff":
        differentiate(float(args.principal), int(args.periods), float(args.interest))
    elif args.type == "annuity":
        if args.payment is None:
            payment(float(args.principal), int(args.periods), float(args.interest))
        elif args.periods is None:
            periods(float(args.principal), float(args.payment), float(args.interest))
        elif args.principal is None:
            principal(float(args.payment), int(args.periods), float(args.interest))
        else: print("Wrong input.")
    else:
        print("Incorrect parameters")


if __name__ == "__main__":
    main()
