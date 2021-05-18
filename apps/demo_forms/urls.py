from django.urls import path, include
from apps.demo_forms import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('register', views.register, name = "register"),
    path('login', views.login, name ="login"),
    path('logout', views.logout, name = "logout"),
    path('hobbie', views.hobbie),
]