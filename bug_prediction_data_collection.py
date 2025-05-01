import requests
import pandas as pd

# Function to fetch issues and commits from a public GitHub repo
def fetch_github_data(owner, repo, token=None):
    headers = {"Authorization": f"token {token}"} if token else {}
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    # Get issues
    issues_url = f"{base_url}/issues"
    issues_response = requests.get(issues_url, headers=headers)
    issues_data = issues_response.json()
    
    # Get commits
    commits_url = f"{base_url}/commits"
    commits_response = requests.get(commits_url, headers=headers)
    commits_data = commits_response.json()

    return issues_data, commits_data

# Extract required fields
def process_data(issues, commits):
    data = []
    for issue in issues:
        if "pull_request" not in issue:
            data.append({
                "title": issue.get("title"),
                "body": issue.get("body"),
                "labels": [label['name'] for label in issue.get("labels", [])],
                "state": issue.get("state"),
                "is_buggy": 1 if "bug" in [label['name'] for label in issue.get("labels", [])] else 0,
                "author": issue.get("user", {}).get("login"),
                "message": None  # No commit message in issue data
            })

    for commit in commits:
        commit_data = commit.get("commit", {})
        data.append({
            "title": None,
            "body": None,
            "labels": [],
            "state": None,
            "is_buggy": 0,
            "author": commit_data.get("author", {}).get("name"),
            "message": commit_data.get("message")
        })
    
    return pd.DataFrame(data)

# ---------- CONFIG ----------
OWNER = "apache"
REPO = "spark"
GITHUB_TOKEN = None  # Optional: Add your GitHub personal access token if needed

# Fetch and process
issues, commits = fetch_github_data(OWNER, REPO, GITHUB_TOKEN)
df = process_data(issues, commits)

# Save to CSV
df.to_csv("github_data.csv", index=False)
print("Data saved to github_data.csv")
