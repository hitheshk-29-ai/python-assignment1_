starting_salary = float(input("Enter the starting salary: "))

# Given constants
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
annual_return = 0.04
semi_annual_raise = 0.07
months = 36

# Bisection search parameters
low = 0
high = 10000
steps = 0
best_rate = None

while low <= high:
    steps += 1
    
    mid = (low + high) // 2
    portion_saved = mid / 10000
    
    current_savings = 0
    annual_salary = starting_salary

    # Simulate 36 months
    for month in range(1, months + 1):
        monthly_salary = annual_salary / 12
        
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_salary * portion_saved
        
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    # Check if within $100 
    if (current_savings >= down_payment - 100) and (current_savings <= down_payment + 100):
        best_rate = portion_saved
        break

    elif current_savings < down_payment - 100:
        low = mid + 1

    else:
        high = mid - 1

# Output
if best_rate is None:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)