from django.urls import path
from api_v2.views import ArticlesView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, CommentCreateView, CommentUpdateView, CommentDetailView, CommentListView, CommentDeleteView

app_name = "api_v2"

urlpatterns = [
    path('list/', ArticlesView.as_view(), name='list'),
    path('add/<int:pk>/', ArticleCreateView.as_view(), name='add'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('comments/list/<int:pk>/', CommentListView.as_view(), name='list'),
    path('comments/add/<int:pk>/', CommentCreateView.as_view(), name='add'),
    path('comments/update/<int:pk>/', CommentUpdateView.as_view(), name='update'),
    path('comments/detail/<int:pk>/', CommentDetailView.as_view(), name='detail'),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view(), name='delete'),
]