from django.urls import path
from . import views



urlpatterns = [
    path('login', views.login),
    path('dashboard', views.index), 
    path('reg', views.reg), 
    path('profile', views.profile)
]

