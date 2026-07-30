from django.views.generic.base import TemplateView


class WebappCalculateView(TemplateView):
    template_name = "webapp/index.html"