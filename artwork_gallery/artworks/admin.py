from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Artist
from .models import Artwork


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'deathday', 'image')

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'category')

admin.site.register(Category)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)