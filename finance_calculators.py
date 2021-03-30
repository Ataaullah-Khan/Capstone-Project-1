# Program to calculate investments and home loan repayments

import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print()

print("investment        - to calculate the amount of interest you'll earn on interest ")
print("bond              - to calculate the amount you'll have to pay on a home loan \n")

user_choice = input("")
user_choice = user_choice.lower()                                                               # Converted to lowercase to check the condition in the if statement


if user_choice == "bond" or user_choice == "investment":                                         # Determines if the user's input was valid or not
    print()
    print(f"You chose {user_choice}. ")
    print()
else:
    print()
    print("Your input was invalid")
    print()


#   The if statement below calculates and displays interest based on the user's choice of simple or compound interest
#   Formula for simple interest:        A = P*(1+r*t)
#   Formula for compound interest:      A = P* math.pow((1+r),t)

#   round(formula,2) is used to show the total amount to two decimal places since we are dealing with money

#   A = total amount   p = money deposited   r = annual interest rate   t = number of years


if user_choice == "investment":                                                                 #Nested If statement used to choose between investment and bond repayment calculator

    P = float(input("How much money will you deposit in rands? Enter numbers only "))     
    interest_rate = float(input("Please enter the interest rate. Enter numbers only "))
    r = interest_rate/100
    t = int(input("For how many years would you like to invest? Enter whole numbers only ")) 

    interest = input("would you like simple or compound interest? (simple/compound) ")
    print()


    if interest == "simple":                                                                    # Simple interest
        A = round(P * (1 + r * t),2)
        print()
        print(f"Total accrued from a R{P} deposit at {interest_rate}% {interest.lower()} interest over {t} year/s = R{A}")

    else:                                                                                       # Compound interest
        A = round(P * math.pow((1 + r),t),2)
        print()
        print(f"Total accrued from a R{P} deposit at {interest_rate}% {interest.lower()} interest over {t} year/s = R{A}")
    
    
else:

#   Calculates and displays monthly bond repayment based on the user's input
#   Bond Repayment Formula:     x = (i*P)/(1 - (1+i)^(-n))

#   x = monthly repayment   P = house value   i = monthly interest rate   n = months to repay


    P = float(input("What is the value of the house? Enter numbers only "))
    interest_rate = float(input("Please enter the interest rate. Enter numbers only "))
    i = (interest_rate/100/12)
    n = int(input("Over how many months will you repay? Enter whole numbers only "))

    x = round((i*P) /( 1 - (1+i)**(-n)),2)
    print(f"Your monthly repayment is: R{x}")
    

    


    
    

    


