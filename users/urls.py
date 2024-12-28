from django.urls import path
from .views import register, user_login, home, create_customer  # Include create_customer view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path('customer/add/', create_customer, name='add_customer'),  # URL for adding a customer
]
