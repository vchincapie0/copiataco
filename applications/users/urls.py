from django.urls import path
from . import views

app_name='users_app'

urlpatterns = [
    path('',views.LogIn.as_view(),name='login'),
    path('list_user/',views.UsersListView.as_view(),name='list_user'),
    path('add_user/',views.UserRegisterView.as_view(),name='add_user'),
    path('edit_user/<pk>',views.UserUpdateView.as_view(),name='edit_user'),
    path('delete_user/<pk>',views.UserDeleteView.as_view(),name='delete_user'),
    path('logout/',views.LogOut.as_view(),name='logout'),

]