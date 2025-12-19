from django.urls import path

from todo_list.views import (IndexView,
                             TaskCreateView,
                             TaskUpdateView,
                             TaskDeleteView,
                             task_complete,
                             task_not_complete)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/complete/", task_complete, name="task-complete"),
    path("<int:pk>/not-complete/", task_not_complete, name="task-not-complete"),
]

app_name = "todo_list"