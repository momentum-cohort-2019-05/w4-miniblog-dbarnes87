from django.db.models import Model, CharField, DateTimeField, ForeignKey, TextField, SET_NULL
from django.urls import reverse
from datetime import date


# Create your models here.
class BlogPost(Model):

    title = CharField(max_length=200, help_text="Enter a title for your blog")

    blogger = ForeignKey('Blogger', on_delete=SET_NULL, null=True)

    post = TextField(max_length=1000, help_text='Enter a brief description of the book')

    post_date = DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blog-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} {self.post_date}'

class Blogger(Model):

    first_name = CharField(max_length=100)
    
    last_name = CharField(max_length=100)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

class Comment(Model):

    comment = CharField(max_length=200, help_text="Enter a comment here")

    post_date = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.comment})'

    