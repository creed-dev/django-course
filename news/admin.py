from django.contrib import admin

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published')


admin.site.register(News, NewsAdmin)
