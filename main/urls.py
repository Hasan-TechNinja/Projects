from django.contrib import admin
from django.urls import path
from . import views
# from .views import CustomPasswordChangeView, CustomPasswordChangeDoneView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomeView, name='home'),
    path('registration/', views.RegistrationView, name='registration'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
]
