from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer, CommentSerializer
from articles.models import Article, Comment, article


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
        return Response({"id": pk},status=204)



class CommentListView(APIView):
    def get(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, id=pk)
        print(article.comments.all())
        serializer = CommentSerializer(article.comments.all(), many=True)
        return Response(serializer.data, status=200)

class CommentDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, id=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=200)

class CommentCreateView(APIView):
    def post(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, id=pk)
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, article=article)
        return Response(serializer.data, status=201)

class CommentUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, id=pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

class CommentDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, id=pk)
        comment.delete()
        return Response({"id": pk}, status=204)
