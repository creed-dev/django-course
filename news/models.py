from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='media/news/img')
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'
