class Twitter:

    def __init__(self):
        # UserId -> List of (time, tweetId)
        self.userTweets = defaultdict(list)
        # UserId -> set of users they follow
        self.userFollowees = defaultdict(set)
        # Time (increases when a tweet is posted)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        newsFeed = self.userTweets[userId].copy()
        for followeeId in self.userFollowees[userId]:
            for tweet in self.userTweets[followeeId]:
                newsFeed.append(tweet)
        # Sort fed based on time descending
        newsFeed.sort(key=lambda x: -x[0])
        for _, tweetId in newsFeed[:10]:
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userFollowees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollowees[followerId].discard(followeeId)