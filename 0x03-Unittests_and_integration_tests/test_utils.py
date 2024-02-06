#!/usr/bin/env python3
"""Unit tests for parameterized functions, Mock HTTP calls, and memoization."""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function with various inputs.

        Parameters:
        - nested_map (dict): The nested dictionary to traverse.
        - path (tuple): The path to the desired value within the nested_map.
        - expected_result: The expected result when accessing the nested_map.

        The function should retrieve values from a nested map based on the provided path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map function when KeyError is expected.

        Parameters:
        - nested_map (dict): The nested dictionary to traverse.
        - path (tuple): The path to a key that does not exist in the nested_map.

        The function should raise a KeyError when attempting to access a non-existing key.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])

class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.get_json')  # Ensure this path is correct
    def test_get_json(self, test_url, test_payload, mock_get_json):
        """
        Test get_json function with different URLs and payloads.

        Parameters:
        - test_url (str): The URL for the HTTP request.
        - test_payload (dict): The expected payload returned by the mocked HTTP call.
        - mock_get_json (MagicMock): The mocked get_json function.

        The function should retrieve JSON data from the specified URL.
        """
        mock_get_json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self):
        """
        Test the memoize decorator for caching and method call count.

        The test class TestClass has a memoized property (a_property) that calls
        a_method. This test ensures that a_property is memoized and a_method is
        called only once.
        """
        class TestClass:
            """TestClass class."""
            def a_method(self):
                """Return a constant value."""
                return 42

            @memoize
            def a_property(self):
                """Memoized property."""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock_method.assert_called_once()
