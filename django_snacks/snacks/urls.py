from django.urls import path

from . import views

# from .views import HomePageView, AboutView


urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.HomePageView.as_view(), name = 'home'),
    path('about', views.AboutView.as_view(), name = 'about'),
    path('snack_list', views.SnackListView.as_view(), name = 'snack_list'),
    path('snack_detail/<int:pk>', views.SnackDetailView.as_view(), name = 'snack_detail'),
    path('snack_create', views.SnackCreateView.as_view(), name='snack_create'),
    path('update_snack/<int:pk>', views.SnackUpdateView.as_view(), name = 'snack_update'),
    path('delete_snack/<int:pk>', views.SnackDeleteView.as_view(), name = 'snack_delete'),
]
