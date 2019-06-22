from django.shortcuts import render
from blog.models import BlogPost, Blogger, Comment
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blog_posts = BlogPost.objects.all().count()
    num_comments = Comment.objects.all().count()
    
    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_bloggers = Blogger.objects.count()
    
    context = {
        'num_blog_posts': num_blog_posts,
        'num_comments': num_comments,
        # 'num_instances_available': num_instances_available,
        'num_bloggers': num_bloggers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5


class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger