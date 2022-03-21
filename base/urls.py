from django.urls import path
from . import views

app_name='base'
urlpatterns =[
    path('',views.landing,name='landing'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('bikes/',views.bikes,name='bikes'),
    path('bikes/<str:pk>/',views.details,name='bike-details'),
    path('update-bike/<str:pk>/',views.update,name='update-bike'),
    path('delete-bike/<str:pk>/',views.delete_bike,name='delete-bike'),
    path('update-details/<str:pk>/',views.update_details,name='update-bike-data'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('customer/<str:pk>/update/',views.update_customer,name='update-customer'),
    path('create_order/<str:pk>/',views.create_order,name='create-order'),
    path('update-order/<str:pk>/',views.update_order,name='update-order'),
    path('delete-order/<str:pk>/',views.delete_order,name='delete-order')
]