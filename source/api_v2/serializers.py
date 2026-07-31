from rest_framework import serializers
from django.core.exceptions import ValidationError
from articles.models.article import Article
from articles.models.comments import Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "content", "author", "status", "tags", "likes", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

        def validate(self, data):
            return super().validate(data)

        def validate_title(self, value):
            if len(value) < 5:
                raise ValidationError("Title must be at least 5 characters")
            return value
