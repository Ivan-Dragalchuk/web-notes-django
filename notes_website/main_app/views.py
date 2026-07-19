from django.shortcuts import render

# Create your views here.
def show_html(request):
    return render(request, "main_app/index.html")