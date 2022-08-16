from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Add fields which will use summernote editor in admin panel
    """
    list_filter = (
        'status', 'created_on', 'base', 'author', 'skill')
    list_display = (
        'title', 'author', 'slug', 'base', 'skill', 'status', 'created_on')
    search_fields = [
        'title', 'base', 'skill']
    prepopulated_fields = {
        'slug': ('title',)}
    summernote_fields = (
        'about', 'ingredients', 'steps')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for additional display in admin panel
    """
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
