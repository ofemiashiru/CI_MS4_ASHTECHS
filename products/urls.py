from django.urls import path
from products import views

urlpatterns = [
    path('', views.see_all_products, name='products'),
    path('<int:product_id>/', views.see_product_details, name='product_details'),
    path('add_product', views.add_product, name='add_product')
]
