from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from blog.models import Article, Dinosaur, Fact

admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Dinosaur, MarkdownxModelAdmin)
admin.site.register(Fact)
