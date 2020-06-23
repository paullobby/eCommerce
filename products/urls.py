

from django.urls import path, include

from .views import (
        ProductListView, 
        #product_list_view, 
        #ProductDetailView, 
        #product_detail_view,
        #ProductFeaturedListView,
        #ProductFeaturedDetailView,
        ProductDetailSlugView
        )



urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug>/', ProductDetailSlugView.as_view(), name='detail'),
]
app_name = 'products'
