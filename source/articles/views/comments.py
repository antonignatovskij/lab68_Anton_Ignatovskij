from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from articles.forms import CommentForm
from articles.models import Article, Comment


class CommentCreateView(CreateView):
    template_name = "comments/comment_create.html"
    form_class = CommentForm
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        artice = get_object_or_404(Article, pk=self.kwargs["pk"])
        form.instance.article = artice
        return super().form_valid(form)

class CommentLikeView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(
            Comment, pk=self.kwargs["pk"])
        if comment.likes.filter(pk=request.user.pk).exists():
            comment.likes.remove(request.user)
            liked = False
        else:
            comment.likes.add(request.user)
            liked = True
        return JsonResponse({
            "liked": liked,
            "likes_count": comment.likes.count()
        })
#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(Comment, pk=self.kwargs["pk"])
#         comment_like = CommentLike.objects.filter(comment=comment,user=request.user).first()
#         if comment_like:
#             comment_like.delete()
#             liked = False
#         else:
#             CommentLike.objects.create(comment=comment,user=request.user)
#             liked = True
#         return JsonResponse({"liked": liked, "likes_count": comment.likes.count()
#         })

