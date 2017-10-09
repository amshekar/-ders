from pyGithubApi import *


class ProfileRanker:
    def __init__(self, profile_id):
        self.profile_id = profile_id
        pass

    def get_points(self):
        return py_github_api_get_points(self.profile_id)

    def get_followers(self):
        return py_github_api_get_followers_count(self.profile_id)

    def get_score(self):
        return self.get_points() + self.get_followers()


if __name__ =="__main__":
    profiles = ["amshekar"]
    for id in profiles:
        pr = ProfileRanker(id)
        print(id+"-->"+str(pr.get_score()))
