from django.contrib import admin

from blog.models import BlogPost, Blogger, Comment

# admin.site.register(BlogPost)
# admin.site.register(Blogger)
# admin.site.register(Comment)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title', 'post_date')

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass    
    # list_display = ('first_name', 'last_name')

@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):
    # pass
    list_display = ('comment', 'comment_date', 'user')
