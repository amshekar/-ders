from github import Github
from constants import *

g = Github("gautam0707","0801nineTeeN1")


def py_github_api_get_followers_count(profile_id, depth=2):
    if depth == 0:
        return g.get_user(profile_id).followers * followers_weighing_factors[0]

    q = list()
    q.append((profile_id, 0))
    followers_count = 0
    curr_depth = 0
    while q and depth > curr_depth:
        curr = q[0][0]
        curr_depth = q[0][1]
        del q[0]
        followers_count += g.get_user(curr).followers * followers_weighing_factors[curr_depth]
        for follower in g.get_user(curr).get_followers():
            q.append((follower.login, curr_depth+1))
    return followers_count


def py_github_api_get_points(profile_id):
    total_count = 0
    for repo in g.get_user(profile_id).get_repos():
        repo = g.get_user(profile_id).get_repo(repo.name)
        total_count += repo.forks_count
        total_count += repo.stargazers_count
        total_count += repo.subscribers_count
    return total_count
