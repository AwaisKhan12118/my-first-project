print("=== Stock Portfolio Tracker ===")

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 170,
    "MSFT": 450
}

total = 0

while True:
    stock = input("Enter stock name (AAPL, TSLA, GOOG, MSFT) or 'done': ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        value = stocks[stock] * quantity
        total += value
        print("Value =", value)
    else:
        print("Stock not found!")

print("\nTotal Portfolio Value =", total)