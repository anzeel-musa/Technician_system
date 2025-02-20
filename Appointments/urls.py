from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name= "index"),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
]
