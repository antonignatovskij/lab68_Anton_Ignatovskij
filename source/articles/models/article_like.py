from django.conf import settings
from django.db import models

from articles.models import BaseModel


class ArticleLike(BaseModel):
    article = models.ForeignKey(
        "articles.Article",
        related_name="likes",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="article_likes",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} → {self.article}"