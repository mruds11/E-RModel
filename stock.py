from typing import Optional
import yfinance as yf

class Stock:
    """
    A class to represent a stock holding (with type hints).
    """

    def __init__(self, company_name: str, symbol: str, qty: float, cost_per_share: float):
        """
        Initializes a new Stock object with user-provided input.

        Args:
            company_name (str): The name of the company.
            symbol (str): The stock symbol.
            qty (float): The number of shares held.
            cost_per_share (float): The cost per share of the stock.
        """

        self.company_name = company_name
        self.symbol = symbol
        self.qty = qty
        self.cost_per_share = cost_per_share

        self._calculate_values()  # Calculate dependent values

    def _calculate_values(self) -> None:
        """
        Calculates dependent values based on the provided input.
        """
        self.cost_price: float = self.qty * self.cost_per_share

        # You'll need to fetch the current market price 
        self.current_price: Optional[float] = self._fetch_current_price()  
        self.market_value: Optional[float] = self.qty * self.current_price if self.current_price else None 
        self.total_change: Optional[float] = self.market_value - self.cost_price if self.market_value else None
        self.gain_loss: Optional[float] = self.total_change 

        # Cannot calculate these without external data:
        self.weekly_change: float = 0.0 
        self.pe_ratio: float = 0.0  

    def _fetch_current_price(self) -> Optional[float]:
        """
        Placeholder: Replace this with logic to retrieve the current market price.
        """

        self.current_price = yf.info[self.symbol] 
        # You would use a financial data API (e.g., Yahoo Finance) here
        #return 100.0  # Temporary placeholder value 

    def __str__(self) -> str:
        """
        Returns a string representation of the Stock object.
        """
        # ... (Same as before) 
