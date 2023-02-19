from django.contrib import admin
from .models import Ad, Category

# Register your models here.
class AdAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'cost', 'created', 'approved')
    filter_horizontal = ('categories', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')

admin.site.register(Ad, AdAdmin)
admin.site.register(Category)



