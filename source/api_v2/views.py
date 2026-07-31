from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer
from articles.models import Article


# Create your views here.

class ArticlesView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleCreateView(APIView):
    def post(self, request, *args, **kwargs):
        tags = request.data.pop('tags', [])
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, tags=tags)
        return Response(serializer.data, status=201)


class ArticleUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, id=pk)
        tags = request.data.pop('tags', [])
        serializer = ArticleSerializer(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        serializer.save(tags=tags)
        return Response(serializer.data, status=200)

class ArticleDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=200)

class ArticleDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, id=pk)
        article.delete()
        return Response({"id": pk, "message": "Статья удалена"},status=204)



