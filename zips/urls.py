from django.urls import path

from .views import list, detail, create, update, delete, search, scrap, scrap_list

app_name = "zips"  # 앱안에 url이 있으면

urlpatterns = [

    path('create/', create, name="create"),
    path('', list, name='list'),

    path('<int:id>/', detail, name="detail"),
    # path( '클라이언트로 받는 요청 URL', views.py에 정의 되어있는 함수, templates에서 url 호출 이름)

    path('<int:id>/update/', update, name="update"),
    path('<int:id>/delete/', delete, name="delete"),
    path('<int:id>/scrap/', scrap, name="scrap"),
    path('scrap_list/', scrap_list, name="scrap_list"),

    path('search/<str:category>/', search, name="search"),
]
