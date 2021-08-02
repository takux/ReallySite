from django.urls import path, include
from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.index),
    path('tags/<slug:slug>/', views.tags),

    path('<slug:pk>/', views.article, name="article"),

    path('<slug:pk>/like/', views.like),
]