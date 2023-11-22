from rest_framework import serializers
from .models import Course, Comment, Degree, Section, Lesson


class LessonSerializer(serializers.ModelSerializer):
    section = serializers.HyperlinkedRelatedField(read_only=True, view_name='section_detail')
    class Meta:
        model = Lesson
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    course = serializers.HyperlinkedRelatedField(read_only=True, view_name='course_detail')
    class Meta:
        model = Section
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ('name', 'icon')


class CourseListSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    degree = DegreeSerializer()
    category = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ('id', 'title', 'author', 'language', 'degree', 'category',
                  'description', 'image', 'price', 'discount', 'rating',)


class CourseSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    degree = DegreeSerializer()
    category = serializers.StringRelatedField()

    sections = SectionSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
