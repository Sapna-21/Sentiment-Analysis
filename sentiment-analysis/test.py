import twitter
import sys

# initialize api instance
twitter_api = twitter.Api(consumer_key='Ka1VpGE43Z76neQoN52tByNG8',
                        consumer_secret='xWwZx8Xfa6nc3ySMibefpkHX7bpnzc4ppQwOdnQqxsnDYvjbje',
                        access_token_key='730334089656434688-vfp9N0Yfduq6wWoGVVX5phoKBtrFXEw',
                        access_token_secret='a6PZeWijAGTQ9mhhfkdK1Vi8Tm0sk5NrD2tcQrxVUrWEn')

# test authentication
print(twitter_api.VerifyCredentials())
def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count = 10000)
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        print(tweets_fetched.translate(non_bmp_map))
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return

search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])
