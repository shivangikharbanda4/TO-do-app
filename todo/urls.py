from django.urls import path
from . import views
urlpatterns = [
    path('', views.add_list, name='add_list'),
]
