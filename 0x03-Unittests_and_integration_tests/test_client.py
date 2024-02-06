#!/usr/bin/env python3
"""Unittest module for GithubOrgClient."""

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized

import client
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """
        Test the GithubOrgClient.org method.

        Args:
            org_name (str): The name of the GitHub organization.
            mock_json (Mock): Mocked get_json function.

        Asserts that the GithubOrgClient.org method makes the correct API call.
        """
        gc = GithubOrgClient(org_name)
        gc.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
