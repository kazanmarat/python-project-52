from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = None
    a.hello()
    return HttpResponse('Hello, world!')