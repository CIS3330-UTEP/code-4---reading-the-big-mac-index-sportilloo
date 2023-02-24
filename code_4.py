# Servando Portillo - ID: South Carolina
# CIS 3330
# CODE 4 - Reading the Big Mac Index

import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
bmf = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    count = 0
    average = 0
    year = str(year)
    country_code = str(country_code)
    country_code = country_code.upper()
    for i, j in bmf.iterrows():
        if year in j.date:
            average = average + j.dollar_price
            count += 1
    return(round(float((average/count)), 2))
                

def get_big_mac_price_by_country(country_code):
    count = 0
    average = 0
    country_code = str(country_code)
    country_code = country_code.upper()
    for i, j in bmf.iterrows():
        if country_code in j.iso_a3:
            average = average + j.dollar_price
            count += 1
    return(round(float((average/count)), 2))
        

def get_the_cheapest_big_mac_price_by_year(year):
    c_name = ''
    c_code = ''
    price = float('inf')
    year = str(year)
    for i, j in bmf.iterrows():
        if year in j.date:
            if price > j.dollar_price:
                price = j.dollar_price
                c_name = j.country_name
                c_code = j.iso_a3
    result = "{}({}): ${}".format(c_name,c_code,float(round(price, 2)))
    return (result)


def get_the_most_expensive_big_mac_price_by_year(year):
    c_name = ''
    c_code = ''
    price = float('-inf')
    year = str(year)
    for i, j in bmf.iterrows():
        if year in j.date:
            if price < j.dollar_price:
                price = j.dollar_price
                c_name = j.country_name
                c_code = j.iso_a3
    result = "{}({}): ${}".format(c_name,c_code,float(round(price, 2)))
    return (result)

if __name__ == "__main__":
    while True:
        print("\n--- Welcome to the Big Mac Info Finder Thingy ---")
        print("\nPlease select one of the following options:")
        print("\n • Type 1 if you wish to GET BIG MAC PRICE BY YEAR")
        print("\n • Type 2 if you wish to GET BIG MAC PRICE BY COUNTRY")
        print("\n • Type 3 if you wish to GET THE CHEAPEST BIG MAC PRICE BY YEAR")
        print("\n • Type 4 if you wish to GET THE MOST EXPENSIVE BIG MAC PRICE BY YEAR")
        print("\n • Type 5 to EXIT")
        selection = int(input())
        if selection == 1:
            s_one_year = input("\nPlease enter the year: ")
            s_one_cc = input("\nPlease enter the country code: ")
            print("\nThis is the average price of a Big Mac in the year " + str(s_one_year) + ": $" + str(get_big_mac_price_by_year(s_one_year, s_one_cc)))
        if selection == 2:
            s_two_cc = input("\nPlease enter the country code: ")
            print("\nThis is the average price of a Big Mac in the country " + str(s_two_cc) + ": $" + str(get_big_mac_price_by_country(s_two_cc)))
        if selection == 3:
            s_three_year = input("\nPlease enter the year: ")
            print("\nThis is the cheapest price of the year: " + str(get_the_cheapest_big_mac_price_by_year(s_three_year)))
        if selection == 4:
            s_four_year = input("\nPlease enter the year: ")
            print("\nThis is the most expensive price of the year: " + str(get_the_most_expensive_big_mac_price_by_year(s_four_year)))
        if selection == 5:
            print("\nThank you for using the Big Mac Info Finder Thingy")
            break