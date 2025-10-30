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
    time_series = input("Please enter time series: ").upper()
    start_date = input("Please enter a start date(YYYY-MM-DD): ")
    end_date = input("Please enter an end date(YYYY-MM-DD): ")


        