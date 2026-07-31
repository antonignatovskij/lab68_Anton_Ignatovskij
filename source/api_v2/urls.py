from django.urls import path
from api_v2.views import ArticlesView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = "api_v2"

urlpatterns = [
    path('list/', ArticlesView.as_view(), name='list'),
    path('add/<int:pk>/', ArticleCreateView.as_view(), name='add'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
]