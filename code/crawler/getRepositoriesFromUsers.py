from github import Github
import pymongo as mongodb
from time import sleep

RATE = 3600 / 5000
MongoClient = mongodb.MongoClient(
    "mongodb://CS3012Github:githubcrawler@cluster0-shard-00-00-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-01-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-02-lj8g0.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = MongoClient["GithubDB"]
nameDB = db["usernames"]
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
totalQueries = 1000
x = 0
for name in nameDB.find().limit(totalQueries):
    x += 1
    gitUser = git.get_user(name["name"])
    sleep(RATE)
    repos = gitUser.get_repos()
    sleep(RATE)
    for repo in repos:
        repository_name = name["name"] + "/" + repo.name
        repositoryNames.add(repository_name)
    print(str(round(x * 100 / totalQueries, 2)) + " % of the way there for repositories")

list_repositories = []
for name in repositoryNames:
    tempDic = {"name": name}
    list_repositories.append(tempDic)
repositoryDB.insert_many(list_repositories)

repositoryCount = len(repositoryNames)
x = 0
for repositoryName in repositoryNames:
    x += 1
    repo = git.get_repo(repositoryName)
    sleep(RATE)
    languages = repo.get_languages()
    sleep(RATE)
    for language in languages:
        languageDictionary[language] = {"bytes": 0, "repositories": 0} if language not in languageDictionary else \
            languageDictionary[language]
        languageDictionary[language]["bytes"] += languages[language]
        languageDictionary[language]["repositories"] += 1
    print(str(round(x * 100 / repositoryCount, 2)) + " % of the way there for languages")

list_languages = []
for language in languageDictionary:
    tempDic = {"name": language, "bytes": languageDictionary.get(language).get("bytes"),
               "#repositories": languageDictionary.get(language).get("repositories")}
    list_languages.append(tempDic)

languageDB.insert_many(list_languages)
