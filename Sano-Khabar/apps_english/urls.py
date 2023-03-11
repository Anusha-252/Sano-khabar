from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='english_index'),
    path('per_page/<int:ids>', views.per_page, name='english_per_page'),
    path('list_news/<int:ids>', views.list_news, name='english_list_news')

]
