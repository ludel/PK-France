from django.contrib import admin

from blog.models import Article, Dinosaur, Fact

admin.site.register(Article)
admin.site.register(Dinosaur)
admin.site.register(Fact)
