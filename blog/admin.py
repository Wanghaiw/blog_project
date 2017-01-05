from django.contrib import admin

# Register your models here.
from blog.models import Article, Category, Tag



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created_time','status','category')



admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
