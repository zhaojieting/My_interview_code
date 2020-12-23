from datetime import datetime
import time

class User:
    def __init__(self,user_id):
        self.posts = dict()
        self.followees = list()
        self.followers = list()
        self.id = user_id


class Weibo:
    def __init__(self):
        self.users = dict()
        self.users.update({1:User(1),2:User(2)})

    def postBlog(self,user_id,blog_id):
        if user_id in self.users.keys():
            t = datetime.now().timestamp()
            self.users[user_id].posts.update({t:blog_id})
        else:
            user = User(user_id)
            t = datetime.time().timestamp()
            user.posts.update({t:blog_id})
            self.users.update({user_id:user})
        time.sleep(0.01)
        return 0

    def follow(self,user1_id,user2_id):
        if user1_id in self.users[user2_id].followers:
            print('User {} followed User {} already!'.format(user1_id,user2_id))
        else:
            print('User {} is following User {} now'.format(user1_id, user2_id))
            self.users[user2_id].followers.append(user1_id)
            self.users[user1_id].followees.append(user2_id)

    def unfollow(self, user1_id, user2_id):
        if user1_id not in self.users[user2_id].followers:
            print('User {} Not followed User {}!'.format(user1_id, user2_id))
        else:
            print('User {} is not following User {} now'.format(user1_id, user2_id))
            self.users[user2_id].followers.remove(user1_id)
            self.users[user1_id].followees.remove(user2_id)

    def getNewsFeed(self,user_id):
        all_posts = dict()
        all_posts.update(self.users[user_id].posts)
        followee_posts = dict()
        for followee in self.users[user_id].followees:
            followee_posts.update(self.users[followee].posts)

        all_posts.update(followee_posts)
        time_list = sorted(list(all_posts.keys()))
        index = 0
        result = list()
        for time in time_list[::-1]:
            if index >= 10: break
            result.append(all_posts[time])
            index += 1
        return result

if __name__ == '__main__':
    weibo = Weibo()
    weibo.postBlog(1,5)

    result = weibo.getNewsFeed(1)
    print(result)

    weibo.follow(1,2)
    weibo.postBlog(2,6)
    result = weibo.getNewsFeed(1)
    print(result)

    weibo.unfollow(1,2)
    print(weibo.getNewsFeed(1))