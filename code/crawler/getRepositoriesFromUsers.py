from github import Github
import pymongo as mongodb

MongoClient = mongodb.MongoClient("mongodb://CS3012Github:githubcrawler@cluster0-shard-00-00-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-01-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-02-lj8g0.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = MongoClient["GithubDB"]
names = db["usernames"]
credentials = open("credentials")
user = credentials.readline().rstrip()
Pass = credentials.readline().rstrip()
clientId = credentials.readline().rstrip()
credentials.close()
git = Github(user, Pass)
docu = {"name": "test111"}
names.insert(docu)