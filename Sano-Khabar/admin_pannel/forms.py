from cProfile import label
from apps_nepali.models import NewsComment, StandardNews, YoutubeLink, BreakingNews, Category, AddSubTitle, AboutUs, Advertisement
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)


class EditNews(forms.ModelForm):
    photo_img = forms.ImageField(
        label='Select Image', required=False, initial='default')

    is_main_news = forms.BooleanField(
        label='Main News', required=True
    )

    class Meta:
        model = StandardNews
        exclude = ('date_uploaded', 'time_uploaded', 'number_of_views')

class EditYoutube(forms.ModelForm):
    class Meta:
        model = YoutubeLink
        exclude = ('date_uploaded', 'time_uploaded')


class EditBreakingNews(forms.ModelForm):
    class Meta:
        model = BreakingNews
        exclude = ('date_uploaded', 'time_uploaded')


class AddCategoryNepali(forms.ModelForm):
    class Meta:
        model = Category
        #exclude = ('parent', 'date_uploaded', 'time_uploaded')
        fields = ('name', 'is_active', 'section')

# class to rename the category name


class RenameCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class Advertisement_Form(forms.ModelForm):
    class Meta:
        model = Advertisement
        exclude = ('date_uploaded', 'time_uploaded')


class AddSubTitle_Form(forms.ModelForm):
    class Meta:
        model = AddSubTitle
        exclude = ('date_uploaded', 'time_uploaded')


# NewsCommentform
class NewsCommentform(forms.ModelForm):
    class Meta:
        model = NewsComment
        exclude = ('date_uploaded', 'time_uploaded')
        fields = ('email', 'comment', 'user_name')


# about us
class AboutUs(forms.ModelForm):
    class Meta:
        model = AboutUs
        exclude = ('date_uploaded', 'time_uploaded')
        fields = ('title', 'content', 'is_active')
