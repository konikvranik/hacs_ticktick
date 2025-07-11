import re

import pyticktick
from homeassistant.components.todo import TodoItem, TodoItemStatus


class TaskMapper:
    @staticmethod
    def task_to_todo_item(task_response: pyticktick.Task) -> TodoItem:
        return TodoItem(
            uid=task_response.id,
            summary=task_response.title,
            description=task_response.desc,
            status=TaskMapper._task_status_to_todo_item_status(task_response),
            due=task_response.due_date,
        )

    @staticmethod
    def todo_item_to_task(project_id: str, todo_item: TodoItem) -> pyticktick.Task:
        priority = TaskMapper._resolve_priority(todo_item)
        task = pyticktick.Task(
            id=todo_item.uid,
            title=todo_item.summary,
            desc=todo_item.description,
            status=TaskMapper._todo_item_status_to_task_status(todo_item),
            dueDate=todo_item.due,
            projectId=project_id,
            priority=priority,
        )
        return task

    @staticmethod
    def merge_todo_item_and_task_response(todo_item: TodoItem, task_response: pyticktick.Task) -> pyticktick.Task:
        priority = TaskMapper._resolve_priority(todo_item)
        task_response.task_id = todo_item.uid
        task_response.status = TaskMapper._todo_item_status_to_task_status(todo_item)
        task_response.title = todo_item.summary
        task_response.desc = todo_item.description
        task_response.due_date = todo_item.due
        if priority:
            task_response.priority = priority
        return task_response

    @staticmethod
    def _task_status_to_todo_item_status(task_response: pyticktick.Task) -> TodoItemStatus | None:
        if task_response.status == 0:
            return TodoItemStatus.NEEDS_ACTION
        elif task_response.status == 2:
            return TodoItemStatus.COMPLETED
        else:
            return None

    @staticmethod
    def _todo_item_status_to_task_status(todo_item: TodoItem) -> int:
        if todo_item.status == TodoItemStatus.COMPLETED:
            return 2
        else:
            return 0

    @staticmethod
    def task_response_to_task_request(response: pyticktick.Task) -> pyticktick.Task:
        return pyticktick.Task(
            title=response.title,
            isAllDay=response.is_all_day,
            content=response.content,
            desc=response.desc,
            items=response.items,
            priority=response.priority,
            reminders=response.reminders,
            repeatFlag=response.repeat_flag,
            sortOrder=response.sort_order,
            startDate=response.start_date,
            timeZone=response.time_zone,
            id=response.id,
            projectId=response.project_id,
            completedTime=response.completed_time,
            status=response.status,
        )

    @staticmethod
    def _resolve_priority(todo_item):
        result = re.compile("^(!*)\\s*(.*)$").match(todo_item.summary)
        todo_item.summary = result.group(2)
        priority = len(result.group(1)) * 2 - 1
        return 0 if todo_item.summary.startswith(" ") else max(priority, 0)
