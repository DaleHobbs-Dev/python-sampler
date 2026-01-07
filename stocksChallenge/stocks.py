"""
Simple module to manage stock pricing and purchases
"""

# Initialize a dictionary of stock ticker symbols
ticker_symbols = {"GM": "General Motors", "CAT": "Caterpillar", "EK": "Eastman Kodak"}

# Purchases of stock
# Tuple format: (ticket symbol, shares purchased, date of purchase, share price)
purchases = [
    ("GE", 100, "10-sep-2001", 48),
    ("CAT", 100, "1-apr-1999", 24),
    ("GE", 200, "1-jul-1998", 56),
    ("GE", 150, "15-jan-2002", 42),
    ("CAT", 50, "20-oct-2003", 68),
    ("EK", 120, "5-mar-2000", 33),
    ("GE", 300, "9-nov-1997", 61),
    ("CAT", 75, "12-aug-2004", 72),
    ("EK", 200, "30-dec-1999", 28),
    ("GE", 180, "2-feb-2005", 36),
    ("CAT", 220, "18-may-2001", 55),
    ("EK", 90, "7-jun-2002", 25),
    ("GE", 250, "11-jan-1996", 49),
]


# Function that displays the entire purchase history of stocks
def purchase_report():
    """Displays the purchase history for all stocks"""
    print("List of all purchases")
    print("------------------------")
    for symbol, shares, _, price in purchases:
        if symbol == "GE":
            print(f"General Electric stock purchased for ${shares * price}.")
        if symbol == "EK":
            print(f"Eastman Kodak stock purchased for ${shares * price}.")
        if symbol == "CAT":
            print(f"Caterpillar stock purchased for ${shares * price}.")


# Functions that outputs a stock dictionary
def build_stocks_dict(purchase_list):
    """Builds dictionary based on stock purchases"""
    result_dict = {}
    for symbol, shares, date, price in purchase_list:
        if symbol not in result_dict:
            result_dict[symbol] = []  # create list if key not there yet
        result_dict[symbol].append((symbol, shares, date, price))
    return result_dict


# Function that displays the entire purchase history of stocks
def purchase_total_report():
    """Displays the purchase history for all stocks"""
    print("List of all purchases")
    print("------------------------")
    total_ge = 0
    total_ek = 0
    total_cat = 0
    for symbol, shares, _, price in purchases:
        if symbol == "GE":
            total_ge += shares * price
        if symbol == "EK":
            total_ek += shares * price
        if symbol == "CAT":
            total_cat += shares * price
    print(f"General Electric stock purchased for ${total_ge}.")
    print(f"Caterpillar stock purchased for ${total_cat}.")
    print(f"General Electric stock purchased for ${total_ek}.")


purchase_report()
stocks = build_stocks_dict(purchases)
print(stocks)
