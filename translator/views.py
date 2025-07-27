from django.shortcuts import render
from django.views.generic import ListView

from translator.models import Image


# Create your views here.
# def index(request):
#     return render(request,"translator/index.html")


class Index(ListView):
    model = Image
    context_object_name = "images"
    template_name = "translator/index.html"