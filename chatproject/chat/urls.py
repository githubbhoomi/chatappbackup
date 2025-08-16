# from django.urls import path
# from . import views

# urlpatterns = [
#     path('<str:room_name>/', views.room, name='room'),
# ]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('index', views.index, name='index'),  # trailing slash!
   path('register/', views.register_view, name='register'),
    # path('login/', views.login_view, name='login'),
    path('', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index'),  # trailing slash!
    path('chat/<str:username>/', views.chat_with_user, name='chat_with_user'),
    path('chat_room/', views, name='dashboard')

   
]

