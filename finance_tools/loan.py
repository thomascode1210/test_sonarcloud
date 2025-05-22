"""
Loan payment calculator module
"""
import numpy as np
from tabulate import tabulate

class Loan:
    """Class to analyze loan payments and amortization."""
    
    def __init__(self, principal, annual_rate, years):
        """
        Initialize loan parameters.
        
        Args:
            principal (float): Loan amount
            annual_rate (float): Annual interest rate (decimal)
            years (int): Loan term in years
        """
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.monthly_rate = annual_rate / 12
        self.total_months = years * 12
        self.monthly_payment = None
        self.total_payment = None
        self.total_interest = None
        self.amortization_schedule = None
    
    def calculate_payment(self):
        """Calculate monthly payment and loan statistics."""
        # Monthly payment formula: P = L[c(1 + c)^n]/[(1 + c)^n - 1]
        # Where:
        # P = monthly payment
        # L = loan amount
        # c = monthly interest rate
        # n = total number of payments
        
        if self.monthly_rate == 0:
            # Handle zero interest case
            self.monthly_payment = self.principal / self.total_months
        else:
            numerator = self.monthly_rate * (1 + self.monthly_rate) ** self.total_months
            denominator = (1 + self.monthly_rate) ** self.total_months - 1
            self.monthly_payment = self.principal * (numerator / denominator)
        
        self.total_payment = self.monthly_payment * self.total_months
        self.total_interest = self.total_payment - self.principal
    
    def display_results(self):
        """Display loan payment results."""
        if self.monthly_payment is None:
            self.calculate_payment()
        
        print("\nLoan Payment Summary:")
        print(f"Loan amount: ${self.principal:,.2f}")
        print(f"Annual interest rate: {self.annual_rate * 100:.2f}%")
        print(f"Loan term: {self.years} years ({self.total_months} months)")
        print(f"Monthly payment: ${self.monthly_payment:,.2f}")
        print(f"Total payment: ${self.total_payment:,.2f}")
        print(f"Total interest: ${self.total_interest:,.2f}")
    
    def generate_amortization_schedule(self):
        """Generate and display amortization schedule."""
        if self.monthly_payment is None:
            self.calculate_payment()
        
        # Initialize arrays
        remaining_balance = np.zeros(self.total_months + 1)
        remaining_balance[0] = self.principal
        
        print("\nAmortization Schedule:")
        print("(Showing annual summary)")
        
        rows = []
        for year in range(1, self.years + 1):
            month = year * 12
            
            # Calculate values for this year
            year_interest = 0
            year_principal = 0
            
            for m in range((year-1)*12 + 1, year*12 + 1):
                # Calculate interest for this month
                interest_payment = remaining_balance[m-1] * self.monthly_rate
                principal_payment = self.monthly_payment - interest_payment
                
                # Update balance
                remaining_balance[m] = remaining_balance[m-1] - principal_payment
                
                # Add to yearly totals
                year_interest += interest_payment
                year_principal += principal_payment
            
            # Add row to table
            rows.append([
                year,
                f"${year_principal:,.2f}",
                f"${year_interest:,.2f}",
                f"${self.monthly_payment * 12:,.2f}",
                f"${remaining_balance[month]:,.2f}"
            ])
        
        # Display as table
        headers = ["Year", "Principal Paid", "Interest Paid", "Total Payment", "Remaining Balance"]
        print("\n" + tabulate(rows, headers=headers, tablefmt="grid"))
        
        # Allow user to see detailed monthly schedule if desired
        see_detailed = input("\nWould you like to see the detailed monthly schedule? (y/n): ")
        if see_detailed.lower() == 'y':
            self._show_detailed_schedule(remaining_balance)
    
    def _show_detailed_schedule(self, remaining_balance):
        """Display detailed monthly amortization schedule."""
        print("\nDetailed Monthly Amortization Schedule:")
        
        # Reset balance to recalculate
        balance = self.principal
        
        detailed_rows = []
        for month in range(1, self.total_months + 1):
            # Calculate values for this month
            interest_payment = balance * self.monthly_rate
            principal_payment = self.monthly_payment - interest_payment
            balance -= principal_payment
            
            # Only show every 12th month to avoid overwhelming output
            if month % 12 == 0 or month <= 12:
                detailed_rows.append([
                    month,
                    f"${principal_payment:,.2f}",
                    f"${interest_payment:,.2f}",
                    f"${self.monthly_payment:,.2f}",
                    f"${balance:,.2f}"
                ])
        
        # Display as table
        headers = ["Month", "Principal", "Interest", "Payment", "Remaining Balance"]
        print("\n" + tabulate(detailed_rows, headers=headers, tablefmt="grid"))
