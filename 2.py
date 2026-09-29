# ============================================================
#  Stock Portfolio Tracker
#  CodeAlpha Internship – Task 2
# ============================================================

import csv
import os
from datetime import datetime

# ---------- Hardcoded stock price dictionary (USD) ----------
STOCK_PRICES = {
    "AAPL":  180.00,   # Apple Inc.
    "TSLA":  250.00,   # Tesla Inc.
    "GOOGL": 140.00,   # Alphabet Inc.
    "AMZN":  185.00,   # Amazon.com Inc.
    "MSFT":  415.00,   # Microsoft Corp.
    "META":  505.00,   # Meta Platforms Inc.
    "NFLX":  625.00,   # Netflix Inc.
    "NVDA":  875.00,   # NVIDIA Corp.
    "BABA":   75.00,   # Alibaba Group
    "RELIANCE": 30.00, # Reliance Industries (approx. USD)
}

# ------------------------------------------------------------

def display_available_stocks():
    """Print all available stocks with their prices."""
    print("\n" + "=" * 45)
    print(f"{'Ticker':<12} {'Company / Stock':<20} {'Price (USD)':>10}")
    print("=" * 45)
    labels = {
        "AAPL": "Apple Inc.", "TSLA": "Tesla Inc.",
        "GOOGL": "Alphabet Inc.", "AMZN": "Amazon.com",
        "MSFT": "Microsoft Corp.", "META": "Meta Platforms",
        "NFLX": "Netflix Inc.", "NVDA": "NVIDIA Corp.",
        "BABA": "Alibaba Group", "RELIANCE": "Reliance Ind.",
    }
    for ticker, price in STOCK_PRICES.items():
        print(f"{ticker:<12} {labels.get(ticker, ''):<20} ${price:>9.2f}")
    print("=" * 45)


def get_portfolio():
    """Interactively collect stock names and quantities from the user."""
    portfolio = {}
    print("\nEnter your stock holdings. Type 'done' when finished.")

    while True:
        ticker = input("\nStock ticker (or 'done'): ").strip().upper()
        if ticker == "DONE":
            break
        if ticker not in STOCK_PRICES:
            print(f"  ⚠  '{ticker}' not found in the price list. Please choose from the available tickers.")
            continue

        try:
            qty = float(input(f"  Quantity of {ticker}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be greater than 0.")
                continue
        except ValueError:
            print("  ⚠  Invalid number. Please enter a numeric value.")
            continue

        # Accumulate if ticker is entered more than once
        portfolio[ticker] = portfolio.get(ticker, 0) + qty

    return portfolio


def calculate_portfolio(portfolio):
    """Return a list of (ticker, qty, price, value) tuples and the grand total."""
    rows = []
    total = 0.0
    for ticker, qty in portfolio.items():
        price = STOCK_PRICES[ticker]
        value = qty * price
        total += value
        rows.append((ticker, qty, price, value))
    return rows, total


def display_summary(rows, total):
    """Pretty-print the portfolio summary."""
    print("\n" + "=" * 58)
    print("               📊  PORTFOLIO SUMMARY")
    print("=" * 58)
    print(f"{'Ticker':<10} {'Qty':>8}  {'Price (USD)':>12}  {'Value (USD)':>12}")
    print("-" * 58)
    for ticker, qty, price, value in rows:
        print(f"{ticker:<10} {qty:>8.2f}  ${price:>11.2f}  ${value:>11.2f}")
    print("-" * 58)
    print(f"{'TOTAL INVESTMENT':.<40} ${total:>11.2f}")
    print("=" * 58)


def save_to_txt(rows, total, filename="portfolio_report.txt"):
    """Save the portfolio summary to a .txt file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "w") as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 58 + "\n")
        f.write(f"{'Ticker':<10} {'Qty':>8}  {'Price (USD)':>12}  {'Value (USD)':>12}\n")
        f.write("-" * 58 + "\n")
        for ticker, qty, price, value in rows:
            f.write(f"{ticker:<10} {qty:>8.2f}  ${price:>11.2f}  ${value:>11.2f}\n")
        f.write("-" * 58 + "\n")
        f.write(f"{'TOTAL INVESTMENT':.<40} ${total:>11.2f}\n")
        f.write("=" * 58 + "\n")
    print(f"\n  ✅  Report saved to: {filepath}")


def save_to_csv(rows, total, filename="portfolio_report.csv"):
    """Save the portfolio summary to a .csv file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker", "Quantity", "Price (USD)", "Value (USD)"])
        for ticker, qty, price, value in rows:
            writer.writerow([ticker, qty, price, round(value, 2)])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", round(total, 2)])
    print(f"  ✅  CSV saved to: {filepath}")


# ========================  MAIN  ============================

def main():
    print("\n╔══════════════════════════════════════════╗")
    print("║       STOCK PORTFOLIO TRACKER  📈         ║")
    print("╚══════════════════════════════════════════╝")

    display_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\n  No stocks entered. Exiting.")
        return

    rows, total = calculate_portfolio(portfolio)
    display_summary(rows, total)

    # --- Save options ---
    print("\nWould you like to save the report?")
    print("  1. Save as TXT")
    print("  2. Save as CSV")
    print("  3. Save as both")
    print("  4. Don't save")

    choice = input("\nEnter choice (1/2/3/4): ").strip()

    if choice == "1":
        save_to_txt(rows, total)
    elif choice == "2":
        save_to_csv(rows, total)
    elif choice == "3":
        save_to_txt(rows, total)
        save_to_csv(rows, total)
    else:
        print("\n  Report not saved.")

    print("\n  Thank you for using Stock Portfolio Tracker! 👋\n")


if __name__ == "__main__":
    main()
