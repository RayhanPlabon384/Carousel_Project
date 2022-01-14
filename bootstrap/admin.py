from django.contrib import admin
from .models import Carousel,About,Feature

# Register your models here.
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_fields = ['title']

admin.site.register(Carousel,CarouselAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ['heading','img']
    search_fields = ['heading']

admin.site.register(About,AboutAdmin)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['f_title','f_image']
    search_fields = ['f_title']

admin.site.register(Feature,FeatureAdmin)
