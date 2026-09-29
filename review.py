owner_age = int(input("What is your age?"))
monthly_revenue = float(input("What is your revenue?"))
credit_score = int(input("What is your credit score?"))
years_in_business = float(input("How long have you been operating?"))

has_defaults_input = input("Have you been bankruped before?")
if has_defaults_input == "no":
    has_defaults = False
else:
    has_defaults = True

collateral_name = input("What is your collateral?")
collateral_value = float(input("What is the value of collateral?"))

base_rate = 0 
maximum_loan = 0

if owner_age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print('You passed the baseline criteria')  
    
    if credit_score >= 720:  # tier 1
        maximum_loan = monthly_revenue * 3
        print('Credit score is High')
        print('maximum loan is', maximum_loan)
       
        if monthly_revenue >= 50000:
            base_rate = 0.015
            print('High revenue base rate is', base_rate)
        else:
            base_rate = 0.025
            print('Base rate is', base_rate)
            
        if collateral_value >= maximum_loan:
            print('Accepted collateraval value is higher than max loan')
            base_fee = maximum_loan * base_rate
            if int(collateral_value) % 5000 != 0:
                final_fee = base_fee + 250.00
                print('a fee is added')
            else:
                final_fee = base_fee
            print('Final Processing Fee is:', final_fee)
        else:
            print('Rejected insufficient collat value')
            
    elif credit_score >= 620 and credit_score < 720: # tier 2
        maximum_loan = monthly_revenue * 1.5
        print('Maximum loan ', maximum_loan)
        
        if years_in_business >= 5.0:
            base_rate = 0.02 
            print('Base rate is', base_rate)
        else:
            base_rate = 0.035  
            print('Base rate is 3.5')
            
        if collateral_value >= maximum_loan:
            print('Accepted collateraval value is higher than max loan')
            base_fee = maximum_loan * base_rate
            if collateral_value % 5000 != 0:
                final_rate = base_rate + 250.00
                print('a fee is added')
            else:
                final_rate = base_rate
            print('Final raete is:', final_rate)
        else:
            print('Rejected insufficient collat value')
            
    elif credit_score < 620: # tier 3 
        print('Credit score was too low')
       
        
else:
    print('You have Failed the criteria')
