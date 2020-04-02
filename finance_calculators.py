#The following program allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator
import math

financial_cal = input("Choose either 'investment' or 'bond' to proceed:  \n \n investment \t - to calculate the amount of interest you'll earn on interest. \n bond   \t - to calculate the amount you'll have to pay on a home loan. \n ")

if (financial_cal == "INVESTMENT") or (financial_cal == "Investment") or (financial_cal == "investment"):
    deposit_money = float(input("Enter the amount of money you're depositing: "))
    inte_rate1 = float(input("Enter the interest rate: "))  #Input the interest rate using only numbers (don't put the % symbol)
    num_years = float(input("Enter the number of years you plan on investing for: "))
    interest = input("Would you like simple or compound interest?: ")  #Answer this question using the words: Simple or Compound
    if interest == "Simple":
        simple_inte = deposit_money * (1 + (inte_rate1 / 100) * num_years)
        print(simple_inte)
    elif interest == "Compound":
        compound_inte = deposit_money * math.pow((1 + (inte_rate1 / 100)), num_years)
        print(compound_inte)
elif (financial_cal == "BOND") or (financial_cal == "Bond") or (financial_cal == "bond"):
    house_value = float(input("Enter the present value of the house: "))
    inte_rate2 = float(input("Enter the interest rate: "))  #Input the interest rate using only numbers (don't put the % symbol)
    num_months = float(input("Enter the number of months you plan to take to repay the bond: ")) 
    repayment = house_value / ((1 - (1 - ((inte_rate2 / 100) ** (- num_months)) / (inte_rate2 / 100))))
    print(repayment)


    


                      



