from rest_framework import serializers
from .models import News
from django.db.models import Count

class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            'title',
            'description',
            'image',
            'created_at',
        )

class NewsDetailSerializer(serializers.ModelSerializer):
    similar_news = serializers.SerializerMethodField()
    tags = serializers.StringRelatedField(many=True)
    
    def get_similar_news(self, obj):
        news_tags_ids = obj.tags.values_list('id', flat=True)
        similar_news = News.objects.filter(tags__in=news_tags_ids).exclude(id=obj.id)
        similar_news = similar_news.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created_at')
        return NewsListSerializer(similar_news, many=True).data
        
    class Meta:
        model = News
        fields = '__all__'