class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp=0
        self.followersmap={}
        self.tweetsmap={}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        # using the time mark the order, since we need to use the heap to get the item
        # the tiimestamp could be reverse
        self.timestamp-=1
        self.tweetsmap[userId]=self.tweetsmap.get(userId,[])+[(self.timestamp,tweetId)]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        # it seems like to merge k lists and return the 10
        theap=[]
        # users == userid + follower
        users=self.followersmap.get(userId,set())|set([userId])
        
        # add the lastest tweets of every user into heap
        for user in users:
            if user in self.tweetsmap and self.tweetsmap[user]:
                time,tweet=self.tweetsmap[user][-1]
                # time, tweet info, user id and the index for the tweet,
                theap.append((time,tweet,user,len(self.tweetsmap[user])-1))
        
        # build the heap
        heapq.heapify(theap)
        res=[]
        # get the laster 10
        for _ in xrange(10):
            if theap:
                time, tweet, user, index=heapq.heappop(theap)
                res.append(tweet)
                # adding the next tweet to the heap
                if index:
                    new_time,new_tweet=self.tweetsmap[user][index-1]
                    heapq.heappush(theap,(new_time,new_tweet,user,index-1))
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followersmap[followerId]=self.followersmap.get(followerId,set())|set([followeeId])
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followersmap:
            self.followersmap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)