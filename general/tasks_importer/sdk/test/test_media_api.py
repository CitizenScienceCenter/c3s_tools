# coding: utf-8

"""
    CCCS

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.media_api import MediaApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.media_api.MediaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_medium(self):
        """Test case for create_medium

        """
        pass

    def test_delete_medium(self):
        """Test case for delete_medium

        Delete all media files related to  source  # noqa: E501
        """
        pass

    def test_get_for_source(self):
        """Test case for get_for_source

        Query media for a specific task or project  # noqa: E501
        """
        pass

    def test_get_media(self):
        """Test case for get_media

        """
        pass

    def test_get_medium(self):
        """Test case for get_medium

        Get a single file  # noqa: E501
        """
        pass

    def test_update_medium(self):
        """Test case for update_medium

        Put a single file  # noqa: E501
        """
        pass

    def test_upload(self):
        """Test case for upload

        """
        pass


if __name__ == '__main__':
    unittest.main()