from django.db import models
from django.utils import timezone


#よく使用するフィールドはForeign Key,ManyToMany,OneToOneの３つ。

class Department(models.Model):
    name=models.CharField('部署名',max_length=20)
    created_at=models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return self.name

class Club(models.Model):
    name=models.CharField('部活名',max_length=20)
    created_at=models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name=models.CharField('名',max_length=20)
    last_name=models.CharField('姓',max_length=20)
    email=models.EmailField('メールアドレス',blank=True)
    #blank=Trueで空文字列を許可している
    department=models.ForeignKey(
        Department,verbose_name='部署',on_delete=models.PROTECT,
    )
    #Protect部署に紐づいた社員が一人でもいれば削除できないようにする。
    #Cascade：道連れに削除　
    club=models.ManyToManyField(
        Club,verbose_name='部活'
    )
    created_at=models.DateTimeField('日付',default=timezone.now)
    address=models.CharField('住所',max_length=20,blank=True)

    def __str__(self):
        return '{0}{1}/Accenture {2}'.format(self.last_name,self.first_name,self.department)

# Create your models here.
