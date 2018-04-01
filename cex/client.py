import requests
from cex.const import *

class CexClient(object):

    def __init__(self, searchItem, count):
        self.API_URL = 'https://wss2.cex.uk.webuy.io/v3/boxes?q={}&firstRecord=1&count={}'.format(searchItem, count) #Assigns a API_URL with the correct search term and item count.

    def mostPopular(self):
        res = requests.get(self.API_URL+'&sortBy=relevance') #Call with the most popular items
        res = res.json() #convert it to json
        try:
            res = res['response']['data']['boxes'] #Gets to the correct json heading
            return res
        except:
            TypeError
            print("No results")

    def priceLow(self):
        res = requests.get(self.API_URL + '&sortBy=sellprice&sortOrder=asc')  # Call with the most popular items
        res = res.json()  # convert it to json
        try:
            res = res['response']['data']['boxes']#Gets to the correct json heading
            return res
        except:
            TypeError
            print("No results")

    def priceHigh(self):
        res = requests.get(self.API_URL + '&sortBy=sellprice&sortOrder=desc')  # Call with the most popular items
        res = res.json()  # convert it to json
        try:
            res = res['response']['data']['boxes']#Gets to the correct json heading
            return res
        except:
            TypeError
            print("No results")

    def fromA(self):
        res = requests.get(self.API_URL + '&sortBy=boxname&sortOrder=asc')  # Call with the most popular items
        res = res.json()  # convert it to json
        try:
            res = res['response']['data']['boxes']#Gets to the correct json heading
            return res
        except:
            TypeError
            print("No results")

    def fromZ(self):
        res = requests.get(self.API_URL + '&sortBy=boxname&sortOrder=desc')  # Call with the most popular items
        res = res.json()  # convert it to json
        try:
            res = res['response']['data']['boxes']#Gets to the correct json heading
            return res
        except:
            TypeError
            print("No results")

    def topRated(self):
        res = requests.get(self.API_URL + '&sortBy=rating&sortOrder=desc')  # Call with the most popular items
        res = res.json()
        try:
            res = res['response']['data']['boxes']#Gets to the correct json heading
            return res
        except:
            TypeError
            print("No results")

    def displayResults(self, products):
        try:
            for i in range(len(products)): #Get how many items are in the search
                print("Product Name:        "+str(products[i][D['bN']])) # Gets the correct item using the constants
                print("Product Price:       "+"£"+str(products[i][D['sP']]))
                print("Product Rating:      "+str(products[i][D['bR']])+"/5")
                print("Product Category:    "+str(products[i][D['cFN']]))
                print("Purchase Link:       "+"https://uk.webuy.com/product-detail?id="+str(products[i][D['bI']])) #Produces a product link
                print("=---------------------------------------=")
        except:
            TypeError

class Gaming(CexClient):
    def __init__(self, searchItem, count):
        self.API_URL = 'https://wss2.cex.uk.webuy.io/v3/boxes?superCatId=1&q={}&firstRecord=1&count={}'.format(searchItem, count) #Url change to fit subgenre

class Dvd(CexClient):
    def __init__(self, searchItem, count):
        self.API_URL = 'https://wss2.cex.uk.webuy.io/v3/boxes?superCatId=2&q={}&firstRecord=1&count={}'.format(searchItem, count) #Url change to fit subgenre

class Computing(CexClient):
    def __init__(self, searchItem, count):
        self.API_URL = 'https://wss2.cex.uk.webuy.io/v3/boxes?superCatId=3&q={}&firstRecord=1&count={}'.format(searchItem, count) #Url change to fit subgenre

class Phones(CexClient):
    def __init__(self, searchItem, count):
        self.API_URL = 'https://wss2.cex.uk.webuy.io/v3/boxes?superCatId=4&q={}&firstRecord=1&count={}'.format(searchItem, count) #Url change to fit subgenre

class Electronics(CexClient):
    def __init__(self, searchItem, count):
        self.API_URL = 'https://wss2.cex.uk.webuy.io/v3/boxes?superCatId=5&q={}&firstRecord=1&count={}'.format(searchItem, count) #Url change to fit subgenre

class Music(CexClient):
    def __init__(self, searchItem, count):
        self.API_URL = 'https://wss2.cex.uk.webuy.io/v3/boxes?superCatId=8&q={}&firstRecord=1&count={}'.format(searchItem, count) #Url change to fit subgenre


