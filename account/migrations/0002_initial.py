# Generated by Django 4.2.6 on 2023-11-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='clients', to='courses.course'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='saved_books',
            field=models.ManyToManyField(blank=True, related_name='users', to='library.book'),
        ),
        migrations.AddField(
            model_name='user',
            name='saved_courses',
            field=models.ManyToManyField(blank=True, related_name='users', to='courses.course'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
