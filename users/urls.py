from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin_view, name='signin'),
    path('signin/authenticate/', views.authenticate_user, name='authenticate_user'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('signup/register/', views.register_user, name='register_user'),
]
