from django.db import models
from django.utils import timezone

# Create your models here
class CloseStation(models.Model):
    name=models.CharField(verbose_name='最寄駅名',blank=True,max_length=20)
    created_at = models.DateTimeField(verbose_name='作成日', default=timezone.now)


    def __str__(self):
        return self.name

class Cafe(models.Model):
    #カフェの情報

    name=models.CharField(verbose_name='カフェの名前',blank=True,max_length=30)
    desc=models.TextField(verbose_name='カフェの説明',blank=True)
    img=models.TextField(verbose_name='カフェの写真',blank=True)
    station=models.ForeignKey(
        CloseStation,verbose_name='最寄駅',on_delete=models.PROTECT)
    goeglemap=models.TextField(verbose_name='位置情報',blank=True)
    instagram_link=models.TextField(verbose_name='インスタ')
    phone_number=models.CharField(verbose_name='電話番号',blank=True,max_length=20)
    created_at = models.DateTimeField(verbose_name='作成日', default=timezone.now)


    def __str__(self):
        return self.name


class Comment(models.Model):
    """ブログのコメント"""

    name = models.CharField(verbose_name='お名前', max_length=30, default='名無し')
    text = models.TextField(verbose_name='本文')
    post = models.ForeignKey(Cafe, verbose_name='紐づくカフェ', on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]
