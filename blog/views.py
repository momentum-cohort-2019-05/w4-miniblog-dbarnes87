from django.shortcuts import render, redirect
from blog.models import BlogPost, Blogger, Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

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

def add_comment(request, pk):
    from blog.forms import CommentForm
    from django.views.generic.edit import CreateView 
    comment = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = comment
            comment.save()
            return redirect('blogpost_detail', pk=BlogPost.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})



class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

# class BlogCommentCreate(LoginRequiredMixin, CreateView):
#     """
#     Form for adding a blog comment. Requires login. 
#     """
#     model = Comment
#     fields = ['comment',]

#     def get_context_data(self, **kwargs):
#         """
#         Add associated blog to form template so can display its title in HTML.
#         """
#         # Call the base implementation first to get a context
#         context = super(BlogCommentCreate, self).get_context_data(**kwargs)
#         # Get the blog from id and add it to the context
#         context['blog'] = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
#         return context
        
#     def form_valid(self, form):
#         """
#         Add author and associated blog to form data before setting it as valid (so it is saved to model)
#         """
#         #Add logged-in user as author of comment
#         form.instance.author = self.request.user
#         #Associate comment with blog based on passed id
#         form.instance.blog=get_object_or_404(BlogPost, pk = self.kwargs['pk'])
#         # Call super-class form validation behaviour
#         return super(BlogCommentCreate, self).form_valid(form)

#     def get_success_url(self): 
#         """
#         After posting comment return to associated blog.
#         """
#         return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})