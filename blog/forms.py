from django import forms
from django.db.models import Model, CharField, DateTimeField, ForeignKey, TextField, SET_NULL
from blog.models import BlogPost, Blogger, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment', 'comment_blog_post')

    # comment = forms.CharField(help_text="Enter your comment here.")







# class CommentForm(LoginRequiredMixin, CreateView):

#     model = Comment

#     fields = ('user', 'comment', 'comment_blog_post')

#     comment = TextField(max_length=500, help_text="Enter a comment here")

#     # comment_date = DateTimeField(auto_now_add=True)


    

    
