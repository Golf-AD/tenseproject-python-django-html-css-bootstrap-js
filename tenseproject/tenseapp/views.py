from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView #for pictures

# Create your views here.
def base(request):
    return render(request,"base.html")

def index(request):
    return render(request,"index.html")
    
def present(request):
    return render(request,"present.html")

def past(request):
    return render(request,"past.html")

def future(request):
    return render(request,"future.html")

def about(request):
    return render(request,"about.html")

class HomeView(TemplateView):
    template_name = 'index.html'