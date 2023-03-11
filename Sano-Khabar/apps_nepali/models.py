from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from django_mysql.models.fields import SizedTextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.db import models
from datetime import datetime


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    is_active = models.BooleanField(
        default=True, help_text='0:processing, 1:completed')
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
    photo_img = models.ImageField(
        blank=True, null=True, upload_to='photos/StandardNews', default='default')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextUploadingField(default=' ')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='standard_category')
    is_active = models.BooleanField(
        default=True, help_text='0:processing, 1:completed')
        

    def __str__(self):
        return '%s%s' % (self.title, self.category.section)


class MainNews(models.Model):
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)
    standard_news = models.OneToOneField(StandardNews, on_delete=models.CASCADE, related_name='main_news')
    is_active = models.BooleanField(
        default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.standard_news.title


class LatestNews(models.Model):
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)
    standard_news = models.OneToOneField(
        StandardNews, on_delete=models.CASCADE, related_name='latest_news')
    is_active = models.BooleanField(
        default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.standard_news.title


class YoutubeLink(models.Model):
    class Meta:
        db_table = 'YoutubeLink'

    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    is_active = models.BooleanField(
        default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.title


class BreakingNews(models.Model):
    title = models.CharField(max_length=200)
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    is_active = models.BooleanField(
        default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    photo_img = models.ImageField(blank=True, null=True, upload_to='image/')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    link = models.CharField(max_length=200, blank=True)
    ads_num = models.BigIntegerField(default=0)


    def __str__(self):
        return self.title

# add_sub_title models


class AddSubTitle(models.Model):

    title = models.CharField(max_length=200)
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='ap_add_sub_title')

    #is_active = models.BooleanField(default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.title


class NewsComment(models.Model):
    class Meta:
        db_table = 'NewsComment'

    user_name = models.CharField(max_length=20)
    comment = models.CharField(max_length=200)
    email = models.CharField(max_length=50, null=True)
    uploaded_date_time = models.DateTimeField(default=datetime.now)
    news = models.ForeignKey(
        StandardNews, on_delete=models.CASCADE, related_name='news_comment')
    

    is_active = models.BooleanField(
        default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return '%s%s' % (self.user_name, self.news.title)


class AboutUs(models.Model):
    class Meta:
        db_table = 'about_us'

    title = models.CharField(max_length=20, default=None)
    content = RichTextUploadingField()
    is_active = models.BooleanField(
        default=True, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.title
