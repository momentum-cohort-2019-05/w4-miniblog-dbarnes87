from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.BlogPostListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),
]