from datetime import datetime, date
from django.db.models import Q

import adbs
import nepali_datetime

from django.shortcuts import render, redirect
# import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import (Advertisement, BreakingNews, Category,
                     StandardNews, MainNews, LatestNews, YoutubeLink, NewsComment)
from admin_pannel.forms import NewsCommentform


def latest_dates_np(value):
    value = value.strftime('%Y/%m/%d')
    given_date = value
    np_list = adbs.ad_to_bs(given_date)
    np_date = np_list['ne']['year'] + '/' + \
              np_list['ne']['month'] + '/' + np_list['ne']['day']
    return np_date


def index(request):
    category_query = Category.objects.all().order_by('id')
    breaking_query = BreakingNews.objects.all().order_by('id')
    main_news_query = MainNews.objects.all().order_by('-id')[0:2]
    section_1 = StandardNews.objects.filter(
        category__section=1).order_by('-id')
    section1_name = Category.objects.filter(section=1).last()
    section1_display1 = section_1[0]
    section1_display2 = section_1[1:4]

    # print(section1_display1)
    # first_section11 = section_1[0]
    # first_section12 = section_1[1]
    # main_news_query1 = MainNews.objects.all().order_by('-id')[2]
    # main_news_query2 = MainNews.objects.all().order_by('-id')[3:7]

    section_2 = StandardNews.objects.filter(
        category__section=2).order_by('-id')
    section2_name = Category.objects.filter(section=2).last()
    section2_display1 = section_2[0]
    section2_display2 = section_2[1]
    section2_display3 = section_2[2:6]
    # first_section22 = section_2[1]
    # section2_section2 = section_2[2:5]
    # for Section3_done
    section_3 = StandardNews.objects.filter(
        category__section=3).order_by('-id')
    section3_name = Category.objects.filter(section=3).last()
    section3_display = section_3[0:5]
    # first_section31 = section_3[0]
    # first_section32 = section_3[1]
    # section3_section2 = section_3[2:5]
    today_date = datetime.now
    today_dates = date.today()
    current_time = datetime.now().time().strftime("%H:%M:%S")
    nepali_date = nepali_datetime.datetime.today().strftime('%K-%n-%D (%G) , %i : %l')



    latest_news_query = StandardNews.objects.all().order_by('-id')[0:6]
    youtube_link_query = YoutubeLink.objects.all().order_by('-id')
    ads_content_001 = Advertisement.objects.filter(ads_num__gte='001')
    ads_content_002 = Advertisement.objects.filter(ads_num__gte='002')
    ads_content_003 = Advertisement.objects.filter(ads_num__gte='003')
    ads_content_004 = Advertisement.objects.filter(ads_num__gte='004')

    ads_content_005 = Advertisement.objects.filter(ads_num__gte='005')
    ads_content_006 = Advertisement.objects.filter(ads_num__gte='006')
    ads_content_007 = Advertisement.objects.filter(ads_num__gte='007')
    ads_content_008 = Advertisement.objects.filter(ads_num__gte='008')

    context = {'category_query': category_query,
               'ads_content_001': ads_content_001,
               'ads_content_002': ads_content_002,
               'ads_content_003': ads_content_003,
               'ads_content_004': ads_content_004,

               'ads_content_005': ads_content_005,
               'ads_content_006': ads_content_006,
               'ads_content_007': ads_content_007,
               'ads_content_008': ads_content_008,

               'title': 'होमपेज',
               'date': today_date,
               'section1_name': section1_name,
               'section1_display1': section1_display1,
               'section1_display2': section1_display2,
               'today_dates': today_dates, 'nepali_date': nepali_date,
               'current_time': current_time,
               'section2_name': section2_name,
               'section2_display1': section2_display1,
               'section2_display2': section2_display2,
               'section2_display3': section2_display3,
               'section_3': section_3,
               'section3_name': section3_name,
               'section3_display': section3_display,
               'main_news_query': main_news_query,
               'latest_news_query': latest_news_query,
               'youtube_link_query': youtube_link_query,
               'breaking_query': breaking_query}
    return render(request, 'index.html', context)


def per_page(request, ids):
    standard_news_query = StandardNews.objects.get(id=ids)
    category_query = Category.objects.all().order_by('id')
    today_date = datetime.now
    today_dates = datetime.date
    print(today_dates)
    nepali_date = nepali_datetime.datetime.today().strftime(
        '%K %N %D (%G), %h : %l : %s')
    np_date = latest_dates_np(standard_news_query.date_uploaded)
    latest_news_query = StandardNews.objects.all().order_by('-id')[0:6]
    section_1 = StandardNews.objects.filter(
        category__section=1).order_by('-id')
    section1_name = Category.objects.filter(section=1).last()
    section1_display1 = section_1[0]
    section1_display2 = section_1[1:4]
    section_2 = StandardNews.objects.filter(
        category__section=2).order_by('-id')
    section2_name = Category.objects.filter(section=2).last()
    section2_display1 = section_2[0]
    section2_display2 = section_2[1]
    section2_display3 = section_2[2:6]
    section_3 = StandardNews.objects.filter(
        category__section=3).order_by('-id')
    section3_name = Category.objects.filter(section=3).last()
    section3_display = section_3[0:5]
    youtube_link_query = YoutubeLink.objects.all().order_by('-id')
    ads_content_001 = Advertisement.objects.filter(ads_num__gte='001')

    ads_content_017 = Advertisement.objects.filter(ads_num__gte='017')
    ads_content_018 = Advertisement.objects.filter(ads_num__gte='018')
    ads_content_019 = Advertisement.objects.filter(ads_num__gte='019')
    ads_content_020 = Advertisement.objects.filter(ads_num__gte='020')

    ads_content_021 = Advertisement.objects.filter(ads_num__gte='021')
    ads_content_022 = Advertisement.objects.filter(ads_num__gte='022')
    ads_content_023 = Advertisement.objects.filter(ads_num__gte='023')
    ads_content_024 = Advertisement.objects.filter(ads_num__gte='024')
    news_comment = NewsComment.objects.filter(news_id=ids).order_by('-uploaded_date_time')

    # to post the commetn in per page news
    context = {'standard_news_query': standard_news_query, 'title': 'होमपेज', 'category_query': category_query,
               'date': today_date, 'nepali_date': nepali_date, 'np_date': np_date,
               'latest_news_query': latest_news_query,
               'section1_name': section1_name, 'section1_display1': section1_display1,
               'section1_display20': section1_display2,
               'section2_name': section2_name,
               'section2_display1': section2_display1,
               'section2_display2': section2_display2,
               'section2_display3': section2_display3,
               'section_3': section_3,
               'section3_name': section3_name,
               'section3_display': section3_display,
               'news_comment': news_comment,
               'ads_content_001': ads_content_001,

               'ads_content_017': ads_content_017,
               'ads_content_018': ads_content_018,
               'ads_content_019': ads_content_019,
               'ads_content_020': ads_content_020,

               'ads_content_021': ads_content_021,
               'ads_content_022': ads_content_022,
               'ads_content_023': ads_content_023,
               'ads_content_024': ads_content_024,

               'youtube_link_query': youtube_link_query}
    return render(request, 'per_page_news001.html', context)


def list_news(request, ids):
    category_query = Category.objects.all().order_by('id')
    current_category = Category.objects.get(id=ids)
    category_news_query = StandardNews.objects.filter(
        Q(category__id=ids) | Q(category__parent_id=ids))
    category_query1 = Category.objects.filter(id=ids).last()
    latest_news_query = LatestNews.objects.all().order_by('-id')[0:6]
    section_3 = StandardNews.objects.filter(
        category__section=3).order_by('-id')
    section3_name = Category.objects.filter(section=3).last()
    youtube_link_query = YoutubeLink.objects.all().order_by('-id')

    ads_content_009 = Advertisement.objects.filter(ads_num__gte='009')
    ads_content_010 = Advertisement.objects.filter(ads_num__gte='010')
    ads_content_011 = Advertisement.objects.filter(ads_num__gte='011')
    ads_content_012 = Advertisement.objects.filter(ads_num__gte='012')

    ads_content_013 = Advertisement.objects.filter(ads_num__gte='0013')
    ads_content_014 = Advertisement.objects.filter(ads_num__gte='014')
    ads_content_015 = Advertisement.objects.filter(ads_num__gte='015')
    ads_content_016 = Advertisement.objects.filter(ads_num__gte='016')

    paginator_current_news = Paginator(category_news_query, 10)
    page_number_current_news = request.GET.get('page_news_object')
    try:
        page_obj_current_news = paginator_current_news.page(
            page_number_current_news)
    except PageNotAnInteger:
        page_obj_current_news = paginator_current_news.page(1)
    except EmptyPage:
        page_obj_current_news = paginator_current_news.page(
            paginator_current_news.num_pages)

    context = {'category_news_query': page_obj_current_news, 'category_query': category_query,
               'current_category': current_category,
               'ads_content_009': ads_content_009,
               'ads_content_010': ads_content_010,
               'ads_content_011': ads_content_011,
               'ads_content_012': ads_content_012,

               'ads_content_013': ads_content_013,
               'ads_content_014': ads_content_014,
               'ads_content_015': ads_content_015,
               'ads_content_016': ads_content_016,
               'category_query1': category_query1, 'latest_news_query': latest_news_query, 'section_3': section_3,
               'section3_name': section3_name, 'youtube_link_query': youtube_link_query}
    return render(request, 'list.html', context)


# function to post commetn in per page news
def post_comment(request, ids):
    if request.method == 'POST':
        form = NewsCommentform(request.POST)
    if form.is_valid():
        user_name = form.cleaned_data['user_name']
        comment = form.cleaned_data['comment']
        email = form.cleaned_data['email']
        news_comment = NewsComment.objects.create(user_name=user_name, comment=comment, email=email, news_id=ids)
        news_comment.save()
        return redirect('per_page', ids)
