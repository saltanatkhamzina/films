from django.contrib import admin
from .models import Profile, Category

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'phone', 'image', 'category', 'description']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)