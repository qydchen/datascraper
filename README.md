### L2 Back End Challenge by David Chen

This back end challenge was implemented with python. The challenge required me to do two things:
scrape data from bestbuy.com and do some light statistical and quantitative analysis. Python
has great libraries such as BeautifulSoup and numpy that help solve these problems.

#### Scraping Data

In order to run the program, make sure BeautifulSoup and numpy is installed.

+ Enter this command on the Command Prompt to scrape: `python run_scrape.py`
+ This will scrape bestbuy.com with the search terms `curved_smart_tv` and `smart_tv`, filtered by Samsung, LG, Toshiba, Sony
+ The csv file will be saved in the `data` folder

The naming convention of the file will be in MMDDYY so that reading the data from a start date to end date will be simpler.

#### Reading Data

+ Enter this command on the Command Prompt to read the data: `python read_data.py`
+ The results that are printed out in the Command Prompt will aggregate ALL the days
+ If you need to look at only one day, create a new ReadData in `read_data.py` passing in a start date and `None` as the end date:

```python
one_day = ReadData('091617', None)
```

+ If you need to look at a specified time period, create a new ReadData in `read_data.py` passing in a start date and end date:

```python
two_days = ReadData('091417','091517')
```

+ Passing no parameters into ReadData will default to analyzing the entire `data` folder:

```python
all_days = ReadData()
```

#### Data Model

An example data model:

``` python
{
    id: [ranking, search_term, brand, rating, reviews],
     0: ['1', 'smart_tv', 'LG', '4.6', '274'],
     1: ['2', 'smart_tv', 'Samsung', '4.6', '5899'],
     2: ['3', 'smart_tv', 'LG', '4.6', '187'],
     3: ['4', 'smart_tv', 'Samsung', '4.6', '3318'],
     4: ['5', 'smart_tv', 'Samsung', '4.7', '219'],
     5: ['6', 'smart_tv', 'Samsung', '4.6', '2538'],
     6: ['7', 'smart_tv', 'LG', '4.8', '51'],
     7: ['8', 'smart_tv', 'LG', '4.6', '231'],
     8: ['9', 'smart_tv', 'LG', '4.5', '443'],
     9: ['10', 'smart_tv', 'Samsung', '4.7', '360'],
     10: ['11', 'smart_tv', 'LG', '4.5', '130'],
     11: ['12', 'smart_tv', 'Samsung', '4.6', '2052'],
     12: ['13', 'smart_tv', 'Samsung', '4.5', '99']
 }
```

#### Answering Questions

##### To answer question 1: Given a set of competitor brands, for a given time range, for a given search term, what percentage of search results are owned by each brand?

+ Pass in the relevant `search_term` into the `brand_ownership` class method

```python
  all_days.brand_ownership('smart_tv')
  all_days.brand_ownership('curved_smart_tv')
```

From 09/14/17 to 09/17/17, the % of brand ownership for `smart_tv`: LG: 32%, Samsung: 65%, Sony: 3%.

From 09/14/17 to 09/17/17, the % of brand ownership for `curved_smart_tv`: Samsung: 100%.

##### To answer question 2: Given a set of competitor brands, for a given time range, for a given search terms, what percentage of the top 3 search results are owned by each brand?

+ Pass in the relevant `search_term` into the `top_brands` class method

```python
  all_days.top_brands('smart_tv')
  all_days.top_brands('curved_smart_tv')
```

From 09/14/17 to 09/17/17, the % of top 3 search results for each brand for `smart_tv`: LG: 67%, Samsung: 33%.

From 09/14/17 to 09/17/17, the % of top 3 search results for each brand for `curved_smart_tv`: Samsung: 100%.

##### To answer question 3: Is there a correlation between the # of reviews and search ranking?
```python
  all_days.review_vs_ranking()
```
With a correlation coefficient of -0.00057, there appears to be no correlation between # of reviews and search ranking.

##### To answer question 4: Is there a correlation between the rating and search ranking?
```python
  all_days.rating_vs_ranking()
```
With a correlation coefficient of -0.05871, there also appears to be no correlation between rating and search ranking.

##### To view all of the answers that was run and saved:
```python
  all_days.view_results()
```

#### Final Note
This project was really fun. Hire me! :)
