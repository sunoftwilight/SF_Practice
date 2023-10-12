from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:todo_pk>/', views.toggle, name='toggle'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]