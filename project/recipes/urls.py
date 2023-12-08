from django.urls import path, include
from . import views

app_name = 'recipes'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment')

]
