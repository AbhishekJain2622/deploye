# In your `admin.py` file

from django.contrib import admin
from .models import Contact, About, Skill, Experience, Project, Post, Comment, Like,Resume

# Register your models here.
# This makes your models visible and editable in the Django admin dashboard.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.
    """
    list_display = ('name', 'email', 'subject', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'subject')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Admin configuration for the About model.
    """
    list_display = ('bio',)  # You might want to display a truncated bio


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Skill model.
    """
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Experience model.
    """
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_present')
    list_filter = ('is_present', 'company')
    search_fields = ('title', 'company')
    fieldsets = (
        (None, {
            'fields': ('title', 'company', 'location', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_present')
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Project model.
    """
    list_display = ('name', 'start_date', 'end_date', 'is_present', 'live_link', 'github_link')
    list_filter = ('is_present',)
    search_fields = ('name', 'description', 'live_link', 'github_link')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_present')
        }),
        ('Links', {
            'fields': ('live_link', 'github_link')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'updated_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author_name', 'text')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'session_id')
    list_filter = ('post',)
    
    
admin.site.register(Resume) # Register the new Resume model