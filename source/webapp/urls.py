from django.urls import path
from webapp.views import WebappCalculateView

app_name = "webapp"

urlpatterns = [
    path('calculate/', WebappCalculateView.as_view(), name='calculate'),
]