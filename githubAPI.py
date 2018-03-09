import requests

api_base = "https://api.github.com"

def get_repos(id):
  url = "{0}/users/{1}/repos".format(api_base, id)
  r = requests.get(url)
  if r.status_code != 200: return "Request Failed"
  return r.json()

def get_commits(id, repo):
  url = "{0}/repos/{1}/{2}/commits".format(api_base, id, repo)
  r = requests.get(url)
  if r.status_code != 200: return "Request Failed"
  return r.json()

def get_summary(id):
  repos = get_repos(id)
  if repos == "Request Failed": return "Request Failed"
  result = "User: {0}\n".format(id)
  for repo in repos:
    commits = get_commits(id, repo["name"])
    if commits == "Request Failed": return "Request Failed"
    result += "Repo: {0} Number of commits: {1}\n".format(repo["name"], len(commits))
  return result[:-1]

if __name__ == '__main__':
  print get_summary("bzimmerm567")
