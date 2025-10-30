import requests, webbrowser, sys
import pygal
from datetime import datetime
from pathlib import Path

API_KEY = "CQTGP3IZCHMSUM53"

def ask_inputs():
    print("Stock Data Visualizer")
    print("---------------------\n")
    symbol = input("Enter the stock symbol you are looking for: ").strip().upper()

    print("\nChart Types")
    print("------------")
    print("1. Bar")
    print("2. Line")
    chart_pick = input("\nEnter the chart type you want (1, 2): ").strip()

    print("\nSelect the Time Series of the chart you want to Generate")
    print("---------------------------------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")
    series_pick = input("\nEnter the seires option (1, 2, 3, 4): ").strip()

    begin_str = input("\nEnter the start Date (YYYY-MM-DD): ").strip()
    end_str   = input("Enter the end Date (YYYY-MM-DD): ").strip()

    if not symbol or chart_pick not in ("1","2") or series_pick not in ("1","2","3","4"):
        print("Input error"); sys.exit(1)
    try:
        begin_date = datetime.strptime(begin_str, "%Y-%m-%d").date()
        end_date   = datetime.strptime(end_str,   "%Y-%m-%d").date()
    except:
        print("Dates must be YYYY-MM-DD."); sys.exit(1)
    if end_date < begin_date:
        print("End date cannot be before the begin date."); sys.exit(1)

    return symbol, chart_pick, series_pick, begin_date, end_date

def series_params(series_pick):
    if series_pick == "1":
        return ("TIME_SERIES_INTRADAY", "Time Series (60min)", {"interval":"60min","outputsize":"full"}, "Intraday (60min)")
    if series_pick == "2":
        return ("TIME_SERIES_DAILY", "Time Series (Daily)", {"outputsize":"full"}, "Daily")
    if series_pick == "3":
        return ("TIME_SERIES_WEEKLY", "Weekly Time Series", {}, "Weekly")
    return ("TIME_SERIES_MONTHLY", "Monthly Time Series", {}, "Monthly")