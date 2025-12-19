from django.urls import path

from todo_list.views import (IndexView,
                             TaskCreateView,
                             TaskUpdateView,
                             TaskDeleteView,
                             TaskToggleCompleteView,
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
    path("<int:pk>/toggle/", TaskToggleCompleteView.as_view(), name="task-toggle"),
    path("tags/", TagsListView.as_view(), name="tags-list"),

    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tags-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tags-delete"),
]

app_name = "todo_list"