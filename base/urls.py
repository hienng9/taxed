from django.urls import path
from . import views


app_name = "base"
urlpatterns = [
    path('', views.front_page, name="front-page"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('contact/', views.contact_view, name="contact"),
    path('thank-you', views.contact_view, name="thank-you"),
    path('profile/', views.home, name="home"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('create-invoice/', views.createInvoice, name="create-invoice"),
    path('update-user/', views.updateUser, name="update-user"),
    path('calculate-salary/', views.calculate_salary, name="calculate-salary"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    # path('room/<str:pk>/', views.room, name="room"),
    # path('chat-bot/', views.chat_bot, name="chat_view"),
    
    # path('create-room/', views.createRoom, name="create-room"),
    # path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    # path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    # path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
]
# 
