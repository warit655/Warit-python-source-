"""
Personal Finance Calculator
Student: Phonphailin
Date: 30 July 2025
Purpose: Calculate monthly budget and savings based on user input
"""
monthly_income = float(input("Monthly income (THB): "))  
rent_cost = float(input("Accommodation rental fee (THB): "))  
food_budget = int(input("Food budget (THB): "))  
transportation_cost = float(input("Travel expenses (THB): "))  
entertainment_budget = int(input("Vacation budget (THB): "))  
investment_percent = float(input("investment percentage (%): "))  

total_fixed_expenses = rent_cost + transportation_cost  


total_variable_expenses = food_budget + entertainment_budget  

total_expenses = total_fixed_expenses + total_variable_expenses  

remaining_income = monthly_income - total_expenses  

emergency_fund = monthly_income * (emergency_fund_percent / 100)  

investment_amount = monthly_income * (investment_percent / 100)  

available_for_savings = remaining_income - emergency_fund - investment_amount  

expense_ratio = (total_expenses / monthly_income) * 100  


print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent:.1f}%): {emergency_fund:.2f} THB")
print(f"Investment ({investment_percent:.1f}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")