from django.contrib import admin

from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('user',)
    list_filter = ('user',)
    #inlines = []
    #raw_id_fields = ('',)
    #readonly_fields = ('',)
    #search_fields = ('',)
    #date_hierarchy = ''
    ordering = ('user',)
    prepopulated_fields = {'slug': ['user'],}