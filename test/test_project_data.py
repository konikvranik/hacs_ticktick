# coding: utf-8

"""
    TickTick API

    [TickTick](https://ticktick.com/) TODO task manager.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from custom_components.ticktick_todo.pyticktick.openapi_client.models.project_data import ProjectData  # noqa: E501

class TestProjectData(unittest.TestCase):
    """ProjectData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectData:
        """Test ProjectData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectData`
        """
        model = ProjectData()  # noqa: E501
        if include_optional:
            return ProjectData(
                project = custom_components.ticktick_todo.pyticktick.openapi_client.models.project.Project(
                    id = '', 
                    name = '', 
                    color = '', 
                    sort_order = 56, 
                    view_mode = 'list', 
                    kind = 'TASK', 
                    closed = True, 
                    group_id = '', 
                    permission = '', ),
                tasks = [
                    custom_components.ticktick_todo.pyticktick.openapi_client.models.task.Task(
                        id = '', 
                        task_id = '', 
                        project_id = '', 
                        title = '', 
                        completed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 0, 
                        is_all_day = True, 
                        content = '', 
                        desc = '', 
                        due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        items = [
                            custom_components.ticktick_todo.pyticktick.openapi_client.models.checklist_item.ChecklistItem(
                                id = '', 
                                title = '', 
                                completed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                is_all_day = True, 
                                sort_order = 234444, 
                                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                time_zone = null, )
                            ], 
                        priority = 0, 
                        reminders = ["TRIGGER:P0DT9H0M0S","TRIGGER:PT0S"], 
                        repeat_flag = 'RRULE:FREQ=DAILY;INTERVAL=1', 
                        sort_order = 12345, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_zone = null, )
                    ],
                columns = [
                    custom_components.ticktick_todo.pyticktick.openapi_client.models.column.Column(
                        id = '', 
                        project_id = '', 
                        name = '', 
                        sort_order = 56, )
                    ]
            )
        else:
            return ProjectData(
        )
        """

    def testProjectData(self):
        """Test ProjectData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
