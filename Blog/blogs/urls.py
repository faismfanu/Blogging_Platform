from django.urls import path
from .views import BlogPostList,BlogPostDetail

urlpatterns = [
    path('', BlogPostList.as_view(), name='blogpost-list'),
    path('<int:id>/', BlogPostDetail.as_view(), name='blogpost-detail'),
]