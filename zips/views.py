from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Zip, Photo
from django.core.paginator import Paginator

import datetime

# 사진 넣는 방법



#게시글 작성 HTML 응답
def create(request):
    if request.method == "POST":
        #1. 클라이언트에서 받은 값 변수 생성
        house_value = request.POST['house_value']
        house_spec = request.POST['house_spec']
        house_adress = request.POST['house_adress']
        house_content = request.POST['house_content']
        house_basic = request.POST['house_basic']
        contact_inform = request.POST['contact_inform']

        if 'main_image' in request.FILES:
            main_image = request.FILES['main_image']
        else :
            return redirect('zips:create')
            # redirect는 view.py로 이동함
        
        category = request.POST.get('category',False)
        #MultiValueDictKeyError는 get방식 사용(False 안넣으면 error)

        #created_by = request.get('username')
        
        #2. 매물 게시글 작성
        zip = Zip.objects.create(
            house_value = house_value,
            house_spec = house_spec,
            house_adress = house_adress,
            house_content = house_content,
            created_at = datetime.datetime.now(),
            #created_by = created_by,
            
            house_basic =  house_basic,
            contact_inform = contact_inform,
            main_image = main_image,
            category = category,

        )
        zip.save()            
       
        if 'house_image' in request.FILES:
            for house_image in request.FILES.getlist('house_image'):
                photo = Photo.objects.create(zip = zip, house_image = house_image)
            photo.save()
        
        else :
            return redirect('zips:create')

        return redirect('zips:list')
    
    else:
        return render(request, 'form.html')
        # redirect는 html로 이동함


def detail(request, id):
    #1. 사용자에게 전달받은 값으로 데이터 조회
    zip = Zip.objects.get(id=id)
    photo_all = Photo.objects.filter(zip=zip)
    create_zip=zip.created_by
    request_zip=str(request.user)

    if create_zip == request_zip:
        author = True
    else:
        author = False
   
    context = {"zip" : zip, "photo_all" : photo_all,'author':author}
    #2. 응답
    return render(request, 'detail.html', context)

def list(request):
    #1. Zip 클래스의 모든 객체를 zip_all에 담음
    
    zip_all = Zip.objects.all().order_by('-id')

    # 12개씩 페이지를 바꿈 -> 18개로 바꿀것
    paginator = Paginator(zip_all,9)

    #get 방식으로 정보를 받아오는 데이터
    page = request.GET.get('page')

    # 페이지를 받아 해당페이지를 리턴
    page_obj = paginator.get_page(page)
    
    context = {'zip_all':zip_all, 'page_obj': page_obj}

    return render(request, 'card.html', context) 


def update(request, id):
    if request.method == "POST":
        #1. 사용자에게 전달받은 값 데이터 조회
        zip = Zip.objects.get(id=id) #(필드명 =값)안은 조건(필드명이 값이 경우)

        #1. 클라이언트에서 받은 값 변수 생성
        house_value = request.POST['house_value']
        house_spec = request.POST['house_spec']
        house_adress = request.POST['house_adress']
        house_content = request.POST['house_content']
        house_basic = request.POST['house_basic']
        contact_inform = request.POST['contact_inform']

        if 'main_image' in request.FILES:
            main_image = request.FILES['main_image']
        else :
            return redirect('zips:create')
            # redirect는 view.py로 이동함
        
        category = request.POST.get('category',False)
        #MultiValueDictKeyError는 get방식 사용(False 안넣으면 error)
        
        #2. 매물 게시글 작성
        zip = Zip.objects.create(
            house_value = house_value,
            house_spec = house_spec,
            house_adress = house_adress,
            house_content = house_content,
            created_at = datetime.datetime.now(),
            house_basic =  house_basic,
            contact_inform = contact_inform,
            main_image = main_image,
            category = category,

        )
        zip.save()            
       
        if 'house_image' in request.FILES:
            for house_image in request.FILES.getlist('house_image'):
                photo = Photo.objects.create(zip = zip, house_image = house_image)
            photo.save()

        else :
            return redirect('zips:update')

        return redirect('zips:detail', zip.id)
    elif request.method == "GET":
        zip = Zip.objects.get(id=id)
        context = {"zip" : zip}
        return render(request, 'form.html', context)

 
def delete(request, id):
    if request.method =="POST":
        zip = Zip.objects.get(id=id)
        zip.delete()
        return redirect('zips:list')
    else:
        zip = Zip.objects.get(id=id)
        context = {"zip" : zip}
        return render(request, 'confirm_delete.html')

def search(request, category):
    
    if category== '전체':
        zip_list = Zip.objects.all().order_by('-id')        
        
    elif category == '경기도' :
        zip_list = Zip.objects.filter(category=category).order_by('-id') 

    elif category == '인천시' :
        zip_list = Zip.objects.filter(category=category).order_by('-id') 

    elif category == '강원도' :
        zip_list = Zip.objects.filter(category=category).order_by('-id') 

    elif category == '충청북도' :
        zip_list = Zip.objects.filter(category=category).order_by('-id') 

    elif category == '충청남도' :
        zip_list = Zip.objects.filter(category=category).order_by('-id') 

    # elif category == '전라북도' :
    #     zip_list = Zip.objects.filter(category=category).order_by('-id') 

    # elif category == '전라남도' :
    #     zip_list = Zip.objects.filter(category=category).order_by('-id') 

    # elif category == '경상북도' :
    #     zip_list = Zip.objects.filter(category=category).order_by('-id') 

    # elif category == '경상남도' :
    #     zip_list = Zip.objects.filter(category=category).order_by('-id') 

    # elif category == '제주도' :
    #     zip_list = Zip.objects.filter(category=category).order_by('-id')     
    
    # 12개씩 페이지를 바꿈 -> 18개로 바꿀것
    paginator = Paginator(zip_list,9)
    
     #get 방식으로 정보를 받아오는 데이터
    page = request.GET.get('page')

    # 페이지를 받아 해당페이지를 리턴
    page_obj = paginator.get_page(page)
    
    context = {'zip_list':zip_list, 'page_obj': page_obj}

    return render(request, 'card.html', context) 