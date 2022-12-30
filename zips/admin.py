from django.contrib import admin

from .models import Zip, Photo, Scrap

# Photo 클래스를 inline으로 나타낸다.


class PhotoInline(admin.TabularInline):
    model = Photo


class ScrapInline(admin.TabularInline):
    model = Scrap


@admin.register(Zip)
class ZipAdmin(admin.ModelAdmin):
    list_display = ['id', 'house_value', 'house_spec',
                    'house_address', 'is_view', 'created_at',  'contact_inform']
    list_editable = ['is_view']
    list_filter = ['is_view', 'created_at']
    search_fields = ['id', 'house_value', 'house_value',
                     'house_spec', 'house_address', 'contact_inform']
  # Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다.
    inlines = [PhotoInline, ScrapInline]
