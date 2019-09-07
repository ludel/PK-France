from django.contrib import admin

from blog.models import News, Dinosaur, Fact

admin.site.register(News)
admin.site.register(Dinosaur)
admin.site.register(Fact)
