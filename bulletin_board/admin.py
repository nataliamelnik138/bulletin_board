from django.contrib import admin

from bulletin_board.models import Advertisement, Review


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'author', 'created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created_at', 'advertisement', 'author', )
