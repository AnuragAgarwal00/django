from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('login/', views.user_login, name="user_login"),
    # path('logout/', auth_view.LogoutView(), name='logout'),
    path('register/', views.register, name="register"),
    path('address/', views.all_address, name='all_address'),
    path('address/<int:address_id>/', views.particular_address, name="particular_address"),
    path('address/add_new_address/', views.create_address, name="create_address")
]
