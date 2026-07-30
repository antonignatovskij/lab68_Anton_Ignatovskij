from django.urls import path
from webapp.views import WebappCalculateView

app_name = "webapp"

urlpatterns = [
    path('', WebappCalculateView.as_view(), name='api_add'),
]