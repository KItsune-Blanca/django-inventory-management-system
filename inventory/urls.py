from django.urls import path
from .views import (home, add_product, update_product, delete_product)
 

urlpatterns = [
    path('', home, name='home'),

    path(
        'add-product/',
        add_product,
        name='add_product'
    ),

    path(
        'update-product/<int:pk>/',
        update_product,
        name='update_product'
    ),
    
    path(
        'delete-product/<int:pk>/',
        delete_product,
        name='delete_product'
    ),
]