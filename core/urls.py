from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:client_id>/', views.edit, name='edit'),
    path('edit-auto/<int:client_id>/', views.edit_automovel, name='edit_auto'),
    path('edit-client/<int:client_id>/', views.edit_client, name='edit_client'),
    path('detail/<int:client_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('delete/<int:client_id>/', views.delete, name='delete'),
    path('print/<int:client_id>/',views.imprimir, name="imprimir")
]
