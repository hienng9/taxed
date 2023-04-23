from django.urls import path
from . import views


app_name = "base"
urlpatterns = [
    path('', views.front_page, name="front-page"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('update-user/', views.updateUser, name="update-user"),

]
# 
