from django.shortcuts import render
from .serializers import NewsSerializer, NewsForUpdateSerializer, CommentSerializer
from .models import News, Comment
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsAuthorrOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class NewsPagePagination(PageNumberPagination):
    page_size = 3




class NewsCreateApiView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagePagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['created', ]
    search_fields = ['search', ]
    permission_classes = [IsAuthorrOrReadOnly, IsOwnerOrReadOnly]


class NewsCreateRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsForUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class CommentCreateViewSet(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    search_fields = ['search', 'offset']


