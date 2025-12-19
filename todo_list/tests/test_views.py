from http.client import responses

from django.test import Client, TestCase
from django.urls import reverse

from todo_list.models import TagsModel, TaskModel

TAGS_URL = reverse("todo_list:tags-list")

class TagsTest(TestCase):
    def test_tags_create(self):
        TagsModel.objects.create(tag_name="work")
        TagsModel.objects.create(tag_name="shop")
        response = self.client.get(TAGS_URL)
        self.assertEqual(response.status_code, 200)
        tags = TagsModel.objects.all()
        self.assertEqual(
            list(response.context["tags_list"]),
            list(tags),
        )
        self.assertTemplateUsed(response, "todo_list/tags_list.html")


class TaskTest(TestCase):
    def test_task_create(self):
        tag = TagsModel.objects.create(tag_name="test")
        task = TaskModel.objects.create(
            content="test",
            is_done=False,
        )
        task.tags.add(tag)
        response = self.client.get(reverse("todo_list:index"))
        tasks = TaskModel.objects.all()
        self.assertEqual(
            list(response.context["tasks_list"]),
            list(tasks),
        )
        self.assertTemplateUsed(response, "todo_list/index.html")