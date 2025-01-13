# coding: utf-8

"""
    TickTick API

    [TickTick](https://ticktick.com/) TODO task manager.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from custom_components.ticktick_todo.pyticktick.openapi_client.models.project import Project  # noqa: E501

class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Project:
        """Test Project
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Project`
        """
        model = Project()  # noqa: E501
        if include_optional:
            return Project(
                id = '',
                name = '',
                color = '',
                sort_order = 56,
                closed = '',
                group_id = '',
                view_mode = '',
                permission = '',
                kind = ''
            )
        else:
            return Project(
        )
        """

    def testProject(self):
        """Test Project"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
