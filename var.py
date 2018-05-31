#!/usr/bin/python
# -*- coding: utf-8 -*-

# var.py

import datetime
import numpy as np

from pandas_datareader import data as web
from scipy.stats import norm

def var_cov_var(P, c, mu, sigma):
    """Variance-Covariance calculation of daily Value-at-Risk
    using confidence level c, with mean of returns mu and 
    standard deviation of returns sigma, on a portfolio of value P."""
    alpha = norm.ppf(1-c, mu, sigma)
    return P - P*(alpha + 1)

def value_at_risk(symbol="", P="", c="", mu="", sigma=""):
    P = 1e6   # 1,000,000 USD
    c = 0.99  # 99% confidence interval
    data = web.DataReader(symbol,'yahoo',start,end)
    data["rets"] = data["Adj Close"].pct_change()    
    mu = np.mean(data["rets"])
    sigma = np.std(data["rets"])  
    var = var_cov_var(P, c, mu, sigma)
    print(symbol + " - $%0.2f" % var)      
    return var
    
if __name__ == "__main__":
    start = datetime.date(2000, 1, 1)
    end = datetime.date.today()
    print("\nPortfolio Value: $1000000.00")
    print("Confidence Level: 99%\n")
    print("Value-at-Risk:\n")
    
    value_at_risk("AAPL")
    value_at_risk("FB")
    value_at_risk("MSFT")
    value_at_risk("DIS")
    value_at_risk("MCD")
