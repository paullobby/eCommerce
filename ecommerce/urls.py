"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from carts.views import cart_detail_api_view
from accounts.views import guest_register_view

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('analytics/', views.analytics, name='analytics'),
    path('accounts/', include('accounts.urls')),
    #path('register/guest/', guest_register_view, name='guest_url'),
    path('checkout/address/create', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/',  checkout_address_reuse_view, name='checkout_address_reuse'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('carts/', include('carts.urls', namespace='carts')),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<pk>/', ProductFeaturedDetailView.as_view()),
    # path('products/', ProductListView.as_view()),
    # path('products-fbv/', product_list_view),
    # #path('products/<pk>/', ProductDetailView.as_view()),
    # path('products/<slug>/', ProductDetailSlugView.as_view()),
    # path('products-fbv/<pk>/', product_detail_view),  #regular expresions to get each id for product
]


if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
