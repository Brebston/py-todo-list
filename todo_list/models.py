from django.db import models


class TagsModel(models.Model):
    name = models.CharField(max_length=20)


class TaskModel(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        TagsModel,
        related_name="tasks"
    )