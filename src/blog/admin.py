from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category , MPTTModelAdmin)
