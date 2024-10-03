from django.contrib import admin
from .models import *

@admin.register(Ticket)
class ticketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id','Issue_type','related_application_number', 'supporting_documents','description','name','phone_number')





@admin.register(DSATicket)
class DSATicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'issue_type', 'status', 'created_at', 'name','phone_number')
    list_filter = ('issue_type', 'status')
    search_fields = ('description', 'name', 'phone_number')
    ordering = ('-created_at',)






class FranchiseeTicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'issue_type', 'status', 'created_at', 'name', 'phone_number')
    list_filter = ('issue_type', 'status', 'created_at')
    search_fields = ('name', 'phone_number', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('issue_type', 'description', 'status', 'name', 'phone_number')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(FranchiseeTicket, FranchiseeTicketAdmin)
