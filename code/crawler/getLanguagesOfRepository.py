from github import Github
import pymongo as mongodb
from time import sleep

RATE = 3600 / 5000
MongoClient = mongodb.MongoClient(
    "mongodb://CS3012Github:githubcrawler@cluster0-shard-00-00-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-01-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-02-lj8g0.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = MongoClient["GithubDB"]
repositoryDB = db["repositories"]
languageDB = db["languages"]
credentials = open("credentials")
user = credentials.readline().rstrip()
Pass = credentials.readline().rstrip()
clientId = credentials.readline().rstrip()
credentials.close()
git = Github(user, Pass)
repositoryNames = set()
languageDictionary = {}

number_of_repositories = 20000
x = 0
for repository in repositoryDB.find().limit(number_of_repositories):
    x += 1
    try:
        repo = git.get_repo(repository["name"])
        sleep(RATE)
        languages = repo.get_languages()
        sleep(RATE)
        for language in languages:
            languageDictionary[language] = {"bytes": 0, "repositories": 0} if language not in languageDictionary else \
                languageDictionary[language]
            languageDictionary[language]["bytes"] += languages[language]
            languageDictionary[language]["repositories"] += 1
        print(str(round(x * 100 / number_of_repositories, 2)) + " % of the way there for languages")
    except Exception as e:
        print(repository["name"] + " gave an error")



list_languages = []
for language in languageDictionary:
    tempDic = {"name": language, "bytes": languageDictionary.get(language).get("bytes"),
               "#repositories": languageDictionary.get(language).get("repositories")}
    list_languages.append(tempDic)

languageDB.insert_many(list_languages)
