from  collections import defaultdict
class Twitter:

    def __init__(self):
        self.cnt=0
        self.user_post=defaultdict(list)
        self.user_follow=defaultdict(set)

    def postTweet(self,userID,tweetID):
        self.user_post[userID].append([self.cnt,tweetID])
        self.cnt+=1

    def getNewsFeed(self,userID):
        persons=self.user_follow[userID]
        res=[]
        res.extend(self.user_post[userID])
        for person in persons:
            res.extend(self.user_post[person])
        res.sort(key=lambda x:x[0],reverse=True)
        ans=[]
        for p in res[:10]:
            ans.append(p[1])
        return ans

    def follow(self,followID,followeeID):
        if followID!=followeeID:
            self.user_follow[followID].add(followeeID)

    def unfollow(self, followID, followeeID):
        if followeeID in self.user_follow[followID]:
            self.user_follow[followID].remove(followeeID)