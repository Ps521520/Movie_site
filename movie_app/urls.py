
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login_register',views.login_register),
    path('movie_selection',views.movie_selection),
    path('data_page',views.data_page),
    path('registered',views.registered),
    path('profile',views.profile),
    path('history',views.history),
    path('recently_viewed',views.recently_viewed),
    path('logout',views.logout),

]
