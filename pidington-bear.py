from twython import Twython

APP_KEY = 'glNP0P78YpwxXpIe0GGiAxO1Y'
APP_SECRET = '4BHUxp3jyPV1gMtHMlNSYtbJlAg9YBCL3fHfvlctTKF7NFt608'
OAUTH_TOKEN = '703778980692758530-Onl4fyDNCt98Q2vayoOYnFWN9qYxcFL'
OAUTH_TOKEN_SECRET = '5YGdTvLUibo2RFTrsaZIYDJ4jvY64i7ZyBabbsRglOJdJ'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

print(twitter.update_status(status="Testing from Twython!"))