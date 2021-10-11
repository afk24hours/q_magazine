from django.contrib import admin
from django import forms
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    inlines = [
        CommentInLine,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)