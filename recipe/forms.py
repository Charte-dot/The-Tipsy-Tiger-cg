from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """comment form for logged in users"""
    class Meta:
        model = Comment
        fields = ('body',)
