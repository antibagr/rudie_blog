# from django.shortcuts import render
#
# # Create your views here.
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the articles index.")


from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics


class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
