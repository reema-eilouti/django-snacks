from django.urls import path

from . import views

# from .views import HomePageView, AboutView


urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.HomePageView.as_view(), name = 'home'),
    path('about', views.AboutView.as_view(), name = 'about'),
    path('snack_list', views.SnackListView.as_view(), name = 'snack_list'),
    path('snack_detail <int:pk>', views.SnackDetailView.as_view(), name = 'snack_detail'),
]
