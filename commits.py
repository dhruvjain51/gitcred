import requests
import json
from requests.auth import HTTPDigestAuth


repository = "https://api.github.com/repos/dhruvjain51/gitcred/stats/contributors"



def get_highest_commits(repository):
    r = requests.get(repository)
    data = json.loads(r.content)

    numCommits = 0
    login = ""
    for item in data:
        if item['total'] > numCommits:
            numCommits = item['total']
            login = item['author']['login']

    return(login, numCommits)
    # print(login)

def get_commits_user(user, repository):
    r = requests.get(repository)
    data = json.loads(r.content)

    numCommits = 0
    login = ""
    for item in data:
        if item['author']['login'] == user:
            numCommits = item['total']
            login = item['author']['login']

    return(login, numCommits)


# difference +1 to account for win
def num_commits_to_make(user, repository):
    return (get_highest_commits(repository)[1] - get_commits_user(user, repository)[1])


print(num_commits_to_make('shabad',repository))
