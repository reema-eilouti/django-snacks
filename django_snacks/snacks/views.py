from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the snacks index. Go to /home/ to view the main page of website.")

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'