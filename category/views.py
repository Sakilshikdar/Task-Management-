from django.shortcuts import render,redirect
from . import forms

# Create your views here.

def categoryHome(request):
    if request.method == "POST":
        post_form = forms.CategoryForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    else:
        post_form = forms.CategoryForm()
    return render(request,'categoryHome.html',{'data':post_form})




