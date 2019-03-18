from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('edit/<int:client_id>/', views.edit, name='edit'),
    path('detail/<int:client_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit_post/', views.edit_post, name='edit_post'),
    path('delete/<int:client_id>/', views.delete, name='delete'),
    path('create/save', views.saveclient, name='saveclient'),
]
