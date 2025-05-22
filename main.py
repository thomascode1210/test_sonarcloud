"""
Financial Analysis Tool - Main Application
"""
import sys
from finance_tools.investment import Investment
from finance_tools.loan import Loan
from finance_tools.budget import Budget

def display_menu():
    """Display the main menu of the application."""
    print("\n===== Financial Analysis Tool =====")
    print("1. Investment Growth Calculator")
    print("2. Loan Payment Calculator")
    print("3. Budget Analyzer")
    print("4. Exit")
    return input("Select an option (1-4): ")

def investment_calculator():
    """Run the investment calculator tool."""
    print("\n----- Investment Growth Calculator -----")
    try:
        principal = float(input("Enter initial investment amount: $"))
        rate = float(input("Enter annual interest rate (%): ")) / 100
        years = int(input("Enter investment period (years): "))
        monthly_contribution = float(input("Enter monthly contribution (optional, $0 for none): $"))
        
        investment = Investment(principal, rate, years, monthly_contribution)
        investment.calculate_growth()
        investment.display_results()
        investment.plot_growth()
    except ValueError:
        print("Error: Please enter valid numbers.")
    
    input("\nPress Enter to continue...")

def loan_calculator():
    """Run the loan calculator tool."""
    print("\n----- Loan Payment Calculator -----")
    try:
        principal = float(input("Enter loan amount: $"))
        rate = float(input("Enter annual interest rate (%): ")) / 100
        years = int(input("Enter loan term (years): "))
        
        loan = Loan(principal, rate, years)
        loan.calculate_payment()
        loan.display_results()
        loan.generate_amortization_schedule()
    except ValueError:
        print("Error: Please enter valid numbers.")
    
    input("\nPress Enter to continue...")

def budget_analyzer():
    """Run the budget analyzer tool."""
    print("\n----- Budget Analyzer -----")
    budget = Budget()
    
    while True:
        print("\n1. Add income")
        print("2. Add expense")
        print("3. View budget summary")
        print("4. Return to main menu")
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            try:
                amount = float(input("Enter income amount: $"))
                source = input("Enter income source: ")
                budget.add_income(amount, source)
            except ValueError:
                print("Error: Please enter a valid amount.")
        
        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: $"))
                category = input("Enter expense category: ")
                budget.add_expense(amount, category)
            except ValueError:
                print("Error: Please enter a valid amount.")
        
        elif choice == '3':
            budget.display_summary()
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid option. Please try again.")

def main():
    """Main application entry point."""
    while True:
        choice = display_menu()
        
        if choice == '1':
            investment_calculator()
        elif choice == '2':
            loan_calculator()
        elif choice == '3':
            budget_analyzer()
        elif choice == '4':
            print("\nThank you for using the Financial Analysis Tool. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
