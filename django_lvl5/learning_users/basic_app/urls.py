from django.urls import path
from . import views


app_name = "basic_app"
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('login/', views.user_login, name="login"),
    path('special/', views.special, name="special")
]
