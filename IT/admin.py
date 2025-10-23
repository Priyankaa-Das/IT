from django.contrib import admin
from .models import Team, Blog, Category, Tags , Service , ContactMessage

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'position')


admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Service)
admin.site.register(ContactMessage)  
