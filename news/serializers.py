from . import models
from .models import News, Comment, StatusComment, StatusNews, StatusType
from rest_framework import serializers



class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=500)

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['title', 'content']

class NewsForUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(write_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_field = ['text', ]








