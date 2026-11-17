import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.count = 0  # Global timestamp for tweet ordering
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1  # Decrement so smaller count = more recent (makes min-heap act like max-heap by time)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        
        # Ensure the user always follows themselves
        self.following[userId].add(userId)
        
        # Collect recent tweets from self and all followees
        for followeeId in self.following[userId]:
            if followeeId in self.tweetMap:
                # Grab up to the 10 most recent tweets from this user to save time
                for t_count, tweetId in self.tweetMap[followeeId][-10:]:
                    min_heap.append([t_count, tweetId])
                    
        heapq.heapify(min_heap)
        
        res = []
        # Pop up to 10 most recent tweets (smallest counts)
        while min_heap and len(res) < 10:
            t_count, tweetId = heapq.heappop(min_heap)
            res.append(tweetId)
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
