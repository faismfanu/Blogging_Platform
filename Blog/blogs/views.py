from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date
from rest_framework.pagination import PageNumberPagination

class BlogPostList(ListCreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PageNumberPagination 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = BlogPost.objects.all()
        author_name = self.request.query_params.get('author')
        if author_name:
            try:
                author = User.objects.get(username=author_name)
                queryset = queryset.filter(author=author)
            except User.DoesNotExist:
                queryset = queryset.none()

        pub_date_str = self.request.query_params.get('pub_date')
        if pub_date_str:
            try:
                pub_date = parse_date(pub_date_str)
                queryset = queryset.filter(pub_date=pub_date)
            except ValueError:
                queryset = queryset.none()
        return queryset

class BlogPostDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PageNumberPagination 
    lookup_field = "id"

    def get_queryset(self):
        return BlogPost.objects.all()



        
