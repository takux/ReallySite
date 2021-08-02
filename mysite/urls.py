from django.urls import path
from django.contrib.auth.views import LogoutView
from mysite import views

app_name = "mysite"

urlpatterns = [
    path('bs-home/', views.index, name="bs-home"),
    path('', views.landing, name="home"),


    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),
    path('mypage/', views.MypageView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('pay/', views.PayView.as_view()),

    path('ping/', views.ping),
]