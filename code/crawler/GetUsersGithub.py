from github import Github
from time import time
import pymongo as mongodb

MongoClient = mongodb.MongoClient("mongodb://CS3012Github:githubcrawler@cluster0-shard-00-00-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-01-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-02-lj8g0.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = MongoClient["GithubDB"]
collection = db["usernames"]
credentials = open("credentials")
user = credentials.readline().rstrip()
Pass = credentials.readline().rstrip()
clientId = credentials.readline().rstrip()
credentials.close()
git = Github(user, Pass)
users_checked = set()
users_notChecked = set([user])
start = time()
while len(users_notChecked) != 0 and time() - start < 60*15 and len(users_notChecked) + len(users_checked) < 10000:
    print("you won't see this")
    member = users_notChecked.pop()
    users_repos = git.get_user(member).get_repos()
    for repo in users_repos:
        contributors = repo.get_contributors()
        for contributor in contributors:
            name = contributor.login
            if name not in users_checked :
                users_notChecked.add(name)
    users_checked.add(member)

users_checked.update(users_notChecked)
names = []
for name in users_checked:
    tempDic = {"name":name}
    names.append(tempDic)

collection.insert_many(names)

