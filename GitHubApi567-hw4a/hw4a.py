import requests
import json

def validID(ID):
    if ID != None:
        return True
    else:
        return False
  
#get the names of repositories for the user
def getrepos(ID):
    url = f"https://api.github.com/users/{ID}/repos"
    user_data = requests.get(url).json()

    for repo in user_data:        
        name = repo['name']
        yield name

    #get the commits of those repositories
        url2 = f"https://api.github.com/repos/{ID}/{name}/commits"
        user_commits = requests.get(url2).json()
        n = len(user_commits)
        yield n

#function call and decision
if __name__=='__main__':
    ID = input("Enter GitHub User ID: ")
    if validID(ID):
        getrepos(ID)
        print(list(getrepos(ID)))
    else:
        print("Invalid GitHub username")


