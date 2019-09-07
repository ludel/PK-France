from django.urls import path
from django.views.generic import DetailView, ListView, TemplateView

from blog.models import News, Dinosaur
from blog.views import FactView

urlpatterns = [
    # Article section
    path('news/', ListView.as_view(template_name='blog/news_list.html', model=News), name='articles'),
    path('news/<int:pk>/', DetailView.as_view(template_name='blog/news_item.html', model=News), name='article'),

    path('article/presentation/', TemplateView.as_view(template_name='article/presentation.html'),
         name='article_presentation'),
    path('article/modes/', TemplateView.as_view(template_name='article/modes.html'),
         name='article_modes'),
    path('article/gameplay/', TemplateView.as_view(template_name='article/gameplay.html'),
         name='article_gameplay'),

    # Dinosaur section
    path('dinosaurs/', ListView.as_view(template_name='blog/dinosaurs.html', model=Dinosaur), name='dinosaurs'),
    path('dinosaur/<int:pk>/', DetailView.as_view(template_name='blog/dinosaur.html', model=Dinosaur), name='dinosaur'),

    # Fact section
    path('fact/', FactView.as_view(), name='fact'),
]
