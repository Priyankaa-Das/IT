from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Team(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
    description = RichTextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.name} - {self.position}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            # Ensure unique slug
            while Team.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)



class Category(models.Model):
    category = models.CharField(max_length = 156)
    def __str__(self):
        return self.category
    

class Tags(models.Model):
    tags = models.CharField(max_length = 156)
    def __str__(self):
        return self.tags   




class Blog(models.Model):
    status  = models.BooleanField(default=True)
    
    h1  = models.CharField(max_length = 156)
    slug =models.CharField(max_length = 1256,blank=True, null=True)
    page_name = models.CharField(max_length = 1256,blank=True, null=True)
    keyword = models.CharField(max_length = 156)
    description = models.CharField(max_length = 900)
    title = models.CharField(max_length = 156)
    breadcrumb = models.CharField(max_length = 156)
    canonical = models.CharField(max_length = 900, default="https://compassionatecareadvisors.com/blogs/")
    og_type =models.CharField(max_length = 156)
    og_card = models.CharField(max_length = 156)
    og_site = models.CharField(max_length = 156)
    og_title=models.CharField(max_length = 100,blank=True, null=True)
    meta_title=models.CharField(max_length = 100,blank=True, null=True)
    og_description=models.CharField(max_length = 250,blank=True, null=True)
    meta_description=models.CharField(max_length = 250,blank=True, null=True)
    image  = models.ImageField(upload_to="SEO")
    
    banner_image  = models.ImageField(upload_to="banner", blank=True, null=True)
    category = models.ManyToManyField(Category)
    tag  = models.ManyToManyField(Tags)
    updated  = models.DateField(auto_now=True)
    

    
    
    published  = models.DateField()
    content = RichTextUploadingField()
    active = True
    edits = RichTextUploadingField( blank=True, null=True)
    schema = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.h1 






class Service(models.Model):
    # Basic info
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.TextField(blank=True, null=True)
    content = RichTextUploadingField()
    
    # Banner image
    banner_image = models.ImageField(upload_to="services/banner/", blank=True, null=True)
    
    # SEO fields
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.CharField(max_length=250, blank=True, null=True)
    canonical = models.URLField(max_length=500, blank=True, null=True)
    
    # Open Graph / Social sharing
    og_title = models.CharField(max_length=200, blank=True, null=True)
    og_description = models.CharField(max_length=250, blank=True, null=True)
    og_type = models.CharField(max_length=50, default="website")
    og_url = models.URLField(max_length=500, blank=True, null=True)
    og_image = models.ImageField(upload_to="services/og/", blank=True, null=True)
    
    # Status & timestamps
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    



class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    agree_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"




class CaseStudyCategory(models.Model):
    category = models.CharField(max_length=156)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name = "Case Study Category"
        verbose_name_plural = "Case Study Categories"
    
    def __str__(self):
        return self.category
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)
        super().save(*args, **kwargs)


class CaseStudyTags(models.Model):
    tags = models.CharField(max_length=156)
    
    class Meta:
        verbose_name = "Case Study Tag"
        verbose_name_plural = "Case Study Tags"
    
    def __str__(self):
        return self.tags


class CaseStudy(models.Model):
    # Status
    status = models.BooleanField(default=True)
    
    # Basic Information
    h1 = models.CharField(max_length=156)
    slug = models.CharField(max_length=1256, blank=True, null=True, unique=True)
    page_name = models.CharField(max_length=1256, blank=True, null=True)
    
    # Client Information
    client_name = models.CharField(max_length=256, blank=True, null=True)
    client_industry = models.CharField(max_length=256, blank=True, null=True)
    project_duration = models.CharField(max_length=100, blank=True, null=True)
    project_date = models.DateField(blank=True, null=True)
    
    # SEO Fields
    keyword = models.CharField(max_length=156)
    description = models.CharField(max_length=900)
    title = models.CharField(max_length=156)
    breadcrumb = models.CharField(max_length=156)
    canonical = models.CharField(max_length=900, default="https://yoursite.com/case-studies/")
    
    # Open Graph
    og_type = models.CharField(max_length=156, default="article")
    og_card = models.CharField(max_length=156, default="summary_large_image")
    og_site = models.CharField(max_length=156, blank=True, null=True)
    og_title = models.CharField(max_length=100, blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    og_description = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    
    # Images
    image = models.ImageField(upload_to="case_study/SEO")
    banner_image = models.ImageField(upload_to="case_study/banner", blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to="case_study/thumbnail", blank=True, null=True)
    
    # Case Study Specific Fields
    challenge = RichTextUploadingField(blank=True, null=True, help_text="Describe the challenge/problem")
    solution = RichTextUploadingField(blank=True, null=True, help_text="Describe the solution provided")
    results = RichTextUploadingField(blank=True, null=True, help_text="Describe the results achieved")
    testimonial = models.TextField(blank=True, null=True, help_text="Client testimonial")
    testimonial_author = models.CharField(max_length=256, blank=True, null=True)
    testimonial_position = models.CharField(max_length=256, blank=True, null=True)
    
    # Statistics/Metrics (for displaying results)
    metric_1_label = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., 'Increase in Sales'")
    metric_1_value = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., '150%'")
    metric_2_label = models.CharField(max_length=100, blank=True, null=True)
    metric_2_value = models.CharField(max_length=50, blank=True, null=True)
    metric_3_label = models.CharField(max_length=100, blank=True, null=True)
    metric_3_value = models.CharField(max_length=50, blank=True, null=True)
    metric_4_label = models.CharField(max_length=100, blank=True, null=True)
    metric_4_value = models.CharField(max_length=50, blank=True, null=True)
    
    # Technologies/Services Used
    technologies_used = models.TextField(blank=True, null=True, help_text="Comma separated technologies/services")
    
    # Categories and Tags
    category = models.ManyToManyField(CaseStudyCategory)
    tag = models.ManyToManyField(CaseStudyTags)
    
    # Content
    content = RichTextUploadingField()
    
    # Dates
    published = models.DateField()
    updated = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Additional Fields
    featured = models.BooleanField(default=False, help_text="Mark as featured case study")
    edits = RichTextUploadingField(blank=True, null=True)
    schema = models.TextField(blank=True, null=True)
    
    # Gallery Images (for case study gallery)
    gallery_image_1 = models.ImageField(upload_to="case_study/gallery", blank=True, null=True)
    gallery_image_2 = models.ImageField(upload_to="case_study/gallery", blank=True, null=True)
    gallery_image_3 = models.ImageField(upload_to="case_study/gallery", blank=True, null=True)
    gallery_image_4 = models.ImageField(upload_to="case_study/gallery", blank=True, null=True)
    
    class Meta:
        ordering = ['-published']
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"
    
    def __str__(self):
        return self.h1
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.h1)
            slug = base_slug
            counter = 1
            # Ensure unique slug
            while CaseStudy.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('case_study_detail', kwargs={'slug': self.slug})
    


    
