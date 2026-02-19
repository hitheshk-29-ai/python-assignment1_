annual_salary=float(input("enter your annual salary"))
portion_saved=float(input("enter the percentage of your monthly salary to save,in decimal"))
total_cost=float(input("enter the total cost of dreamed house"))
semi_annual_raise=float(input("enter semi annual raise,as a decimal"))
#constans in the problem
down_payment_portion=0.25
current_savings=0
annual_return=0.04

monthly_return=annual_return/12
#calulate down payment
down_payment=total_cost*0.25
months=0

while current_savings<down_payment:
    #calculate current monthly salary
    monthly_salary=annual_salary/12
    current_savings+=current_savings*monthly_return
    current_savings+=monthly_salary*portion_saved
    months+=1

    #apply raise every 6 months
    if months%6==0:
        annual_salary+=annual_salary*semi_annual_raise

print("number of months:",months)