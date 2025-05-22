"""
Investment growth calculator module
"""
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

class Investment:
    """Class to analyze investment growth with compound interest."""
    
    def __init__(self, principal, annual_rate, years, monthly_contribution=0):
        """
        Initialize investment parameters.
        
        Args:
            principal (float): Initial investment amount
            annual_rate (float): Annual interest rate (decimal)
            years (int): Investment period in years
            monthly_contribution (float): Monthly additional contribution
        """
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.monthly_contribution = monthly_contribution
        self.monthly_rate = annual_rate / 12
        self.total_months = years * 12
        self.results = None
    
    def calculate_growth(self):
        """Calculate investment growth over time."""
        # Initialize arrays to track balance and growth
        balance = np.zeros(self.total_months + 1)
        balance[0] = self.principal
        
        # Calculate monthly compounding with contributions
        for month in range(1, self.total_months + 1):
            interest = balance[month-1] * self.monthly_rate
            balance[month] = balance[month-1] + interest + self.monthly_contribution
        
        # Create results array with year, balance and interest
        self.results = []
        for year in range(self.years + 1):
            month_idx = year * 12
            if year == 0:
                interest_earned = 0
                contributions = 0
            else:
                prev_year_idx = (year - 1) * 12
                interest_earned = balance[month_idx] - balance[prev_year_idx] - (self.monthly_contribution * 12)
                contributions = self.monthly_contribution * 12
            
            self.results.append({
                'year': year,
                'balance': balance[month_idx],
                'interest_earned': interest_earned,
                'contributions': contributions
            })
    
    def display_results(self):
        """Display investment growth results."""
        if self.results is None:
            self.calculate_growth()
        
        print("\nInvestment Growth Summary:")
        print(f"Initial investment: ${self.principal:,.2f}")
        print(f"Annual interest rate: {self.annual_rate * 100:.2f}%")
        print(f"Investment period: {self.years} years")
        print(f"Monthly contribution: ${self.monthly_contribution:,.2f}")
        
        # Create table rows for display
        rows = []
        for result in self.results:
            rows.append([
                result['year'],
                f"${result['balance']:,.2f}",
                f"${result['interest_earned']:,.2f}",
                f"${result['contributions']:,.2f}"
            ])
        
        # Display as table
        headers = ["Year", "Balance", "Interest Earned", "Contributions"]
        print("\n" + tabulate(rows, headers=headers, tablefmt="grid"))
        
        # Display final results
        final = self.results[-1]
        total_interest = sum(result['interest_earned'] for result in self.results)
        total_contributions = sum(result['contributions'] for result in self.results)
        
        print(f"\nFinal balance after {self.years} years: ${final['balance']:,.2f}")
        print(f"Total contributions: ${total_contributions:,.2f}")
        print(f"Total interest earned: ${total_interest:,.2f}")
        print(f"Investment growth: {(final['balance'] / self.principal - 1) * 100:.2f}%")
    def plot_growth(self):
        """Generate and display a plot of investment growth."""
        if self.results is None:
            self.calculate_growth()
        
        years = [r['year'] for r in self.results]
        balances = [r['balance'] for r in self.results]
        
        # Calculate cumulative components
        principal_component = np.ones(len(years)) * self.principal
        contribution_component = np.zeros(len(years))
        for i in range(1, len(years)):
            contribution_component[i] = self.monthly_contribution * 12 * i
        
        interest_component = np.array(balances) - principal_component - contribution_component
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.bar(years, principal_component, label='Initial Principal', color='#1f77b4')
        plt.bar(years, contribution_component, bottom=principal_component, 
                label='Contributions', color='#ff7f0e')
        plt.bar(years, interest_component, 
                bottom=principal_component+contribution_component, 
                label='Interest', color='#2ca02c')
        
        plt.plot(years, balances, 'k--', label='Total Balance')
        
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Value ($)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Format y-axis to show dollar amounts
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
        
        plt.tight_layout()
        plt.show(block=False)  # Non-blocking display
        plt.pause(0.1)  # Small pause to render the plot
