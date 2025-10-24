from django.contrib import admin
from .models import Team, Blog, Category, Tags , Service , ContactMessage , CaseStudy, CaseStudyCategory, CaseStudyTags



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





@admin.register(CaseStudyCategory)
class CaseStudyCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    prepopulated_fields = {'slug': ('category',)}

@admin.register(CaseStudyTags)
class CaseStudyTagsAdmin(admin.ModelAdmin):
    list_display = ['tags']

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ['h1', 'client_name', 'status', 'featured', 'published']
    list_filter = ['status', 'featured', 'published', 'category']
    search_fields = ['h1', 'client_name', 'description']
    prepopulated_fields = {'slug': ('h1',)}
    filter_horizontal = ['category', 'tag']
    date_hierarchy = 'published'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('status', 'featured', 'h1', 'slug', 'page_name')
        }),
        ('Client Information', {
            'fields': ('client_name', 'client_industry', 'project_duration', 'project_date')
        }),
        ('SEO', {
            'fields': ('keyword', 'description', 'title', 'breadcrumb', 'canonical',
                      'meta_title', 'meta_description')
        }),
        ('Open Graph', {
            'fields': ('og_type', 'og_card', 'og_site', 'og_title', 'og_description')
        }),
        ('Images', {
            'fields': ('image', 'banner_image', 'thumbnail_image', 
                      'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4')
        }),
        ('Case Study Content', {
            'fields': ('challenge', 'solution', 'results', 'content')
        }),
        ('Testimonial', {
            'fields': ('testimonial', 'testimonial_author', 'testimonial_position')
        }),
        ('Metrics', {
            'fields': (('metric_1_label', 'metric_1_value'),
                      ('metric_2_label', 'metric_2_value'),
                      ('metric_3_label', 'metric_3_value'),
                      ('metric_4_label', 'metric_4_value'))
        }),
        ('Technologies & Categories', {
            'fields': ('technologies_used', 'category', 'tag')
        }),
        ('Dates', {
            'fields': ('published',)
        }),
        ('Additional', {
            'fields': ('edits', 'schema')
        }),
    )
