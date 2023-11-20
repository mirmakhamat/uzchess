from rest_framework import generics, filters
from .models import Book
from rest_framework.pagination import PageNumberPagination
from .serializers import BookListSerializer, BookDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter


class BookFilter(FilterSet):
    category = CharFilter(field_name='category__name', lookup_expr='iexact')
    degree = CharFilter(field_name='degree__name', lookup_expr='iexact')
    language = CharFilter(field_name='language__name', lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['category', 'degree', 'language']


class BookListPagination(PageNumberPagination):
    page_size = 5


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BookListPagination
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_class = BookFilter


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
