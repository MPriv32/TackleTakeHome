from github import Github
import os
import boto3
import json

#Specify .env folder to store credentials
if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

#Authorization for DynamoDB
access_key = os.getenv('AWS_ACCESS_KEY')
secret_key = os.getenv('AWS_SECRET_KEY')

#DynamoDB table that contains the repo list
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
table = dynamodb.Table('TackleTakeHome')

# Scans repo names from DB and return a list of repos
response = table.scan()
data = response['Items']
repo_list = [x.get("repo") for x in data]


#Authorization to access repo data
access_token = os.getenv("ACCESS_TOKEN")
g = Github(access_token)

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

    #Check if rebase and merging is allowed
    if repo.allow_rebase_merge == True:
        print("Rebase and merge is allowed!")
    else:
        print("Rebase and merge isn't allowed.")

#Specifies if the head branch is set to auto delete after pull requests are merged
def auto_delete_enabled(branch):
    print(branch.protected)
        
#Loop through list of repos
for repo in repo_list:
    repo = g.get_repo(repo)
    branch = repo.get_branch("main")
    repo_merge_strategies(repo)
    auto_delete_enabled(branch)