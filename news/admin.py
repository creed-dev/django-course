from django.contrib import admin

# Register your models here.
from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'is_published', 'created_at')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'category')


admin.site.register(News, NewsAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Category, CategoriesAdmin)
