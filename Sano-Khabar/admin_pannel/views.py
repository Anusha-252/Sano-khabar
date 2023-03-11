from email import message
import http
import json
from logging import exception
from unicodedata import category, name
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, EditBreakingNews, EditNews, EditYoutube, AddCategoryNepali, RenameCategory, \
    AddSubTitle_Form, Advertisement_Form
from apps_nepali.models import BreakingNews, Category, MainNews, Advertisement, YoutubeLink, StandardNews, \
    AddSubTitle


# Create your views here.

def index(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'admin_pannel/login_page.html', context)


def admin_signup_post(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ap_dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('ap_index')


def logout_post(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You are logged out")
    return redirect('ap_index')


@login_required(login_url='/admin_login/')
def ap_dashboard(request):
    return render(request, 'admin_pannel/AdminPanel_dashboard.html')


# @login_required(login_url='/admin_login/')
# def ap_layout_page(request):
#     category_query = Category.objects.all().order_by('-id')
#     context = {'category_query': category_query}
#     return render(request, 'admin_pannel/layout_page.html', context)
#

@login_required(login_url='/admin_login/')
def ap_landing_page(request):
    category_query = Category.objects.all()
    title_high = "Layout"
    context = {'category_query': category_query, 'title_high': title_high}
    return render(request, 'admin_pannel/AdminPanel_landingpage.html', context)


# delete category
@login_required(login_url='/admin_login/')
def ap_delete_category(request):
    category_query = Category.objects.all()
    context = {'category_query': category_query}
    return render(request, 'admin_pannel/Delete_Category.html', context)

@login_required(login_url='/admin_login/')
def delete_category(request, ids):
    category_query = Category.objects.get(id=ids)
    category_query.delete()
    return redirect('ap_delete_category')

# Adding Category Starts

@login_required(login_url='/admin_login/')
def ap_add_more_tittle(request):
    category_query = Category.objects.all()
    form = AddCategoryNepali()
    context = {'category_query': category_query, 'form': form}
    # context = {'category_query': category_query, 'form': form , 'category_id':ids}
    return render(request, 'admin_pannel/AdminPanel_addmoretitle.html', context)


@login_required(login_url='/admin_login/')
def add_more_post(request):
    if request.method == 'POST':
        form = AddCategoryNepali(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data.get('name')
            is_active = form.cleaned_data.get('is_active')
            section_num = request.POST.get('_section')

            print(section_num)
            if section_num == '':
                category_query = Category.objects.create(
                    name=category_name, is_active=is_active)
                category_query.save()
                return redirect('ap_layout_page')
            else:
                section_check = Category.objects.filter(section=section_num)
                if section_check:
                    return redirect('ap_layout_page')
                else:
                    category_query = Category.objects.create(
                        name=category_name, is_active=is_active, section=section_num)
                    category_query.save()
                    return redirect('ap_layout_page')

        else:
            print(form.errors)
            return redirect('ap_layout_page')


# Adding category ends
@login_required(login_url='/admin_login/')
def ap_layout_page(request):
    category_query = Category.objects.filter(level=0).order_by('-id')
    title_high = "Layout"
    context = {'category_query': category_query, 'title_high': title_high}

    return render(request, 'admin_pannel/layout_page.html', context)
# Youtube Section Starts

@login_required(login_url='/admin_login/')
def ap_youtube(request):
    category_query = Category.objects.all()
    youtube_query = YoutubeLink.objects.all().order_by('-id')
    title_high = "Youtube"
    context = {'youtube_query': youtube_query,
               'category_query': category_query, 'title_high': title_high}
    return render(request, 'admin_pannel/youtube/youtube_page.html', context)


# page to add youtube news

@login_required(login_url='/admin_login/')
def ap_add_youtube(request):
    category_query = Category.objects.all()
    youtube_query = YoutubeLink.objects.all().order_by('-id')
    form = EditYoutube()
    title_high = "Youtube"
    context = {'category_query': category_query,
               'youtube_query': youtube_query, 'form': form, 'title_high': title_high}
    return render(request, 'admin_pannel/youtube/add_youtube_news.html', context)


# adding youtube news

@login_required(login_url='/admin_login/')
def ap_add_youtube_news(request):
    if request.method == 'POST':
        form = EditYoutube(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            link = form.cleaned_data.get('link')
            is_active = form.cleaned_data.get('is_active')

            youtube_query = YoutubeLink.objects.create(
                title=title, link=link, is_active=is_active)
            youtube_query.save()
            return redirect('ap_youtube')
        else:
            print(form.errors)

            return redirect('ap_add_youtube')


@login_required(login_url='/admin_login/')
def edit_youtube_page(request, ids):
    category_query = Category.objects.all()
    youtube_query = YoutubeLink.objects.get(id=ids)
    form = EditYoutube(instance=youtube_query)
    title_high = "Youtube"
    context = {'form': form, 'youtube_query': youtube_query,
               'category_query': category_query, 'title_high': title_high}
    return render(request, 'admin_pannel/youtube/edit_youtube.html', context)

@login_required(login_url='/admin_login/')
def edit_youtube_page_post(request, ids):
    if request.method == 'POST':
        form = EditYoutube(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            link = form.cleaned_data.get('link')
            is_active = form.cleaned_data.get('is_active')

            youtube_query = YoutubeLink.objects.get(id=ids)

            youtube_query.title = title
            youtube_query.link = link
            youtube_query.is_active = is_active

            youtube_query.save()

            return redirect('ap_youtube')

        else:
            print(form.errors)

@login_required(login_url='/admin_login/')
def delete_youtube_page(request, ids):
    youtube_query = YoutubeLink.objects.get(id=ids)
    youtube_query.delete()
    return redirect('ap_adds_plus_breakingnews')

# Youtube Section Ends

@login_required(login_url='/admin_login/')
def ap_edit_breaking_news_page(request, ids):
    category_query = Category.objects.all()
    title_high = "Breaking"
    breaking_news_query = BreakingNews.objects.get(id=ids)
    form = EditBreakingNews(instance=breaking_news_query)
    context = {'form': form, 'breaking_news_query': breaking_news_query,
               'category_query': category_query, 'title_high': title_high}
    return render(request, 'admin_pannel/breaking_news/edit_breaking_news.html', context)

@login_required(login_url='/admin_login/')
def edit_breaking_news_page_post(request, ids):
    if request.method == 'POST':
        form = EditBreakingNews(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            is_active = form.cleaned_data.get('is_active')

            breaking_news_query = BreakingNews.objects.get(id=ids)

            breaking_news_query.title = title
            breaking_news_query.is_active = is_active

            breaking_news_query.save()

            return redirect('ap_breaking_news')

        else:
            print(form.errors)


@login_required(login_url='/admin_login/')
def ap_main_news_page(request):
    category_query = Category.objects.all()
    title_high = "Main_News"
    main_news_query = MainNews.objects.all().order_by('-id')

    context = {'category_query': category_query,
               'main_news_query': main_news_query, 'title_high': title_high}
    return render(request, 'admin_pannel/main_news/index.html', context)


@login_required(login_url='/admin_login/')
def ap_latest_news_page(request):
    category_query = Category.objects.all()
    news_query = StandardNews.objects.all().order_by('-id')
    form = EditNews(request.POST)
    title_high = "Latest_News"
    context = {'category_query': category_query,
               'news_query': news_query, 'form': form, 'title_high': title_high}
    return render(request, 'admin_pannel/latestnews/index.html', context)

@login_required(login_url='/admin_login/')
def delete_latest_news_page(request, ids):
    latest_news_query = StandardNews.objects.get(id=ids)
    latest_news_query.delete()
    return redirect('ap_latest_news_page')

@login_required(login_url='/admin_login/')
def ap_edit_news_page(request, ids):
    category_query = Category.objects.all()
    news_query = StandardNews.objects.get(id=ids)
    form = EditNews(instance=news_query)
    context = {'form': form, 'news_query': news_query,
               'category_query': category_query}
    return render(request, 'admin_pannel/edit_news.html', context)


# breaking_news
@login_required(login_url='/admin_login/')
def ap_breaking_news_listpage(request):
    category_query = Category.objects.all()
    breaking_query = BreakingNews.objects.all().order_by('-id')
    title_high = "Breaking"
    context = {'category_query': category_query,
               'breaking_query': breaking_query, 'title_high': title_high}
    return render(request, 'admin_pannel/breaking_news/breaking_news_page.html', context)

@login_required(login_url='/admin_login/')
def ap_add_breaking_news(request):
    category_query = Category.objects.all()
    breaking_query = BreakingNews.objects.all().order_by('-id')
    title_high = "Breaking"
    form = EditBreakingNews()
    context = {'category_query': category_query,
               'breaking_query': breaking_query, 'form': form, 'title_high': title_high}
    return render(request, 'admin_pannel/breaking_news/add_breaking_news.html', context)


@login_required(login_url='/admin_login/')
# adding breaking new post
def ap_add_breaking_news_post(request):
    if request.method == 'POST':
        form = EditBreakingNews(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')

            breaking_news_query = BreakingNews.objects.create(title=title)

            breaking_news_query.save()

            return redirect('ap_breaking_news_listpage')

        else:
            print(form.errors)

@login_required(login_url='/admin_login/')
def ap_edit_breaking_news_page(request, ids):
    category_query = Category.objects.all()
    breaking_news_query = BreakingNews.objects.get(id=ids)
    form = EditBreakingNews(instance=breaking_news_query)
    title_high = "Breaking"
    context = {'form': form, 'breaking_news_query': breaking_news_query,
               'category_query': category_query, 'title_high': title_high}
    return render(request, 'admin_pannel/breaking_news/edit_breaking_news.html', context)

@login_required(login_url='/admin_login/')
def edit_breaking_news_page_post(request, ids):
    if request.method == 'POST':
        form = EditBreakingNews(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            is_active = form.cleaned_data.get('is_active')

            breaking_news_query = BreakingNews.objects.get(id=ids)

            breaking_news_query.title = title
            breaking_news_query.is_active = is_active

            breaking_news_query.save()

            return redirect('ap_breaking_news_listpage')

        else:
            print(form.errors)

@login_required(login_url='/admin_login/')
def delete_breaking_news_page(request, ids):
    breaking_news_query = BreakingNews.objects.get(id=ids)
    breaking_news_query.delete()
    return redirect('ap_breaking_news_listpage')

@login_required(login_url='/admin_login/')
def delete_main_news_page(request, ids):
    main_news_query = StandardNews.objects.get(id=ids)
    main_news_query.delete()
    return redirect('ap_main_news_page')


# shift news to main news

@login_required(login_url='/admin_login/')
def add_main_news_btn(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['mainnewsId']
        print(product_id)

        standard_query = StandardNews.objects.filter(id=product_id).last()
        print(standard_query)

        main_news_check = MainNews.objects.filter(
            standard_news=standard_query).last()
        if main_news_check:
            print('already exist')
        else:
            main_news_query = MainNews.objects.create(
                standard_news=standard_query)
            main_news_query.save()


# adding_adds


@login_required(login_url='/admin_login/')
def ads_list_page(request):
    category_query = Category.objects.all()
    #ads_query_003 = Advertisement.objects.all().order_by('-id')
    ads_query_001 = Advertisement.objects.filter(ads_num='001').last()
    ads_query_002 = Advertisement.objects.filter(ads_num='002').last()
    ads_query_003 = Advertisement.objects.filter(ads_num='003').last()
    ads_query_004 = Advertisement.objects.filter(ads_num='004').last()

    ads_query_005 = Advertisement.objects.filter(ads_num='005').last()
    ads_query_006 = Advertisement.objects.filter(ads_num='006').last()
    ads_query_007 = Advertisement.objects.filter(ads_num='007').last()
    ads_query_008 = Advertisement.objects.filter(ads_num='008').last()

    ads_query_009 = Advertisement.objects.filter(ads_num='009').last()
    ads_query_010 = Advertisement.objects.filter(ads_num='010').last()
    ads_query_011 = Advertisement.objects.filter(ads_num='011').last()
    ads_query_012 = Advertisement.objects.filter(ads_num='012').last()

    ads_query_013 = Advertisement.objects.filter(ads_num='013').last()
    ads_query_014 = Advertisement.objects.filter(ads_num='014').last()
    ads_query_015 = Advertisement.objects.filter(ads_num='015').last()
    ads_query_016 = Advertisement.objects.filter(ads_num='016').last()

    ads_query_017 = Advertisement.objects.filter(ads_num='017').last()
    ads_query_018 = Advertisement.objects.filter(ads_num='018').last()
    ads_query_019 = Advertisement.objects.filter(ads_num='019').last()
    ads_query_020 = Advertisement.objects.filter(ads_num='020').last()

    ads_query_021 = Advertisement.objects.filter(ads_num='021').last()
    ads_query_022 = Advertisement.objects.filter(ads_num='022').last()
    ads_query_023 = Advertisement.objects.filter(ads_num='023').last()
    ads_query_024 = Advertisement.objects.filter(ads_num='024').last()

    title_high = "Advertisement"
    context = {'category_query': category_query,'title_high': title_high,
               'ads_query_001': ads_query_001,'ads_query_013': ads_query_013,
                'ads_query_002': ads_query_002,'ads_query_014': ads_query_014,
                'ads_query_003': ads_query_003,'ads_query_015': ads_query_015,
                'ads_query_004': ads_query_004,'ads_query_016': ads_query_016,
                'ads_query_005': ads_query_005,'ads_query_017': ads_query_017,
                'ads_query_006': ads_query_006,'ads_query_018': ads_query_018,
                'ads_query_007': ads_query_007,'ads_query_019': ads_query_019,
                'ads_query_008': ads_query_008,'ads_query_020': ads_query_020,
                'ads_query_009': ads_query_009,'ads_query_021': ads_query_021,
                'ads_query_010': ads_query_010,'ads_query_022': ads_query_022,
                'ads_query_011': ads_query_011,'ads_query_023': ads_query_023,
               'ads_query_012': ads_query_012, 'ads_query_024': ads_query_024}
    return render(request, 'admin_pannel/ads/for_adds.html', context)

@login_required(login_url='/admin_login/')
def add_adds(request):
    category_query = Category.objects.all()
    ads_query = Advertisement.objects.all().order_by('-id')
    form = Advertisement_Form(request.POST)
    title_high = "Advertisement"
    context = {'category_query': category_query,
               'ads_query': ads_query, 'form': form, 'title_high': title_high}
    return render(request, 'admin_pannel/ads/add_ads.html', context)


# adding new advertisement

@login_required(login_url='/admin_login/')
def add_ads_post(request):
    if request.method == 'POST':
        form = Advertisement_Form(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            print(title, '................')
            photo_img = form.cleaned_data.get('photo_img')
            print(photo_img, '................')
            link = form.cleaned_data.get('link')
            ads_num = form.cleaned_data.get('ads_num')
            ads_query = Advertisement.objects.create(
                title=title, photo_img=photo_img, link=link, ads_num=ads_num)
            ads_query.save()

            return redirect('ads_list_page')
        else:
            print(form.errors)
            return redirect('add_adds')

@login_required(login_url='/admin_login/')
def edit_ads(request, ids):
    category_query = Category.objects.all()
    #ads_query = Advertisement.objects.get(id=ids)
    ads_query = Advertisement.objects.filter(ads_num=ids).last()
    print(ads_query, "......")
    form = Advertisement_Form(instance=ads_query)
    title_high = "Advertisement"
    context = {'form': form,
               'category_query': category_query, 'title_high': title_high, 'ads_query': ads_query}
    return render(request, 'admin_pannel/ads/edit_ads.html', context)

@login_required(login_url='/admin_login/')
def edit_ads_post(request, ids):
    if request.method == 'POST':
        form = Advertisement_Form(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            print(title, '................')
            photo_img = form.cleaned_data.get('photo_img')
            link = form.cleaned_data('link')
            ads_query = Advertisement.objects.get(id=ids)
            ads_query.title = title
            ads_query.photo_img = photo_img
            ads_query.link = link

            ads_query.save()
            return redirect('ads_list_page')
        else:
            print(form.errors)
            return redirect('ads_list_page')

@login_required(login_url='/admin_login/')
def delete_ads_page(request, ids):

    ads_query = Advertisement.objects.get(ads_num=ids)
    ads_query.delete()
    return redirect('ads_list_page')
# Category title name page starts


@login_required(login_url='/admin_login/')
def ap_titles_name(request):
    category_query = Category.objects.all()
    form = RenameCategory()
    title_high = "Layout"
    context = {'category_query': category_query,
               'form': form, 'title_high': title_high}
    return render(request, 'admin_pannel/AdminPanel_titlesname.html', context)


# renaming category name
@login_required(login_url='/admin_login/')
def ap_rename_category(request):
    form = RenameCategory()
    if request.method == 'POST':
        form = RenameCategory(request.POST)
        if form.is_valid():
            category_id = request.POST.get('category_ids')
            category_name = form.cleaned_data.get('name')
            rename_query = Category.objects.filter(id=category_id).last()
            rename_query.name = category_name
            rename_query.save()
            return redirect('ap_titles_name')

# add_news page
@login_required(login_url='/admin_login/')
def ap_add_news(request):
    category_query = Category.objects.all()
    news_query = StandardNews.objects.all().order_by('-id')
    form = EditNews(request.POST)
    context = {'category_query': category_query,
               'news_query': news_query, 'form': form, }
    return render(request, 'admin_pannel/sub-category/add_news.html', context)


# add_news post
@login_required(login_url='/admin_login/')
def ap_add_news_post(request):
    if request.method == 'POST':
        form = EditNews(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            editor_name = form.cleaned_data.get('editor_name')
            location = form.cleaned_data.get('location')
            is_main_news = form.cleaned_data.get('is_main_news')
            news_summary = form.cleaned_data.get('news_summary')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            is_active = form.cleaned_data.get('is_active')
            photo_img = form.cleaned_data.get('photo_img')

            try:
                print("Hello ")
                news_query = StandardNews.objects.create(title=title, editor_name=editor_name, location=location,
                                                        news_summary=news_summary, description=description,
                                                        is_active=is_active, category=category, photo_img=photo_img)
                news_query.save()

                print(is_main_news)
                if is_main_news:
                    main_news_query = MainNews.objects.create(standard_news=news_query, is_active=is_active)

                    main_news_query.save()

                return redirect('ap_add_sub_title', ids=category.id)
            except Exception as e:
                print("excetion ", e)
                return redirect(http.HTTPStatus.INTERNAL_SERVER_ERROR)

        else:
            print(form.errors)


# edit_news page
@login_required(login_url='/admin_login/')
def ap_edit_news(request, ids):
    category_query = Category.objects.all()
    news_query = StandardNews.objects.get(id=ids)
    form = EditNews(instance=news_query)
    context = {'form': form, 'news_query': news_query,
               'category_query': category_query, 'edit_news': 'true'}
    return render(request, 'admin_pannel/sub-category/add_news.html', context)

@login_required(login_url='/admin_login/')
def ap_edit_news_post(request, ids):
    if request.method == 'POST':
        form = EditNews(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
        print(title, '................')
        editor_name = form.cleaned_data.get('editor_name')
        location = form.cleaned_data.get('location')
        news_summary = form.cleaned_data.get('news_summary')
        print(news_summary, '................')
        description = form.cleaned_data.get('description')
        category = form.cleaned_data.get('category')
        print(category, '................')
        is_active = form.cleaned_data.get('is_active')
        photo_img = form.cleaned_data.get('photo_img')
        news_query = StandardNews.objects.get(id=ids)
        news_query.title = title
        news_query.editor_name = editor_name
        news_query.location = location
        news_query.news_summary = news_summary
        news_query.description = description
        news_query.category = category
        news_query.is_active = is_active
        news_query.photo_img = photo_img
        news_query.save()
        return redirect('ap_add_sub_title', news_query.category.id)
    else:

        print("error")
        return redirect('ap_dashboard')


# delete news page

@login_required(login_url='/admin_login/')
def delete_news_page(request, ids):
    news_query = StandardNews.objects.get(id=ids)
    news_query.delete()
    return redirect('ap_add_sub_title', ids=news_query.category.id)


@login_required(login_url='/admin_login/')
def ap_add_sub_title(request, ids):
    current_query = Category.objects.filter(id=ids).last()
    category_query = Category.objects.filter(parent_id=ids).order_by('-id')
    news_query = StandardNews.objects.filter(category=current_query)
    print(category_query, '................')
    form = AddSubTitle()
    print(ids, '................')
    context = {'category_query': category_query, 'form': form, 'category_id': ids,
               'news_query': news_query, 'current_query': current_query}
    return render(request, 'admin_pannel/sub-category/Add_sub_title.html', context)


# adding new sub-title

@login_required(login_url='/admin_login/')
def ap_add_sub_title_post(request, ids):
    if request.method == 'POST':
        form = AddSubTitle_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('title')
            print(name, '......t..........')
            current_category = Category.objects.get(id=ids)
            sub_title_query = Category.objects.create(
                name=name, parent=current_category)
            sub_title_query.save()
            print(ids)
            return redirect('ap_add_sub_title', ids)
        else:
            print(form.errors)
