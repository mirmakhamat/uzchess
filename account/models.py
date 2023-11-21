from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.FileField(upload_to='images/', blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=255)

    courses = models.ManyToManyField(
        'courses.Course', blank=True, related_name='clients')
    saved_books = models.ManyToManyField(
        'library.Book', blank=True, related_name='users')
    saved_courses = models.ManyToManyField(
        'courses.Course', blank=True, related_name='users')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    book = models.ForeignKey(
        'library.Book', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.book}"
