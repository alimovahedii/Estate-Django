# Generated by Django 3.2.8 on 2021-11-01 16:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211101_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='advertiser',
            field=models.CharField(choices=[('شخصی', 'شخصی'), ('مشاور املاک', 'مشاور املاک')], default=(('شخصی', 'شخصی'), ('مشاور املاک', 'مشاور املاک')), max_length=30, verbose_name='آگهی دهنده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='در توضیحات آگهی به مواردی مانند شرایط اجاره، جزئیات و ویژگی\u200cهای قابل توجه، امکانات ملک اشاره کنید.', null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='article',
            name='property_contract',
            field=models.CharField(choices=[('-------', '-------'), ('اجاره', 'اجاره'), ('خرید', 'خرید')], default=(('-------', '-------'), ('اجاره', 'اجاره'), ('خرید', 'خرید')), max_length=20, verbose_name='نوع آگهی'),
        ),
    ]
