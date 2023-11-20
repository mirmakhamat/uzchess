from django.urls import path
from . import views


urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('section/<int:pk>/', views.SectionView.as_view(), name='section_detail'),
    path('lesson/<int:pk>/', views.LessonView.as_view(), name='lesson_detail'),
]
