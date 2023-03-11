from ckeditor_uploader.fields import RichTextUploadingField
from django_mysql.models.fields import SizedTextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.db import models
from datetime import datetime


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True, help_text='0:processing, 1:completed')
    section = models.IntegerField(blank=True, null=True, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        if self.section:
            return '%s%s' % (self.name, self.section)
        else:
            return '%s' % self.name


class StandardNews(models.Model):
    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/StandardNews', default='default')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextUploadingField(default=' ')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='standard_category')
    is_active = models.BooleanField(default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return '%s%s' % (self.title, self.category.section)


class MainNews(models.Model):
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)
    standard_news = models.OneToOneField(StandardNews, on_delete=models.CASCADE, related_name='main_news')
    is_active = models.BooleanField(default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.standard_news.title


class LatestNews(models.Model):
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)
    standard_news = models.OneToOneField(StandardNews, on_delete=models.CASCADE, related_name='latest_news')
    is_active = models.BooleanField(default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.standard_news.title

