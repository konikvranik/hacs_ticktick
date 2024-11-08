# coding: utf-8

"""
    TickTick API

    [TickTick](https://ticktick.com/) TODO task manager.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.task import Task

class TestTask(unittest.TestCase):
    """Task unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Task:
        """Test Task
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Task`
        """
        model = Task()
        if include_optional:
            return Task(
                title = '',
                is_all_day = True,
                content = '',
                desc = '',
                due_date = None,
                items = [
                    openapi_client.models.checklist_item.ChecklistItem(
                        id = '', 
                        title = '', 
                        status = null, 
                        completed_time = null, 
                        is_all_day = True, 
                        sort_order = 234444, 
                        start_date = null, 
                        time_zone = null, )
                    ],
                priority = ERROR_TO_EXAMPLE_VALUE,
                reminders = ["TRIGGER:P0DT9H0M0S","TRIGGER:PT0S"],
                repeat_flag = 'RRULE:FREQ=DAILY;INTERVAL=1',
                sort_order = 12345,
                start_date = None,
                time_zone = None
            )
        else:
            return Task(
        )
        """

    def testTask(self):
        """Test Task"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
