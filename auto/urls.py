from django.urls import path
from auto import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book/', views.book, name="book"),
    path('success/', views.success, name="success"),
]
