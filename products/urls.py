from django.urls import path
from products import views

urlpatterns = [
    path('', views.see_all_products, name='products'),
    # path('accessories', views.see_all_accessories, name='accessories'),
    path('<product_id>', views.see_product_details, name='product_details')
]
