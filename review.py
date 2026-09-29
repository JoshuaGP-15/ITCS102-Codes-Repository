owner_age = int(input("What is your age?"))
monthly_revenue = float(input("What is your revenue?"))
credit_score = int(input("What is your credit score?"))
years_in_business = float(input("How long have you been operating?"))
has_defaults = bool(input("Have you been bankruped before?"))
collateral_name = input("What is your collateral?")
collateral_value = float(input("What is the value of collateral?"))


base_rate = 0
maximum_loan = 0 
#outer Baseline Requirements

if owner_age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("Passed")
    if credit_score >= 720: #tier 1
        print("Your credit score is very High")
        if
    elif credit_score <= 620 and > 720 :
            print("Credit score is in range")
            maximum_loan = monthly_revenue * 1.5
            print("maximum loan is" maximum_loan)
    else :
         print("Invalid")
else:
    
    print("Failed baseline criteria")
