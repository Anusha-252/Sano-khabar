from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from .models import (Category, StandardNews, MainNews, LatestNews,Advertisement,
                     YoutubeLink, BreakingNews,  NewsComment)

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
# Register your models here.
admin.site.register(
    StandardNews)

admin.site.register(
    MainNews)

admin.site.register(
    LatestNews)

admin.site.register(
    YoutubeLink)

admin.site.register(
    BreakingNews)

admin.site.register(
    Advertisement)

admin.site.register(
    NewsComment)
