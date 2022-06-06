from typing import List

class User:
    def __init__(self):
        self.tweets = []
        self.following = set()

class Tweet:
    def __init__(self, tweet_id, counter ):
        self.id = tweet_id
        self.counter = counter

class Twitter:
    def __init__(self):
        self.users = dict()
        self.tweet_counter = 0

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        if user_id not in self.users:
            self.users[user_id] = User()

        user = self.users[user_id]
        tweet = Tweet(tweet_id, self.tweet_counter)
        user.tweets.append(tweet)
        self.tweet_counter += 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        if user_id not in self.users:
            self.users[user_id] = User()

        all_tweets = []

        user = self.users[user_id]
        all_tweets.extend(user.tweets)

        for following_id in user.following:
            following_user = self.users[following_id]
            all_tweets.extend(following_user.tweets)

        all_tweets.sort(key=lambda x: x.counter, reverse=True)

        tweet_ids = []

        for tweet in all_tweets[0: 10]:
            tweet_ids.append(tweet.id)


        return tweet_ids

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id not in self.users:
            self.users[follower_id] = User()

        if followee_id not in self.users:
            self.users[followee_id] = User()

        user = self.users[follower_id]
        user.following.add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if follower_id not in self.users:
            self.users[follower_id] = User()

        if followee_id not in self.users:
            self.users[followee_id] = User()

        user = self.users[follower_id]
        user.following.discard(followee_id)

twitter = Twitter()
twitter.postTweet(1, 1)
twitter.postTweet(1, 2)
twitter.postTweet(1, 3)
twitter.postTweet(1, 4)
twitter.postTweet(1, 5)
twitter.postTweet(1, 6)

twitter.follow(1, 2)
twitter.follow(1, 3)

twitter.postTweet(2, 7)
twitter.postTweet(2, 8)
twitter.postTweet(2, 9)
twitter.postTweet(2, 10)

twitter.postTweet(3, 11)
twitter.postTweet(3, 12)
twitter.postTweet(3, 13)
twitter.postTweet(3, 14)

print(twitter.getNewsFeed(1))


