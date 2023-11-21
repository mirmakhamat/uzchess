from django.contrib import admin
from .models import User, Cart


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'birthdate',
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'book',
        'quantity',
    )
