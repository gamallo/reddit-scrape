# reddit-scrape

Scraping posts from Reddit by using API credentials


## Requeriments:
* Python modules: praw datetime langid (use `pip install`)
* You are required to be registered at Reddit and have Reddit API credentials: client_id = <CLIENT_ID>, client_secret = <CLIENT_SECRET>, username = <USER_NAME>, password = <PASS_WORD>, user_agent = <USER_AGENT>. For this purpose, go to www.reddit.com/prefs/apps (create another app)

## How to use:

*  The `scrape.py` script requires 5 arguments:

1. Start date: for instance "2024, 1, 1"

2. End date: for instance "2024, 3, 1"

3. Language: for instance "en"

4. A list of keywords. This is an open argument: it starts by an integer referring to the number of keywords you whish to use, following for the keywords. For instance: 3 trump biden putin.

5. A list of subreddits. This is also an open argument: you can put all the names you whish. For instance: news worlnews politics TrueReddit Confession

This is an exemple of use (3 keywords followed by two subreddits):

```python3 scrape.py "2024, 1, 1" "2024, 3, 1" "en" 3 trump biden putin news Confession```

This is another example: (1 keyword followed by three subreddits):

```python3 scrape.py "2024, 1, 1" "2024, 3, 1" "en" 1 depression Confession TrueReddit```

## Output

For each post it gives three lines: Title, Content, URL.
