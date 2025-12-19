from django.urls import path

from todo_list.views import (IndexView,
                             TaskCreateView,
                             TaskUpdateView,
                             TaskDeleteView,
                             task_complete,
                             task_not_complete,
                             TagsListView,
                             TagCreateView,
                             TagUpdateView,
                             TagDeleteView,
                             )


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/complete/", task_complete, name="task-complete"),
    path("<int:pk>/not-complete/", task_not_complete, name="task-not-complete"),
    path("tags/", TagsListView.as_view(), name="tags-list"),

    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tags-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tags-delete"),
]

app_name = "todo_list"