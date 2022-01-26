
from django.contrib import admin
from .models import Article, Tag, Category
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    '''Admin View for Article'''

    list_display = ('title',)
    list_filter = ('title',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    ordering = ('published',)
    prepopulated_fields = {'slug': ['title'],}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name',)
    list_filter = ('name',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    ordering = ('name',)
    prepopulated_fields = {'slug': ['name'],}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    '''Admin View for Tag'''

    list_display = ('name',)
    list_filter = ('name',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    ordering = ('name',)
    prepopulated_fields = {'slug': ['name'],}