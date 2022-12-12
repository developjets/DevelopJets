from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addContactQuerry/', views.addContactQuerry, name='addContactQuerry'),
    path('projects/', views.projects, name='projects'),
    path('projects/projectDetail/<int:id>', views.projectDetail, name = 'projectDetail'),
]