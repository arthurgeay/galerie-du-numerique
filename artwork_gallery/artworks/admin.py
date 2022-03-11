from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'deathday', 'image')

admin.site.register(Category)
admin.site.register(Artist, ArtistAdmin)