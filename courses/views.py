from rest_framework import generics, filters
from .serializers import CourseListSerializer, CourseSerializer, LessonSerializer, SectionSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from rest_framework.pagination import PageNumberPagination

from .models import Course, Lesson, Section


class CourseFilter(FilterSet):
    category = CharFilter(field_name='category__name', lookup_expr='iexact')
    degree = CharFilter(field_name='degree__name', lookup_expr='iexact')
    language = CharFilter(field_name='language__name', lookup_expr='iexact')

    class Meta:
        model = Course
        fields = ['category', 'degree', 'language']


class CourseListPagination(PageNumberPagination):
    page_size = 4


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    pagination_class = CourseListPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_class = CourseFilter


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class SectionView(generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
