from django.contrib import admin

from .models import Course, Section, Lesson, Category, Degree, Language, Comment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'degree', 'category', 'price', 'rating')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'section')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'rating')