from django.contrib import admin
from .models import Ourteam, Contact, Blog

class OurteamAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'image')
    search_fields = ('name', 'title')
    list_filter = ('title',)
    ordering = ('name',)
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('name', 'email', 'phone')
    ordering = ('name',)
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'is_active')  # Display these fields in the admin list view
    list_filter = ('author', 'date', 'is_active')  # Add filters for these fields
    search_fields = ('title', 'short_description', 'description')  # Enable search by these fields
    ordering = ('-date',)  # Order by date in descending order
    list_editable = ('is_active',)  # Allow inline editing of the 'is_active' field in the list view
    date_hierarchy = 'date'  # Add a date hierarchy for quick navigation

    # Customize the form view
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'image', 'short_description', 'description', 'slug', 'is_active')
        }),
        ('Date Information', {
            'fields': ('date',),
            'classes': ('collapse',),  # Collapse the date section for a cleaner UI
        }),
    )

    readonly_fields = ('date',)  # Make the 'date' field read-only

admin.site.register(Ourteam, OurteamAdmin)
admin.site.register(Contact, ContactAdmin)


