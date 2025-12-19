import datetime

from django.test import TestCase

from todo_list.models import TagsModel, TaskModel


class ModelTests(TestCase):
    def test_tags_str(self):
        tag = TagsModel.objects.create(tag_name="test")
        self.assertEqual(str(tag), tag.tag_name)

    def test_tasks_str(self):
        tag = TagsModel.objects.create(tag_name="test")
        tasks = TaskModel.objects.create(
            content="test",
            is_done=False,
        )
        tasks.tags.add(tag)
        self.assertEqual(
            str(tasks),
            f"Task: {tasks.content}, {tasks.created_at}, {tasks.is_done}, {tag.tag_name}",
        )
