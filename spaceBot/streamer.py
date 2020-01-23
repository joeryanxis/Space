my_mentions = api.mentions_timeline()

print(my_mentions[0])
user = "@"+my_mentions[0].author.screen_name
statusID = my_mentions[0].id 

tweet = my_mentions[0].text
tweet = tweet.replace(user, '')