from django.contrib import admin
from auditTrail.models import AuditTrail

class AuditTrailAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'action', 'audit','item_id','timestamp')
#   list_filter = ['domain', 'category', 'status']
    search_fields = ('user_id', 'action', 'audit','item_id','timestamp')
admin.site.register(AuditTrail,AuditTrailAdmin)

