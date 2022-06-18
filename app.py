from github import Github
import os

#Specify .env folder to store credentials
if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

#Github repo name
repo_name = "MPriv32/fleetwood-k8s-project"

#Authentication with a personal access token
access_token = os.getenv("ACCESS_TOKEN")
g = Github(access_token)

#Assign repo name to a value
repo = g.get_repo(repo_name)

#Assign head branch to a value
branch = repo.get_branch("main")

#Specifies whether merge commits, squash merging and rebase & merge are allowed
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

#Specifies if the head branch is set to auto delete after pull requests are merged
def auto_delete_enabled(branch):
    print(branch.protected)
        
repo_merge_strategies(repo)
auto_delete_enabled(branch)