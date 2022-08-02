"""
Imports
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'published'))


class Recipe(models.Model):

    """ Model for recipe """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post")
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    process = models.TextField(blank=False)
    ingredients = models.TextField(blank=False)
    serves = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(4)])
    status = models.IntegerField(choices=STATUS, default=0)
    recipe_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='recipe_like', blank=True)

    EASY = ''
    MEDIUM = 'Flashy'
    HARD = 'Challenge'

    SKILL_LEVEL = [
        (EASY, 'Quick'),
        (MEDIUM, 'Flashy'),
        (HARD, 'Challenge')
    ]

    skill = models.CharField(
        max_length=15,
        choices=SKILL_LEVEL,
        blank=False,
        default=EASY
        )

    BOURBON = 'Bourbon-base'
    GIN = 'Gin-base'
    LIQUEUR = 'Liqueur-base'
    RUM = 'Rum-base'
    TEQUILA = 'Tequila-base'
    VODKA = 'Vodka-base'
    WHISKEY = 'Whiskey-base'

    ALCOHOL_BASE_CHOICES = [
        (BOURBON, 'Bourbon-base'),
        (GIN, 'Gin-base'),
        (LIQUEUR, 'Liqueur-base'),
        (RUM, 'Rum-base'),
        (TEQUILA, 'Tequila-base'),
        (VODKA, 'Vodka-base'),
        (WHISKEY, 'Whiskey-base')
    ]

    base = models.CharField(
        max_length=15,
        choices=ALCOHOL_BASE_CHOICES,
        blank=False,
        default=BOURBON
        )

    notes = models.TextField(blank=True, max_length=200)

    class Meta:
        """ Recipes ordered to show newest first """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """ Show number of likes on a recipe """
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)


class Comment(models.Model):
    """ Model for comments, for registered users """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(default=None)
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Comments ordered from last to first """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
