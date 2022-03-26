# Make Bots

## Get started making a bot

So, you want to make an evil twitter bot?  There are lots of ways. This is one.

## Get a Twitter Dev Account
* First, go to [developer.twitter.com](https://developer.twitter.com/en)
    - Sign Up for a developer account
    - It'll take a bit of back and forth with Twitter, but you'll get it.  Be persistent.

## Learn Python
  * [python.org/about/gettingstarted](https://www.python.org/about/gettingstarted/)
  * [w3schools.com/python](https://www.w3schools.com/python/)
  * [geeksforgeeks.org/python-programming-language](https://www.geeksforgeeks.org/python-programming-language/)

## Use Tweepy
  * [tweepy.org](https://www.tweepy.org/)

## Now for the GOOD stuff.
### Annoy a Congressman's Intern
* Like 100 of his Tweets
```python
import tweepy 

class TweepyApi:
    def __init__(self):
        self.consumer_key = "YOUR_CONSUMER_KEY_HERE"
        self.consumer_secret = "YOUR_CONSUMER_SECRET_HERE"        
        self.access_token = "YOUR_ACCESS_TOKEN_HERE"
        self.access_token_secret = "YOUR__ACCESS_TOKEN_SECRET_HERE"     
        self.api = tweepy.API(self.get_auth(), wait_on_rate_limit=True)

        
    def get_auth(self):        
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)        
        return auth        
    

def annoy_don_bacons_intern():
    me = TweepyApi().api
    screen_name_ = 'donjbacon'
    dons_tweets = me.user_timeline(screen_name=screen_name_,trim_user=True,count=100)
    for tweet in dons_tweets:        
        me.create_favorite(id=tweet.id)



def main():
    annoy_don_bacons_intern()
    
    
if __name__ == '__main__':
    main()

```


