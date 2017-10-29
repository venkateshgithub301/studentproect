"""studentproect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app143 import views
from rest_framework.authtoken import views as drf_views
from app143.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getbook/',views.get_books),
    url(r'^getbookbyid/',views.get_bookby_id),
    url(r'^getbooksByUsers/',views.get_booksByUsers),
    url(r'^$',views.index),
    url(r'^login/',views.login), 
    url(r'^parent$',views.Iheritance),
    url(r'^register/',views.register),
    url(r'^addbook/',views.addbook), 
    url(r'^logout/',views.logout_page),
    url(r'^insertbookform/',views.insert_book_form),
    url(r'^api/Bookserializer/',views.GetBooksAPI.as_view()),
    url(r'^api/login/$',drf_views.obtain_auth_token),
    url(r'^cache/',views.book_viwe),
    url(r'^userinventary/',views.BookInventery.as_view()),
    
    url(r'^authorinventary/',views.AuthorInventey.as_view()),
    url(r'^author1inventary/',views.AuthorInventey.as_view()),


    url(r'^bookinventary/',views.BookInventery.as_view()),


]