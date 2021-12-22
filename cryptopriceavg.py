# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:58:49 2021

@author: mikejgreene

This program is used to figure out how many shares to buy of a stock to 
average the price to a desired amount based on initial investment
"""
import numpy as np

# Place important information in 'info' variable

# info[0] = Name of Asset
# info[1] = Amount of Shares
# info[2] = Cost of individual share
# info[3] = Today's price of individual share
# info[4] = Desired final averaged Price

info = np.array(['LSK',7.8,11.937,3.9448,5.0]); #array forces all entries to be same type() = str 

## Calculations
#Name of share
name_share = info[0]
#Already Purchased
total_units = np.double(info[1]); #amount of shares 
price_purchased = np.double(info[2]); #cost of individual share at purchase ($)
total_cost = total_units * price_purchased; #total cost ($)

#Want to purchase
price_current = np.double(info[3]); #current price of stock ($)
desired_avg_price = np.double(info[4]); # desired final avg'd price ($)

#To Calculate
shares_to_buy = (total_cost - (total_units  * desired_avg_price)) / (desired_avg_price - price_current);
amount_to_spend = shares_to_buy * price_current;
shares_to_buy = round(shares_to_buy,2) # Round value to nearest hundredth
amount_to_spend = round(amount_to_spend,2) #Rouns value to nearest hundredth

print('You need to buy {0} amount of {1}. Totaling ${2} \n to bring down the average price from ${3} to ${4} \n '.format(shares_to_buy, name_share ,  amount_to_spend, price_purchased, desired_avg_price));

