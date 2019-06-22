from django.urls import path, include
from django.conf.urls import re_path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.BlogPostListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('blogger/', views.BloggerListView.as_view(), name='blogger'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),

]

urlpatterns += [   
    path('blogpost/<post:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
