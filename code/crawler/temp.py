from github import Github
import pprint as pp
credentials = open("credentials")
user = credentials.readline().rstrip()
Pass = credentials.readline().rstrip()
clientId = credentials.readline().rstrip()
credentials.close()
git = Github(user, Pass)
repos = git.get_user("gmarkall").get_repos();
for repo in repos:
    languages = repo.get_languages();
    pp.pprint(languages)