
from django.urls import path
from . import views

# from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    path('logout/',views.logout, name='logout'),
    path('register/', views.register, name='register'),
    
    path('login/', views.login, name='login'),
    path('search/', views.search, name='search'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update, name='update'),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
  
] 
