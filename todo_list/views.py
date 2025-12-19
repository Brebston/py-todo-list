from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskForm
from todo_list.models import TaskModel


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


def task_complete(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_done = True
    task.save()
    return redirect("todo_list:index")

def task_not_complete(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_done=False
    task.save()
    return redirect("todo_list:index")