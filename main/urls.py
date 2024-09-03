from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomeView, name='home'),
    path('registration/', views.RegistrationView, name='registration'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),

]
