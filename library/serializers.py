from rest_framework import serializers
from .models import Book, Category, Degree, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ('name', 'icon')


class BookListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    degree = DegreeSerializer()
    language = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ('title', 'author', 'image', 'price', 'discount',
                  'rating', 'category', 'degree', 'language')



class BookDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    degree = DegreeSerializer()
    language = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = '__all__'
