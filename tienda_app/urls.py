from django.urls import path
from .api.views import CompraAPIView, ProductosAPIView
from .api.views import CompraAPIView
from .views import CompraView, CompraRapidaView, compra_rapida_fbv

urlpatterns = [
    path('compra/<int:libro_id>/', CompraView.as_view(), name='finalizar_compra'),
    path('api/v1/comprar/', CompraAPIView.as_view(), name='api_comprar'),
    path('api/v1/productos/', ProductosAPIView.as_view(), name='api_productos'),
    # Tutorial 01
    path('compra-rapida-fbv/<int:libro_id>/', compra_rapida_fbv, name='compra_rapida_fbv'),
    path('compra-rapida/<int:libro_id>/', CompraRapidaView.as_view(), name='compra_rapida'),
]