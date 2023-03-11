from datetime import datetime, date
from django.db.models import Q

import adbs
import nepali_datetime

from django.shortcuts import render

from .models import (Category, StandardNews, MainNews, LatestNews)
from apps_nepali.models import YoutubeLink


def latest_dates_np(value):
    value = value.strftime('%Y/%m/%d')
    given_date = value
    np_list = adbs.ad_to_bs(given_date)
    np_date = np_list['ne']['year'] + '/' + np_list['ne']['month'] + '/' + np_list['ne']['day']
    return np_date


def index(request):
    category_query = Category.objects.all().order_by('id')

    # standard_news_query = StandardNews.objects.all()
    section_1 = StandardNews.objects.filter(category__section=1).order_by('-id')
    first_section11 = section_1[0]
    first_section12 = section_1[1]
    section1_section2 = section_1[2:5]
    section_2 = StandardNews.objects.filter(category__section=2).order_by('-id')
    first_section21 = section_2[0]
    first_section22 = section_2[1]
    section2_section2 = section_2[2:5]
    section_3 = StandardNews.objects.filter(category__section=3).order_by('-id')
    section3_name = Category.objects.filter(section=3).last()

    today_date = datetime.now
    today_dates = date.today()
    current_time = datetime.now().time().strftime("%H:%M:%S")
    print(current_time , "hello")

    nepali_date = nepali_datetime.datetime.today().strftime('%K-%n-%D (%G) , %i : %l')

    main_news_query = MainNews.objects.all().order_by('-id')[0:2]
    main_news_query1 = MainNews.objects.all().order_by('-id')[2]
    main_news_query2 = MainNews.objects.all().order_by('-id')[3:7]
    latest_news_query = LatestNews.objects.all().order_by('-id')[0:6]

    youtube_link_query = YoutubeLink.objects.all().order_by('-id')

    context = {'category_query': category_query, 'title': 'होमपेज', 'date': today_date,
               'first_section11': first_section11, 'today_dates': today_dates, 'nepali_date': nepali_date,
               'first_section12': first_section12, 'section1_section2': section1_section2,
               'first_section21': first_section21, 'current_time': current_time,
               'first_section22': first_section22, 'section2_section2': section2_section2,
               'section_3': section_3, 'section3_name': section3_name, 'main_news_query': main_news_query,
               'main_news_query1': main_news_query1, 'main_news_query2': main_news_query2,
               'latest_news_query': latest_news_query,
               'youtube_link_query': youtube_link_query}
    return render(request, 'index.html', context)


def per_page(request, ids):
    standard_news_query = MainNews.objects.get(id=ids)
    # print(standard_news_query)
    # product = get_object_or_404(StandardNews, id=7)
    # print(product)
    category_query = Category.objects.all().order_by('id')
    today_date = datetime.now
    today_dates = datetime.date
    print(today_dates)
    nepali_date = nepali_datetime.datetime.today().strftime('%K %N %D (%G), %h : %l : %s')
    np_date = latest_dates_np(standard_news_query.date_uploaded)

    latest_news_query = LatestNews.objects.all().order_by('-id')[0:6]

    section_3 = StandardNews.objects.filter(category__section=3).order_by('-id')
    section3_name = Category.objects.filter(section=3).last()

    youtube_link_query = YoutubeLink.objects.all().order_by('-id')

    context = {'standard_news_query': standard_news_query, 'title': 'होमपेज', 'category_query': category_query,
               'date': today_date, 'nepali_date': nepali_date, 'np_date': np_date,
               'latest_news_query': latest_news_query, 'section_3': section_3, 'section3_name': section3_name,
               'youtube_link_query': youtube_link_query}
    return render(request, 'per_page_news.html', context)


def list_news(request, ids):
    category_query = Category.objects.all().order_by('id')
    category_news_query = StandardNews.objects.filter(Q(category__id=ids) | Q(category__parent_id=ids))
    category_query1 = Category.objects.filter(id=ids).last()
    latest_news_query = LatestNews.objects.all().order_by('-id')[0:6]

    section_3 = StandardNews.objects.filter(category__section=3).order_by('-id')
    section3_name = Category.objects.filter(section=3).last()

    youtube_link_query = YoutubeLink.objects.all().order_by('-id')

    context = {'category_news_query': category_news_query, 'category_query': category_query,
               'category_query1': category_query1, 'latest_news_query': latest_news_query, 'section_3': section_3,
               'section3_name': section3_name, 'youtube_link_query': youtube_link_query}
    return render(request, 'list.html', context)
