from github import Github
import os

#Specify .env folder to store credentials
if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

repo_lists = ["MPriv32/fleetwood-k8s-project", "MPriv32/TackleTakeHome"]

access_token = os.getenv("ACCESS_TOKEN")
g = Github(access_token)

def repo_merge_strategies(repo):
    #Check if merge commits are allowed
    if repo.allow_merge_commit == True:
        print("Merge commits are allowed!")
    else:
        print("Merge commits aren't allowed.")

    #Check if squash merging is allowed
    if repo.allow_squash_merge == True:
        print("Squash merging is allowed!")
    else:
        print("Squash merging isn't allowed.")


    if repo.allow_rebase_merge == True:
        print("Rebase and merge is allowed!")
    else:
        print("Rebase and merge isn't allowed.")

def auto_delete_enabled(branch):
    print(branch.protected)
        
for repo in repo_lists:
    repo = g.get_repo(repo)
    branch = repo.get_branch("main")
    repo_merge_strategies(repo)
    auto_delete_enabled(branch)