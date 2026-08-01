from django.shortcuts import render
from .forms import AddNewNote
from .models import AddNewNoteModel
from django.http import HttpResponseRedirect


def menu(request):
    notes = AddNewNoteModel.objects.all()
    return render(request, "main_app/index.html", context={
        "notes":notes,
    })

def add_(request):
    if request.method == "POST":
        form = AddNewNote(request.POST)
        if form.is_valid():
            addnote = AddNewNoteModel(
            title = form.cleaned_data["title"],
            describe = form.cleaned_data["describe"],
            )
            addnote.save()
            return HttpResponseRedirect("/menu")
    else:
        form = AddNewNote()
    return render(request, "main_app/add.html", context={
        "form":form
    })