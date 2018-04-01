# Cex WeBuy Python Wrapper
**Install using pip**
```
pip install cexapi
```

**To initialise use the API you first need to call the class you wish to use.**
Each class represents their own subgenre.

|Class|Description |
|--|--|
|CexClient|Performs a search through the entire site|
|Gaming|Performs a search on the gaming sub genre|
|Dvd|Performs a seach on the DVD sub genre|
|Computing|Performs a search on the computing sub genre|
|Phones|Performs a search on the phone sub genre|
|Electronics|Performs a search on the electronics sub genre|
|Music|Performs a search on the music sub genre|

Each class requires a search term and the amount of items to be collected. 50 is the maximum.

```python
Cex = CexClient("Search Term", 10)
```
|Function|Description  |
|--|--|
| mostPopular |Gathers the most popular items  |
|priceLow|Gathers the items with the lowest price|
|priceHigh|Gathers the items with the highest price|
|fromA|Gathers items which name starts with A|
|fromZ|Gathers items which name starts with Z|
|topRated|Gathers the most rated items|
|displayResults|Displays the results of the searched passed into it|

```python
mostPopular = Cex.mostPopular()
Cex.displayResults(mostPopular)
```




> ***v0.0.1***
> Initial release. Basic API allowing users to retrieve data from the site and it is displayed in a good manner.

