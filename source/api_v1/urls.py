from django.urls import path
from api_v1.views import CalculateView, get_token_view

app_name = "api_v1"

urlpatterns = [
    path('add/', CalculateView.as_view(), name='api_add'),
    path('subtract/', CalculateView.as_view(), name='api_subtract'),
    path('multiply/', CalculateView.as_view(), name='api_multiply'),
    path('divide/', CalculateView.as_view(), name='api_divide'),
    path('token/', get_token_view, name='token'),
]