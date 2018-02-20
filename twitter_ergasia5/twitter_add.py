import tweepy##sta parakato simplironete ta klidia apo to app


def get_timeline(user):
	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
	auth.set_access_token(key, secret)
	api = tweepy.API(auth)
	return api.user_timeline(screen_name = user, count = 10)