from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "2440070016-Tk6ijnlHENoZNF3yWtkTmImSZbG7eroz6zWljS4"
access_token_secret = "8Bgth9cz3UhWFjzYHZMImrOdOSamOPv0r6g6NaWXICKQ6"
consumer_key = "6tEduLobxjzvwEVIToytfNhoj"
consumer_secret = "Uqg31sTZ9pu6x4SYDp1ROKvmyl7idfR4ICf7HuZYxIvrwj5k4I"


class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['google', 'facebook', 'microsoft'])
