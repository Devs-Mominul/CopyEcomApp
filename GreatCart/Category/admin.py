from django.contrib import admin
from Category.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
admin.site.register(Category, CategoryAdmin)
