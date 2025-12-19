from django.db import models
from django.urls import reverse


class TagsModel(models.Model):
    tag_name = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.tag_name}"

    def get_absolute_url(self):
        return reverse("todo_list:tags-list")

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

    def __str__(self):
        tags = ", ".join(tag.tag_name for tag in self.tags.all())
        return f"Task: {self.content}, {self.created_at}, {self.is_done}, {tags}"

    def get_absolute_url(self):
        return reverse("todo_list:index")