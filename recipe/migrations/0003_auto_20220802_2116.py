# Generated by Django 3.2.14 on 2022-08-02 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='content',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='process',
            new_name='steps',
        ),
    ]
