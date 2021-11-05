from django.urls import path

from .views import signup, login, logout# id_check

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    #path('id_check/', id_check, name = 'id_check'),
]