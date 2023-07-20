from django.contrib import admin
from blog.models import Category


# Register your models here.

class blogAdmin(admin.ModelAdmin):
    list_display = ('cat_id','title','description','url','add_date')

admin.site.register(Category,blogAdmin)
