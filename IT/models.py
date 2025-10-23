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

