# Generated by Django 3.2.14 on 2022-08-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20220802_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='base',
            field=models.CharField(choices=[('Bourbon-base', 'Bourbon-base'), ('Gin-base', 'Gin-base'), ('Liqueur-base', 'Liqueur-base'), ('Non-Alcoholic', 'Non-Alcoholic'), ('Rum-base', 'Rum-base'), ('Tequila-base', 'Tequila-base'), ('Vodka-base', 'Vodka-base'), ('Whiskey-base', 'Whiskey-base')], default='Bourbon-base', max_length=15),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='skill',
            field=models.CharField(choices=[('Quick & Easy', 'Quick & Easy'), ('A bit Flashy', 'A bit Flashy'), ('Challenge me', 'Challenge Me')], default='Quick & Easy', max_length=15),
        ),
    ]
