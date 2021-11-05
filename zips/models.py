from django.db import models
from django.db.models.fields.files import ImageField

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
    
    house_adress = models.CharField(
        verbose_name='주소',
        max_length=200,
        )

    house_content = models.TextField(
        verbose_name='설명'
        )

    created_at = models.DateTimeField(
        verbose_name='업데이트 날짜'
        )

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

class Photo(models.Model):
    zip = models.ForeignKey(Zip, on_delete=models.CASCADE, null=True)
    house_image = models.ImageField(upload_to='images/', null=True, blank=True)
    