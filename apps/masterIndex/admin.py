from django.contrib import admin
from masterIndex.models import MasterIndex

class MasterIndexAdmin(admin.ModelAdmin):
    list_display = ('location_id','resource_id')
#   list_filter = ['domain', 'category', 'status']
    search_fields = ('location_id','resource_id')
admin.site.register(MasterIndex,MasterIndexAdmin)

