from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup-page'),
    path('signin/', views.signin, name='signin-page'),
    path('signout/', views.signout, name='signout-page'),
    path('/', views.signup, name='signup-page'),
]
