from django.urls import path
from reviews import views

urlpatterns = [
    path('add_review/<product_id>/', views.add_review, name='add_review'),
]