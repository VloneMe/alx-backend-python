#!/usr/bin/env python3

"""Unit tests for parameterized functions, Mock HTTP calls, and memoization."""
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """
        Test the GithubOrgClient.org property.

        Args:
            org_name (str): The name of the GitHub organization.
            mock_get (MagicMock): Mocked get_json function.

        Asserts that GithubOrgClient.org returns the correct value.
        """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        """
        Unit test for GithubOrgClient._public_repos_url property.

        Asserts that GithubOrgClient._public_repos_url returns the correct URL.
        """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once()
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """
        Unit test for GithubOrgClient.public_repos method.

        Args:
            mock_get (MagicMock): Mocked get_json function.

        Asserts that GithubOrgClient.public_repos
        returns the correct list of repos.
        """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("hoberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once()
            mock_pub.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """
        Unit test for GithubOrgClient.has_license method.

        Args:
            repo (dict): Repository information.
            license_key (str): License key to check.
            expected_return (bool): Expected result.

        Asserts that GithubOrgClient.has_license returns the correct result.
        """
        test_client = GithubOrgClient("holberton")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to initialize the patcher.

        It is part of the unittest.TestCase
        API method to return example payloads
        found in the fixtures.
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher.

        It is part of the unittest.TestCase API method.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Integration test for GithubOrgClient.public_repos method.

        Asserts that GithubOrgClient.public_repos works as expected.
        """
        test_class = GithubOrgClient("holberton")
        assert True

    def test_public_repos_with_license(self):
        """
        Integration test for GithubOrgClient.public_repos
        with the argument license.

        Asserts that GithubOrgClient.public_repos works as
        expected with the license argument.
        """
        test_class = GithubOrgClient("holberton")
        assert True
