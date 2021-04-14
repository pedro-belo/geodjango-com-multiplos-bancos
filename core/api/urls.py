from django.urls import path
from core.api import views

urlpatterns = [
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail')
]
