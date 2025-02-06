from django.urls import path
from . import views

urlpatterns = [
    path('event/create/', views.event_create_view, name='event_create_view'),
    path('event/store/', views.event_create, name='event_store'),
]
