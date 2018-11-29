import pymongo as mongodb
from bson import BSON
from bson import json_util
import json

MongoClient = mongodb.MongoClient(
    "mongodb://CS3012Github:githubcrawler@cluster0-shard-00-00-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-01-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-02-lj8g0.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = MongoClient["GithubDB"]
languages = db["languages"]
lst = list(languages.find({}, {"_id": 0}).sort("#repositories", mongodb.DESCENDING).limit(30))
print(lst)
print(len(lst))
f = open("C:\\Users\\xander\\PycharmProjects\\CS3012_GithubCrawlerAndVisualizer\\code\\webserver\\data\\languages.json","w")
json.dump(lst,default=json_util.default,fp=f)
