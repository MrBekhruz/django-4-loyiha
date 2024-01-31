from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.safestring import mark_safe

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content',  'surat', 'date','category',)
    list_filter = ("date", "name",)
    def surat(self, objectcha):
        return mark_safe(f"<img src='{objectcha.image.url}' width='150' height='150' />")
admin.site.register(Category)
admin.site.register(Post, PostAdmin)