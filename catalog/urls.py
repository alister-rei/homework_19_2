from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomepageListView, ContactsPageView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomepageListView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
