import json
import requests

import Functions as function
import Graph as graph

def createRate(number):
    answer = str(int(number * 100) / 100)
    return answer

def get_all_rates():
    allRates = ["CAD", "HKD", "ISK", "PHP", "DKK", "HUF", "CZK", "GBP", "RON", "SEK",
                "IDR", "INR", "BRL", "RUB", "HRK", "JPY", "THB", "CHF", "EUR", "MYR",
                "BGN", "TRY", "CNY", "NOK", "NZD", "ZAR", "USD", "MXN", "SGD", "AUD",
                "ILS", "KRW", "PLN"]
    response = json.loads(requests.get("https://api.exchangeratesapi.io/latest?base=USD").text)["rates"]
    string = ""
    for i in range(len(response)):
        string += allRates[i] + ": " + createRate(response[allRates[i]]) + "\n"
    return string

def get_history(currency):
    response = json.loads(requests.get("https://api.exchangeratesapi.io/history?start_at=2019-11-27&end_at=2019-12-03&base=USD&symbols=" + currency).text)["rates"]
    graph.create_graph_img(function.get_dates_and_rates(response, currency))

def convert_to(currency):
    response = json.loads(requests.get("https://api.exchangeratesapi.io/latest?base=USD").text)["rates"]
    rate = createRate(response[currency])
    rate = float(rate)
    answer = ": 10 USD = " + str(((10*rate) * 100) / 100) + " " + currency
    return answer