import statistics
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from user.forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('anasayfa/', views.index),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='girisYap.html',
         authentication_form=LoginForm), name='login'),

]
