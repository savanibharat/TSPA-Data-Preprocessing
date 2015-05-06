auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")

# Redirect user to Twitter to authorize
redirect_user(auth.get_authorization_url())

# Get access token
auth.get_access_token("verifier_value")

# Construct the API instance
api = tweepy.API(auth)
# Iterate through all of the authenticated user's friends
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    process_friend(friend)

# Iterate through the first 200 statuses in the friends timeline
for status in tweepy.Cursor(api.friends_timeline).items(200):
    # Process the status here
    process_status(status)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

page = 1
while True:
    statuses = api.user_timeline(page=page)
    if statuses:
        for status in statuses:
            # process status here
            process_status(status)
    else:
        # All done
        break
    page += 1  # next page

for status in tweepy.Cursor(api.user_timeline).items():
    # process status here
    process_status(status)

api.user_timeline(id="twitter")
for page in tweepy.Cursor(api.user_timeline).pages():
    # page is a list of statuses
    process_page(page)

# Only iterate through the first 200 statuses
for status in tweepy.Cursor(api.user_timeline).items(200):
    process_status(status)

# Only iterate through the first 3 pages
for page in tweepy.Cursor(api.user_timeline).pages(3):
    process_page(page)    