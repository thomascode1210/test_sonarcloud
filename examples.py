"""
Example script demonstrating the Financial Analysis Tool
"""
from finance_tools.investment import Investment
from finance_tools.loan import Loan
from finance_tools.budget import Budget

def investment_example():
    """Demonstrate investment growth calculator."""
    print("\n===== Investment Growth Example =====")
    
    investment = Investment(
        principal=10000,
        annual_rate=0.08,
        years=30,
        monthly_contribution=200
    )
    
    investment.calculate_growth()
    investment.display_results()

def loan_example():
    """Demonstrate loan payment calculator."""
    print("\n===== Loan Payment Example =====")
    
    loan = Loan(
        principal=250000,
        annual_rate=0.045,
        years=30
    )
    
    loan.calculate_payment()
    loan.display_results()

def budget_example():
    """Demonstrate budget analyzer."""
    print("\n===== Budget Analyzer Example =====")
    
    budget = Budget()
    budget.add_income(5000, "Salary")
    budget.add_income(1000, "Freelance")
    budget.add_income(200, "Dividends")
    
    budget.add_expense(1800, "Housing")
    budget.add_expense(600, "Car Payment")
    budget.add_expense(800, "Food")
    budget.add_expense(400, "Utilities")
    budget.add_expense(300, "Entertainment")
    budget.add_expense(250, "Insurance")
    budget.add_expense(600, "Savings")
    
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
