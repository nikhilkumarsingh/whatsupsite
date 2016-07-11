from django.contrib import admin
from .models import Search,User



class SearchAdmin(admin.ModelAdmin):
    list_display = ('query', 'user')
admin.site.register(Search,SearchAdmin)
