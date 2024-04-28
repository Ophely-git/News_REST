from rest_framework import generics, views, viewsets
from rest_framework.response import Response

from .models import Category, News, Comments
from .serializers import CategorySerializer, NewsSerializer, CommentsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class CategoryAPIView(views.APIView):
#     def get(self, request):
#         category = Category.objects.all()
#         serializer_category = CategorySerializer(category, many=True).data
#
#         context = {
#             'category': serializer_category,
#         }
#         return Response(context)
#
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         context = {'post': serializer.data}
#         return Response(context)


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

        context = {
            'post': serializer.data
        }
        return Response(context)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Нет такой записи'})

        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({'error': 'Объект не найден'})

        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'update': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Запись не найдена'})

        news = News.objects.get(pk=pk)
        news.delete()

        return Response({'delete': f'Удалена запись {pk}'})


class CommentsAPIList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

