from django.urls import path
from . import views

urlpatterns = [
    path('', views.bot_list, name='bot_list'),               # HTML view
    path('api/bots/', views.bot_list_api, name='bot_list_api'),  # API view
]
