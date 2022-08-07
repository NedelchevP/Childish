from onlinestore import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename="products")
router.register(r'order', views.OrdersViewSet, basename="orders")


urlpatterns = [
    path('', include(router.urls)),
    path('api/stats/', views.ApiStats.as_view({'post': 'stats'}))
]