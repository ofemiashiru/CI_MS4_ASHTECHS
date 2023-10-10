from django.urls import path
from wishlist import views

urlpatterns = [
    path('<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
]