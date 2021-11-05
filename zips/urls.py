from django.urls import path

from .views import list, detail, create, update, delete, search
app_name = "zips" #앱안에 url이 있으면

urlpatterns = [

    path('create/', create, name = "create"),
    path('', list, name = 'list'),

    path('<int:id>/', detail, name = "detail"),
    # path( '클라이언트로 받는 요청 URL', views.py에 정의 되어있는 함수, templates(detail.html)에서 detail이란 이름을 받아서  <int:id> 형식으로 주소를 요청받음)
    path('<int:id>/update', update, name = "update"),
    path('<int:id>/delete', delete, name = "delete"),    
    path('search/<str:category>/', search, name="search"),
]
