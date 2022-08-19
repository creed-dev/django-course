from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News, Category
from .serializers import NewsSerializer


class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsUpdateAPIView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# class NewsAPIView(APIView):
#     def get(self, request):
#         all_news = News.objects.all().values()
#
#         return Response({'posts': all_news})
#
#     def post(self, request):
#         serializer = NewsSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             instance = News.objects.get(pk=pk)
#         except:
#             return Response({"errors": ["Object does not exist"]})
#
#         serializer = NewsSerializer(data=request.data, instance=instance)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             instance = News.objects.get(pk=pk)
#         except:
#             return Response({"errors": ["Object does not exist"]})
#
#         instance.delete()
#         return Response({"message": "Object is deleted"})
