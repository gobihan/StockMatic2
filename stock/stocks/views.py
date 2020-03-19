from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import yfinance as yf
import pandas as pd
import numpy as np
from .models import Stock, StockData

def index(request):
    return render(request, 'stocks/index.html')

def addStock(request):

    stock_name = request.POST['stock_name']
    stock_code = request.POST['stock_code']
    stock_sector = request.POST['stock_sector']

    print(stock_code)

    ticker = yf.Ticker(stock_code)
    # sector = msft.info['sector']
    data = ticker.history(period='60d', interval='2m')
    data.drop(["Dividends","Stock Splits"], axis = 1, inplace = True)
    # stock = Stock.objects.get(name = "Microsoft")
    new_stock = Stock(name = stock_name, symbol = stock_code, sector=stock_sector)
    new_stock.save()
    for date in data.index:
        stock_data = StockData(stock = new_stock, date = date, open_price = data.loc[date, "Open"], close_price = data.loc[date, "Close"], high_price = data.loc[date, "High"], low_price = data.loc[date, "Low"], volume = data.loc[date, "Volume"])
        stock_data.save()
    context = {
        'data': data,
        'sector': stock_sector
    }
    return render(request, 'stocks/displayStockData.html', context)

def getStockInfo(request, stock_code):
    ticker = yf.Ticker(stock_code)

    # Stock.objects.all()
    present = False
    stock = Stock.objects.filter(symbol=stock_code)
    
    if(stock): present = True
    
    context={
        'name' : ticker.info['longName'],
        'sector': ticker.info['sector'],
        'present': present
    }
    return JsonResponse(context)

def addStockData(request):

    for stock in Stock.objects.all():
        print(stock.symbol)
        stock_code = stock.symbol
        ticker = yf.Ticker(stock_code)
        data = ticker.history(period='6m', interval='2m')
        data.drop(["Dividends","Stock Splits"], axis = 1, inplace = True)
        counter = 0
        for date in data.index:
            if counter == 1: break 
            stock_data = StockData(stock = stock, date = date, open_price = data.loc[date, "Open"], close_price = data.loc[date, "Close"], high_price = data.loc[date, "High"], low_price = data.loc[date, "Low"], volume = data.loc[date, "Volume"])
            stock_data.save()
            counter+=1

    return JsonResponse({"msg":"Successfully added two more data points"})
