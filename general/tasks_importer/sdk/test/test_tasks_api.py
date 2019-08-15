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
from swagger_client.api.tasks_api import TasksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tasks_api.TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tasks(self):
        """Test case for create_tasks

        Post an array of tasks  # noqa: E501
        """
        pass

    def test_delete_task(self):
        """Test case for delete_task

        Delete a single tasks  # noqa: E501
        """
        pass

    def test_delete_tasks(self):
        """Test case for delete_tasks

        Delete an array of tasks  # noqa: E501
        """
        pass

    def test_get_task(self):
        """Test case for get_task

        Get a single task  # noqa: E501
        """
        pass

    def test_get_task_count(self):
        """Test case for get_task_count

        Get row count of query  # noqa: E501
        """
        pass

    def test_get_tasks(self):
        """Test case for get_tasks

        Get a list of tasks  # noqa: E501
        """
        pass

    def test_update_task(self):
        """Test case for update_task

        Modify/Create a task  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()