from django.contrib.auth import get_user_model
from django.db import models

from articles.models import BaseModel


class Comment(BaseModel):
    article = models.ForeignKey('articles.Article', related_name='comments', on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')
    likes = models.ManyToManyField(get_user_model(), related_name="liked_comments", blank=True)