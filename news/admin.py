from django.contrib import admin

from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated', 'is_published']
    list_filter = ['updated', 'is_published']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'text']
    ordering = ['updated', 'is_published']
