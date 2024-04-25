from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):  
    list_display = ['title', 'slug', 'author' ,'publish', 'status'] #  Columns to be displayed in the table  of posts on Django Admin Panel
    list_filter = ['status','created', 'publish', 'author']  # Filters the queryset on the main page of the admin site
    search_fields = ['title', 'body'] # Search  by title and body fields in the list view 
    prepopulated_fields = {'slug': ('title',)} #  If user enters a new title, generate a slug based on it automatically
    raw_id_fields = ['author'] #  Add a dropdown menu to select an author instead of typing it into the field
    date_hierarchy = 'publish' #  Organize by year in the changelist view
    ordering = ['status', 'publish'] #  Order by status first (draft, published), then by publish date (newest first)