from django.contrib import admin
from .models import Article, ArticleSeries

class ArticleSeriesAdmin(admin.ModelAdmin):
  fields = [
    'title',
    'subtitle',
    'slug'
    # 'published' don't want to show it
  ]

class ArticleAdmin(admin.ModelAdmin):
  # fields = ['title', 'subtitle', 'slug', 'series', 'content', 'modified']

  fieldsets = [
    ('Header', { 'fields': ['title', 'subtitle', 'slug', 'series'] }),
    ('Content', { 'fields': ['content'] }),
    ('Date', { 'fields': ['modified'] })
  ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
