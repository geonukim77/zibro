from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate, login as auth_login, logout as auth_logout)


def logout(request) :
    auth_logout(request)
    return redirect("home")

def login(request):
    if request.method == 'POST' :
    #데이터수신
        username = request.POST['username']
        password = request.POST['password']

    #데이터 사용자 확인
        user = authenticate(request, username = username, password = password)
    #로그인 처리
        if user :
            auth_login(request, user)
            return redirect('home')
        else :
            context = {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'}
            return render(request, "accounts/login.html", context)

    #응답
    else :
        return render(request, "accounts/login.html")

# def id_check(request):
#     username = request.GET['username']
#     #아이디 중복 체크
#     if User.objects.get(username=username):
#         context1 = {'error_double': '아이디가 중복되었습니다.'}
#         return render(request, 'accounts/signup.html', context1)
    
#     else :
#         context1 = {'error_double': '아이디가 사용가능합니다.'}
#         return render(request, 'accounts/signup.html', context1)
        
        

# def signup(request):
#     if request.method == 'POST':
#         if request.POST['user-password1'] == request.POST['user-password2']:
#             form = UserCreationMultiForm(request.POST, request.FILES)
#             if form.is_valid(): 
#                 user = form['user'].save()
#                 profile = form['profile'].save(commit=False)
#                 profile.user = user
#                 profile.nick = user
#                 profile.save()
#                 return redirect('signin')
#             else:
#                 user = request.POST['user-username']
#                 user = User.objects.get(username=user)
#                 messages.info(request, '아이디가 중복됩니다.')
#                 return render(request, 'signup.html')
#         else:
#             messages.info(request, '비밀번호가 다릅니다.')
#             return render(request, 'signup.html')
#     return render(request, 'signup.html')




def signup(request) :
    if request.method == 'POST':
        # 데이터 수신
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
   
        if User.objects.filter(username=username):
            context = {'error': '아이디가 중복되었습니다.'}
            return render(request, 'accounts/signup.html', context)
            

    
        # else :
        #     context1 = {'error_double': '아이디가 사용가능합니다.'}
        #     return render(request, 'accounts/signup.html', context1)

        #데이더 생성

        elif not username or not email or not password or not password1 :
            context = {'error' : '모두 채워주세요'}
            return render(request, 'accounts/signup.html', context)

        elif password == password1 :

                User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                    )
                
                return redirect('home') 
        else :
            context = {'error' : '비밀번호와 비밀번호 확인이 일치하지 않습니다.'}
        #응답
            return render(request, 'accounts/signup.html', context)

    else :
        return render(request, 'accounts/signup.html')