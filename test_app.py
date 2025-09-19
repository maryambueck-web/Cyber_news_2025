#!/usr/bin/env python3
"""
Simple tests for the Cyber News Tracker application
"""

import unittest
import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(__file__))

import app as main_app


class CyberNewsTrackerTestCase(unittest.TestCase):
    """Test cases for the Cyber News Tracker application"""

    def setUp(self):
        """Set up test client"""
        self.app = main_app.create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_page(self):
        """Test that the home page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Latest Cybersecurity News', response.data)

    def test_search_page(self):
        """Test that the search page loads successfully"""
        response = self.client.get('/search')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search Cybersecurity News', response.data)

    def test_admin_login_page(self):
        """Test that the admin login page loads successfully"""
        response = self.client.get('/admin/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Login', response.data)

    def test_api_endpoint(self):
        """Test that the API endpoint returns JSON"""
        response = self.client.get('/api/news')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_search_with_query(self):
        """Test search functionality with a query"""
        response = self.client.get('/search?q=ransomware')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search Results for "ransomware"', response.data)

    def test_admin_access_without_login(self):
        """Test that admin dashboard redirects without login"""
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_404_error(self):
        """Test that 404 errors are handled properly"""
        response = self.client.get('/nonexistent-page')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()