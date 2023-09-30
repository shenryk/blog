
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "posts_home"),
    # path('posts/', views.index, name="index"),
    path('members/',views.members,name="members")
]
    
