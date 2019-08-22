from django.urls import path, re_path
from . import views

urlpatterns = [
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]