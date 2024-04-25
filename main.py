from setup import *
from typing import *

def readSubs() -> list[str]:
	subList = []
	with open('subList.txt', 'r') as f:
		for subreddit in f.readlines():
			subList.append(subreddit)
	return subList

def subscribe(subList:list[str], reddit) -> None:
	for sub in subList:
		#print(f'Subscribing to {sub}')
		reddit.subreddit(sub).subscribe()
		#print(f'Subscribed to {sub}\n')

def main():
	reddit = setup()

	subList = readSubs()

	subscribe(subList, reddit)

if __name__ == '__main__':
	main()