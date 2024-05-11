from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(required=False)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'content', 'author', 'pub_date')