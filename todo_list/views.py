from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo_list.forms import TaskForm
from todo_list.models import TagsModel, TaskModel


class IndexView(generic.ListView):
    model = TaskModel
    context_object_name = "tasks_list"
    template_name = "todo_list/index.html"


class TaskCreateView(generic.CreateView):
    model = TaskModel
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = TaskModel
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = TaskModel
    context_object_name = "task_list"
    template_name = "todo_list/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:index")


class TagsListView(generic.ListView):
    model = TagsModel
    context_object_name = "tags_list"
    template_name = "todo_list/tags_list.html"


class TagCreateView(generic.CreateView):
    model = TagsModel
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = TagsModel
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags-list")


class TagDeleteView(generic.DeleteView):
    model = TagsModel
    context_object_name = "tags_list"
    template_name = "todo_list/tags_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tags-list")


class TaskToggleCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(TaskModel, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo_list:index")