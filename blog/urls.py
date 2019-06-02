from django.urls import path
from django.views.generic import DetailView, ListView

from blog.models import Article, Dinosaur

urlpatterns = [
    # Article section
    path('articles/', ListView.as_view(template_name='blog/articles.html', model=Article), name='articles'),
    path('article/<int:pk>/', DetailView.as_view(template_name='blog/article.html', model=Article), name='article'),

    # Dinosaur section
    path('dinosaurs/', ListView.as_view(template_name='blog/dinosaurs.html', model=Dinosaur), name='dinosaurs'),
    path('dinosaur/<int:pk>/', DetailView.as_view(template_name='blog/dinosaur.html', model=Dinosaur), name='dinosaur'),
]
