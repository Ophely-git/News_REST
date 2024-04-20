from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from django.forms import model_to_dict

from .models import Category, News
from .serializers import CategorySerializer, NewsSerializer


# class CategoryAPIList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryAPIView(views.APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer_category = CategorySerializer(category, many=True).data

        context = {
            'category': serializer_category,
        }
        return Response(context)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        context = {'post': serializer.data}
        return Response(context)


class NewsAPIView(views.APIView):

    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True).data

        context = {
            'news': serializer
        }
        return Response(context)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        context = {'post': serializer.data}
        return Response(context)