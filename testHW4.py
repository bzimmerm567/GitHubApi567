import unittest
import mock
import json
import githubAPI

class TestHW4(unittest.TestCase):
  @mock.patch("githubAPI.get_repos")
  def test_get_reposA(self, mock_get_repos):
    mock_get_repos.return_value = json.load(open("getReposResponse.json"))
    self.assertNotEqual(githubAPI.get_repos("bzimmerm567"), "Request Failed", "A successful response should occur")

  @mock.patch("githubAPI.get_repos")
  def test_get_reposB(self, mock_get_repos):
    mock_get_repos.return_value = "Request Failed"
    self.assertEqual(githubAPI.get_repos("bzimmerm568"), "Request Failed", "An unsuccessful response should occur")

  @mock.patch('githubAPI.get_repos')
  def test_get_reposC(self, mock_get_repos):
    mock_get_repos.return_value = json.load(open("getReposResponse.json"))
    found = False
    for repo in githubAPI.get_repos("bzimmerm567"):
      if repo["name"] == "Triangle567": found = True
    self.assertEqual(found, True, "Triangle567 should be in the returned repos")

  @mock.patch("githubAPI.get_commits")
  def test_get_commitsA(self, mock_get_commits):
    mock_get_commits.return_value = json.load(open("getCommitsResponse.json"))
    self.assertNotEqual(githubAPI.get_commits("bzimmerm567", "Triangle567"), "Request Failed", "A successful response should occur")

  @mock.patch("githubAPI.get_commits")
  def test_get_commitsB(self, mock_get_commits):
    mock_get_commits.return_value = "Request Failed"
    self.assertEqual(githubAPI.get_commits("bzimmerm567", "Square567"), "Request Failed", "An unsuccessful response should occur")

  @mock.patch("githubAPI.get_commits")
  def test_get_commitsC(self, mock_get_commits):
    mock_get_commits.return_value = json.load(open("getCommitsResponse.json"))
    self.assertEqual(len(githubAPI.get_commits("bzimmerm567", "Triangle567")), 4, "This repo should have 4 commits")

if __name__ == '__main__':
  print "Running unit tests"
  unittest.main()
