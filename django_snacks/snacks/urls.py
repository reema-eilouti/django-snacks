from django.urls import path

from . import views

# from .views import HomePageView, AboutView


urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.HomePageView.as_view(), name = 'home'),
    path('about', views.AboutView.as_view(), name = 'about'),
]
