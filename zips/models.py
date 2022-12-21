from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

#집 모델

class Zip(models.Model):
      
    # house_number = models.IntegerField(
    #     verbose_name='매물번호')
    
    house_value = models.CharField(
        verbose_name='주택가격', max_length=80,
        )

       
    house_spec = models.CharField(
        verbose_name='스펙', 
        max_length=200,
        )
    
    house_address = models.CharField(
        verbose_name='주소',
        max_length=200,
        )

    house_content = models.TextField(
        verbose_name='설명'
        )

    created_at = models.DateTimeField(
        verbose_name='업데이트 날짜'
        )

    created_by= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #모델 column을 바꾸면 에러발생하는데 해결방법->python manage.py migrate {app 이름} zero
    
    #created_by = models.CharField(    
    #     verbose_name='작성자',
    #     max_length=80, null=True
    #  )

    house_basic = models.TextField(
        verbose_name='기본정보'
        )

    contact_inform = models.TextField(
        verbose_name='연락처'
        )
    

    is_view = models.BooleanField(
        verbose_name='공개 여부',
        default=True
        )
    
    main_image = models.ImageField(
        upload_to='images/', null=True, blank=True
        )

    category = models.CharField(max_length=15, default='경기도') 

    # zip_likes = models.ManyToManyField(User, related_name='zip_likes' ,blank=True)

#하위 사진 모델
class Photo(models.Model):
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, null=True)
    sub_image = models.ImageField(upload_to='images/', null=True, blank=True)
    
#찜(scrap) 모델
class Scrap(models.Model):
    user = models.ForeignKey(to = User, on_delete=models.CASCADE, null= True)
    zip = models.ForeignKey(to = Zip, on_delete=models.CASCADE, null = True)


