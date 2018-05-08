#calculate an individual's tax and after-tax income

#use def to change the amount of income for different results
def tax(income):

#Identify and calculate tax and after-tax in 5 situations,
#and print the outcome in each situation
    if 0 <= income <= 18200:
        tax = 0
        final_income = income -tax
        print('Tax liability:', tax)
        print('Afer-tax income:', final_income)
        
    elif 18200 < income <= 37000:
        tax = 0.19*(income - 18200)
        final_income = income - tax
        print('Tax liability:', tax)
        print('Afer-tax income:', final_income)
        
    elif 37000 < income <= 87000:
        tax = 3572 + 0.325*(income - 37000)
        final_income = income - tax
        print('Tax liability:', tax)
        print('Afer-tax income:', final_income)

    elif 87000 < income <= 180000:
        tax = 19822 + 0.37*(income - 87000)
        final_income = income - tax
        print('Tax liability:', tax)
        print('Afer-tax income:', final_income)

    else:
        tax = 54532 + 0.45*(income -180000)
        final_income = income - tax
        print('Tax liability:', tax)
        print('Afer-tax income:', final_income)
    
    
