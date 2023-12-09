from django.shortcuts import render,redirect
from . import forms
from category.models import TaskCategory
from . import models


# Create your views here.

def taskHome(request):
    Category = (TaskCategory.objects.all())
    if request.method == "POST":
        post_form = forms.TaskForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    else:
        post_form = forms.TaskForm()
    return render(request,'taskHome.html',{'data':post_form,})


def edit_post(request,id):
    post = models.TaskModel.objects.get(pk=id)
    post_form = forms.TaskForm(instance = post)
    if request.method == "POST":
        post_form = forms.TaskForm(request.POST, instance= post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    return render(request,'taskHome.html',{'data':post_form})


def delete_post(request,id):

    post = models.TaskModel.objects.get(pk=id)
    post.delete()
    return redirect('homepage')