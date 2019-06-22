from django import forms
from django.db.models import Model, CharField, DateTimeField, ForeignKey, TextField, SET_NULL

    
class CommenmtForm(forms.Form):

    comment = forms.TextField(max_length=500, help_text="Enter a comment here")

    comment_date = DateTimeField(auto_now_add=True)

    

    
