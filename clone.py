import subprocess
import os
import sys


log = open("log.txt", "w")
error = open ("error.txt", "w")


def check_git():
    try:
        subprocess.check_call(["git", "-version"], stdout=log, stderr=error)
    except subprocess.CalledProcessError:
        print("Please install github")


def clone_repo():
    github_user = (input("Please enter your github username:")) # Probably do not need for public repo's
    github_repo = (input("Please enter your github repo URL:"))
    command = str("curl -u %s https://api.github.com/user" % github_user)
    os.system(command)
    command = str("git clone %s" % github_repo)
    os.system(command)


check_git()
clone_repo()






