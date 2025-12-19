from django.db import models
from django.urls import reverse


class TagsModel(models.Model):
    tag_name = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.tag_name}"

class TaskModel(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        TagsModel,
        related_name="tasks"
    )

    class Meta:
        ordering = ("is_done", "-created_at", )

    def get_absolute_url(self):
        return reverse("todo_list:index")