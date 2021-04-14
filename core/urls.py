from django.urls import path

from core import views
from core.api.urls import urlpatterns as api_urls

app_name = 'core'

urlpatterns = [

    # marketplace
    path('novo', views.MarketplaceCreateView.as_view(), name='marketplace-create'),
    path('remover/<int:pk>', views.MarketplaceDeleteView.as_view(), name='marketplace-delete'),

    path('mapa', views.MapView.as_view(), name='map'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard')
]

urlpatterns += api_urls
