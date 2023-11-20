from django.contrib import admin
from .models import User, BoughtCourse, SavedBook, SavedCourse, Cart


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'birthdate',
    )


@admin.register(BoughtCourse)
class BoughtCourseAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
    )


@admin.register(SavedBook)
class SavedBookAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'book',
    )


@admin.register(SavedCourse)
class SavedCourseAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'book',
        'quantity',
    )

