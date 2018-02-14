import unittest

from githubAPI import get_repos, get_commits

class TestHW4(unittest.TestCase):
  def test_get_reposA(self):
    self.assertNotEqual(get_repos("bzimmerm567"), "Request Failed", "A successful response should occur")

  def test_get_reposB(self):
    self.assertEqual(get_repos("bzimmerm568"), "Request Failed", "An unsuccessful response should occur")

  def test_get_reposC(self):
    found = False
    for repo in get_repos("bzimmerm567"):
      if repo["name"] == "Triangle567": found = True
    self.assertEqual(found, True, "Triangle567 should be in the returned repos")

  def test_get_commitsA(self):
    self.assertNotEqual(get_commits("bzimmerm567", "Triangle567"), "Request Failed", "A successful response should occur")

  def test_get_commitsB(self):
    self.assertEqual(get_commits("bzimmerm567", "Square567"), "Request Failed", "An unsuccessful response should occur")

  def test_get_commitsC(self):
    self.assertEqual(len(get_commits("bzimmerm567", "Triangle567")), 4, "This repo should have 4 commits")

if __name__ == '__main__':
    print "Running unit tests"
    unittest.main()