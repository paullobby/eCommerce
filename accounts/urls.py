from . import views
from .views import guest_register_view
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', views.home, name='accounts'),
    # path('treasure/', views.treasure, name='treasure'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/guest/', guest_register_view, name='guest'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]