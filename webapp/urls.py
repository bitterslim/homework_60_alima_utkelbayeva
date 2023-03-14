from django.urls import path

from webapp.views.index import IndexView
from webapp.views.product import ProductDeleteView, ProductDetailView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),

]
