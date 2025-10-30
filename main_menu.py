import pandas as pd
import requests 
import matplotlib as plt
import webbrowser
import datetime

API_KEY = "CQTGP3IZCHMSUM53"

def main():
    print("\nWelcome to the Stock Data Visualizer!")

    stock_symbol = input("Please enter a stock symbol: ").upper()
    chart = input("Please enter the type of chart (line/bar): ").lower()
    time_series = input("Please enter time series(Time_Series_Daily, Time_Series_Weekly, Time_Series_Monthly): ").upper()
    start_date = input("Please enter a start date(YYYY-MM-DD): ")
    end_date = input("Please enter an end date(YYYY-MM-DD): ")

    try:
        start_date1 = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date1 = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        if end_date1 < start_date1:
            print("Error: End date cannot be before start date.")
            return
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return

    #Fetch data from Alpha Vantage
    print("\nFetching data, please wait....")
    url = f"https://www.alphavantage.co/query?function={time_series}&symbol={stock_symbol}&apikey={API_KEY}&outputsize=full"
    response = requests.get(url)
    data = response.json()

    key_mapping = {
        "Time_Series_Daily"
        "Time_Series_Weekly"
        "Time_Series_Montly"
    }
    if time_series not in key_mapping or key_mapping[time_series] not in data:
        print("Error: Could not find time series data. Please try again.")
        return 