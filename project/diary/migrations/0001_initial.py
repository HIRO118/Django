# Generated by Django 2.2.4 on 2019-08-03 04:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('text', models.TextField(default='本文を入力してください', verbose_name='本文')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
    ]
