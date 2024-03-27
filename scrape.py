import praw
import datetime
import langid
import sys
import re

# Reddit API credentials: please put your credentials in the <..> slots:
client_id = <CLIENT_ID>
client_secret = <CLIENT_SECRET>
username = <USER_NAME>
password = <PASS_WORD>
user_agent = <USER_AGENT>

def main():
    # Authenticate with Reddit
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         password=password,
                         user_agent=user_agent)
    
    ###The five arguments of the function:
    start = sys.argv[1]
    end =  sys.argv[2]
    lang = sys.argv[3]
    num_keywords = int(sys.argv[4])
    list_keywords = sys.argv[5:num_keywords+5]
    list_subreddits = sys.argv[num_keywords+5:]

    # Compile regex patterns for exact word matching
    keyword_patterns = [re.compile(r'\b{}\b'.format(re.escape(keyword)), re.IGNORECASE) for keyword in list_keywords]

    # Subreddits to search
    subreddits = list_subreddits

    # Calculate timestamps for the start and end of the time range
    start_date = datetime.datetime(*map(int, start.split(',')))  # Unpack and convert string input to datetime object
    end_date = datetime.datetime(*map(int, end.split(',')))  # Unpack and convert string input to datetime object
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    # Search for posts containing the keywords
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        print(f"Searching in r/{subreddit_name}...")
        for submission in subreddit.search(' OR '.join(list_keywords), limit=None, sort='new'):
            # Check if the submission was created within the desired time range
            if start_timestamp <= submission.created_utc <= end_timestamp and langid.classify(submission.selftext)[0] == lang:
                # Check if any of the keywords match as whole words in the title or selftext (content) of the post
                if any(pattern.search(submission.title) or pattern.search(submission.selftext) for pattern in keyword_patterns):
                    selftext_no_newlines = submission.selftext.replace('\n', ' ')
                    print("Title:", submission.title)
                    print("Content:", selftext_no_newlines)
                    print("URL:", submission.url)
                    print("---------------------")

if __name__ == "__main__":
    main()

