from github import Github

credentials = open("credentials")
user = credentials.readline().rstrip()
Pass = credentials.readline().rstrip()
clientId = credentials.readline().rstrip()
credentials.close()
git = Github(user, Pass)
repos = git.get_user("krakker4life").get_repos()
for rep in repos:
    print(rep)
    contributors = rep.get_contributors()
    for contributor in contributors:
        print(contributor)
