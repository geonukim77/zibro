from django.contrib import admin

from .models import Zip, Photo

# Photo 클래스를 inline으로 나타낸다.
class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Zip)
class ZipAdmin(admin.ModelAdmin):
    list_display = ['id', 'house_value', 'house_spec', 'house_adress','house_content', 'house_basic', 'is_view', 'created_at',  'contact_inform']
    list_editable = ['is_view']
    list_filter = ['is_view', 'created_at']
    search_fields = ['id', 'house_value','house_value', 'house_spec', 'house_adress', 'house_content','house_basic', 'contact_inform' ]
  # Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
    inlines = [PhotoInline, ]
    

# # Register your models here.
# admin.site.register(Zip, ZipAdmin)
