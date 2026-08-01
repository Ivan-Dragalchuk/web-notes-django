from django.shortcuts import render
from .forms import AddNewNote
from django.http import HttpResponseRedirect


def menu(request):
    return render(request, "main_app/index.html")

def add_(request):
    if request.method == "POST":
        form = AddNewNote(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/menu")
    else:
        form = AddNewNote()
    return render(request, "main_app/add.html", context={
        "form":form
    })