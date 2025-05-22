"""
Budget analyzer module
"""
import matplotlib.pyplot as plt
from tabulate import tabulate
from collections import defaultdict

class Budget:
    """Class to analyze budget, expenses and income."""
    
    def __init__(self):
        """Initialize budget tracking."""
        self.incomes = []
        self.expenses = []
        self.income_categories = defaultdict(float)
        self.expense_categories = defaultdict(float)
    
    def add_income(self, amount, source):
        """
        Add an income entry to the budget.
        
        Args:
            amount (float): Income amount
            source (str): Source of income
        """
        if amount <= 0:
            raise ValueError("Income amount must be positive")
        
        self.incomes.append({"amount": amount, "source": source})
        self.income_categories[source] += amount
        print(f"Added income: ${amount:.2f} from {source}")
    
    def add_expense(self, amount, category):
        """
        Add an expense entry to the budget.
        
        Args:
            amount (float): Expense amount
            category (str): Expense category
        """
        if amount <= 0:
            raise ValueError("Expense amount must be positive")
        
        self.expenses.append({"amount": amount, "category": category})
        self.expense_categories[category] += amount
        print(f"Added expense: ${amount:.2f} for {category}")
    
    def calculate_total_income(self):
        """Calculate total income."""
        return sum(income["amount"] for income in self.incomes)
    
    def calculate_total_expenses(self):
        """Calculate total expenses."""
        return sum(expense["amount"] for expense in self.expenses)
    
    def calculate_balance(self):
        """Calculate budget balance."""
        return self.calculate_total_income() - self.calculate_total_expenses()
    
    def display_summary(self):
        """Display budget summary including income and expense breakdown."""
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        balance = self.calculate_balance()
        
        print("\n===== Budget Summary =====")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")
        
        # Display income breakdown
        if self.incomes:
            print("\nIncome Breakdown:")
            income_rows = []
            for source, amount in self.income_categories.items():
                percentage = (amount / total_income * 100) if total_income > 0 else 0
                income_rows.append([source, f"${amount:.2f}", f"{percentage:.1f}%"])
            
            headers = ["Source", "Amount", "Percentage"]
            print(tabulate(income_rows, headers=headers, tablefmt="grid"))
        
        # Display expense breakdown
        if self.expenses:
            print("\nExpense Breakdown:")
            expense_rows = []
            for category, amount in self.expense_categories.items():
                percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
                expense_rows.append([category, f"${amount:.2f}", f"{percentage:.1f}%"])
            
            headers = ["Category", "Amount", "Percentage"]
            print(tabulate(expense_rows, headers=headers, tablefmt="grid"))
            
            # Display expense chart
            self._plot_expense_breakdown()
    
    def _plot_expense_breakdown(self):
        """Generate and display expense breakdown pie chart."""
        if not self.expenses:
            return
            
        # Prepare data for pie chart
        categories = list(self.expense_categories.keys())
        amounts = list(self.expense_categories.values())
        
        # Only display detailed categories if there are ≤ 7
        # Otherwise, combine smaller categories
        if len(categories) > 7:
            sorted_indices = sorted(range(len(amounts)), key=lambda i: amounts[i], reverse=True)
            top_categories = [categories[i] for i in sorted_indices[:6]]
            top_amounts = [amounts[i] for i in sorted_indices[:6]]
            
            # Combine the rest into "Other"
            other_amount = sum(amounts[i] for i in sorted_indices[6:])
            if other_amount > 0:
                top_categories.append("Other")
                top_amounts.append(other_amount)
            
            categories = top_categories
            amounts = top_amounts
        
        # Create pie chart
        plt.figure(figsize=(10, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', 
                startangle=90, shadow=True)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title('Expense Breakdown')
        plt.tight_layout()
        plt.show()
