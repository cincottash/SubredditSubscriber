import praw

def setup():

	reddit = praw.Reddit(client_id='_37h-5vZJcrWYUIRaTmeYg', \
		                     client_secret='***', \
		                     user_agent='Subreddit Scraper', \
		                     username='throwaway10100110111', \
		                     password='***')

	return reddit