from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ContactsPageView, ProductDetailView, ProductListView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [

    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),

    path('create/', ProductCreateView.as_view(), name='create'),
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
