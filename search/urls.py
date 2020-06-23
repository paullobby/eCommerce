from django.urls import path, include

from .views import (
        SearchProductView
        )



urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]
app_name = 'search'