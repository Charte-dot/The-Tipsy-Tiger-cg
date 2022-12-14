# Generated by Django 3.2.14 on 2022-08-02 18:43

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True)),
                ('process', models.TextField()),
                ('ingredients', models.TextField()),
                ('serves', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'published')], default=0)),
                ('recipe_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('skill', models.CharField(choices=[('', 'Quick'), ('Flashy', 'Flashy'), ('Challenge', 'Challenge')], default='', max_length=15)),
                ('base', models.CharField(choices=[('Bourbon-base', 'Bourbon-base'), ('Gin-base', 'Gin-base'), ('Liqueur-base', 'Liqueur-base'), ('Rum-base', 'Rum-base'), ('Tequila-base', 'Tequila-base'), ('Vodka-base', 'Vodka-base'), ('Whiskey-base', 'Whiskey-base')], default='Bourbon-base', max_length=15)),
                ('notes', models.TextField(blank=True, max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_post', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='recipe_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipe.recipe')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
