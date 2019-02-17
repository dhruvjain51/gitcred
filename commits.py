import requests
import json

# def getcommits(repo):
#     r = requests.get(repo)
#     json_string = (r.json())
#     length = len(json_string)
#     # return(json_string)
#     return length
#
#
#
#
# print(getcommits("https://api.github.com/repos/shabad/ImagineCode/commits"))


repository = "https://api.github.com/repos/shabad/gre_words/commits"

response = []
page = 1
next_page = True;
while next_page:
    r = requests.get(repository + "?page=" + str(page))
    response.append(r.json())
    if(len(r.json())) < 30:
        next_page = False;

    page = page +1;

# now at this stage, respose is an array with the responses in each single page

# print(len(response[]))
# total = 0;
# for rs in response:
#     total = total + len(rs)

# print(total)

committers = {}
# Assume everything is in first page
# print(response[0][0]['committer']['login'])

for cur_page in response:
    for item in cur_page:
        if item['committer']['login'] not in committers:
            committers[item['committer']['login']] = 1
        else:
            committers[item['committer']['login']] = committers[item['committer']['login']] + 1

print(committers)
