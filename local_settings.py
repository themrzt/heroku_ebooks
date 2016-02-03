'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'DBBqNBKonI4Ingcyr96yiGcHO'
MY_CONSUMER_SECRET = '0a83HBkSLvnp4oVYMQRylIiWFGr5AfrQQAgN3aIhfiCLth8cd0'
MY_ACCESS_TOKEN_KEY = '15001652-G9KETuSKRBU5PCM4ykSyCSERGLJgpfWSHDNBSYmWy'
MY_ACCESS_TOKEN_SECRET = 'YWgCQwR0BxKOE6Fpu7llTMVcDPPLFHlxhswJ7wNEOc5lV'

SOURCE_ACCOUNTS = ["johnlegere", "sprint", "sprintcares", "marceloclaure"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 3 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = True #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "ztappsandbox42" #The name of the account you're tweeting to.
