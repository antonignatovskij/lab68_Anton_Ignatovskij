from django.conf import settings
from django.db import models

from articles.models import BaseModel


class CommentLike(BaseModel):
    comment = models.ForeignKey(
        "articles.Comment",
        related_name="likes",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comment_likes",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} → {self.comment}"