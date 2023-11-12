from django.contrib import admin
from .models import Hotel, Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('uid', 'hotel', 'user', 'rating')
    list_filter = ('hotel', 'user')
    
class HotelAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'description', 'city')
    search_fields = ('name', 'description', 'city')
    list_filter = ('name', 'description', 'city')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Rating, RatingAdmin)