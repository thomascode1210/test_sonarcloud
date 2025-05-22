"""
Example script demonstrating the Financial Analysis Tool
"""
from finance_tools.investment import Investment
from finance_tools.loan import Loan
from finance_tools.budget import Budget

def investment_example():
    """Demonstrate investment growth calculator."""
    print("\n===== Investment Growth Example =====")
    
    # Create an investment with initial parameters
    investment = Investment(
        principal=10000,         # Initial investment of $10,000
        annual_rate=0.08,        # 8% annual interest rate
        years=30,                # 30 year investment period
        monthly_contribution=200 # $200 monthly contribution
    )
    
    # Calculate and display results
    investment.calculate_growth()
    investment.display_results()
    
    # Uncomment to display graph (requires GUI)
    # investment.plot_growth()

def loan_example():
    """Demonstrate loan payment calculator."""
    print("\n===== Loan Payment Example =====")
    
    # Create a loan with initial parameters
    loan = Loan(
        principal=250000,  # $250,000 loan (e.g., mortgage)
        annual_rate=0.045, # 4.5% annual interest rate
        years=30           # 30 year term
    )
    
    # Calculate and display results
    loan.calculate_payment()
    loan.display_results()
    
    # Uncomment to see amortization schedule
    # loan.generate_amortization_schedule()

def budget_example():
    """Demonstrate budget analyzer."""
    print("\n===== Budget Analyzer Example =====")
    
    # Create a new budget
    budget = Budget()
    
    # Add sample incomes
    budget.add_income(5000, "Salary")
    budget.add_income(1000, "Freelance")
    budget.add_income(200, "Dividends")
    
    # Add sample expenses
    budget.add_expense(1800, "Housing")
    budget.add_expense(600, "Car Payment")
    budget.add_expense(800, "Food")
    budget.add_expense(400, "Utilities")
    budget.add_expense(300, "Entertainment")
    budget.add_expense(250, "Insurance")
    budget.add_expense(600, "Savings")
    
    # Display budget summary
    budget.display_summary()

def main():
    """Run all examples."""
    print("Financial Analysis Tool - Examples")
    investment_example()
    loan_example()
    budget_example()
    
    print("\nExamples completed. Run main.py to use the interactive application.")

if __name__ == "__main__":
    main()
