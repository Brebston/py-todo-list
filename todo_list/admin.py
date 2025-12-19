from django.contrib import admin

from todo_list.models import TagsModel, TaskModel


@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = [
        "content",
        "created_at",
        "deadline",
        "is_done",
    ]
    list_filter = [
        "is_done",
    ]
    search_fields = [
        "content",
    ]

@admin.register(TagsModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = [
        "tag_name",
    ]
    list_filter = [
        "tag_name",
    ]
    search_fields = [
        "tag_name",
    ]