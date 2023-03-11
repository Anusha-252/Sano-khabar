from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='nepali_index'),
    path('per_page/<int:ids>', views.per_page, name='nepali_per_page'),
    path('list_news/<int:ids>', views.list_news, name='nepali_list_news'),
    path('post_comment/<int:ids>', views.post_comment, name='post_comment'),
   
]
