from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from zips.views import list
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list, name = 'home'),

    path("zips/", include("zips.urls")),
    path("accounts/", include("accounts.urls")), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #미디어 로트로 되어있어서 settings.py에서는 MEDIA_ROOT로 설정해야함