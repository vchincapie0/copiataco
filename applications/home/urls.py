from django.urls import path
from . import views

app_name='home_app'

urlpatterns = [
    path('home/',views.Home.as_view(),name='home'),

]