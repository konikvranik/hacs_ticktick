# coding: utf-8

"""
    TickTick API

    [TickTick](https://ticktick.com/) TODO task manager.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from custom_components.ticktick_todo.pyticktick.openapi_client.models.open_v1_project_project_id_task_task_id_complete_post_request import OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest

class TestOpenV1ProjectProjectIdTaskTaskIdCompletePostRequest(unittest.TestCase):
    """OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest:
        """Test OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest`
        """
        model = OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest()
        if include_optional:
            return OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest(
                project_id = '',
                task_id = ''
            )
        else:
            return OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest(
        )
        """

    def testOpenV1ProjectProjectIdTaskTaskIdCompletePostRequest(self):
        """Test OpenV1ProjectProjectIdTaskTaskIdCompletePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
