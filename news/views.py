from .serializers import NewsListSerializer, NewsDetailSerializer
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from .models import News

class NewsListPagination(PageNumberPagination):
    page_size = 12


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = NewsListPagination
    

class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)
