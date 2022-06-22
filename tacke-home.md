# DevOps Take-Home
This is meant to be a quick exercise that demonstrates the ability to integrate multiple technologies to solve a problem.

# Task
Given a list of GitHub repos, audit the repos for the following:

- merge strategies:
  - merge commits allowed
  - squash merging allowed
  - rebase & merge allowed
- auto delete head branches

## Notes
- All of the above can be expressed as boolean values.
- Assume that your GitHub user has admin access to all of the repos.

## Considerations
- What's the best way to take the list of repos as input?
- How should the rest of the configuration be passed in?
- How should errors be handled and presented to the user?
- Documentation (e.g. "how does someone use this?")

# Stretch Goals
- Document how you would adapt and deploy this method to AWS Lambda or EKS.
- Document considerations for passing credentials and storing artifacts (e.g. S3).

# Resources

[GitHub API](https://docs.github.com/en/rest/reference/repos) - GitHub's RESTful API

[PyGithub](https://github.com/PyGithub/PyGithub) - Python implementation for the GitHub API

# Results
Export the results as a JSON object.

# Delivery
Provide zipped git repo via email. Please include the .git directory. Make meaningful commits along the way so we can see how you break up your work.
