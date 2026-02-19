annual_salary=float(input("enter your salary"))
portion_saved=float(input("enter the percentage of your monthly salary to save,as a decimal"))
total_cost=float(input("enter total cost of your dream house"))
#constans given in the problems
portion_down_payment=0.25
current_savings=0
annual_return=0.04
#convert annual valuess to monthly values
monthly_salary=annual_salary/12
monthly_return=annual_return/12
#calculation of down_payment
down_payment=total_cost*0.25
months=0
#loop untill it reach down-payment
while current_savings<down_payment:
    current_savings+=current_savings*monthly_return
    current_savings+=monthly_salary*portion_saved
    months+=1
print("number of months:",months)